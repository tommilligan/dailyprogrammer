#!/usr/bin/env python
"""
[2017-08-11] Challenge #326 [Hard] Multifaceted alphabet blocks
https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/
"""

import collections
import copy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def objectLogger(o):
    name = o.__module__ + "." + o.__class__.__name__
    newLogger = logging.getLogger(name)
    newLogger.setLevel(logging.DEBUG)
    return newLogger

class BrickException(Exception):
    pass

class Brick(object):
    """
    An alphabet brick with variable number of faces

    :param int id: Position in sequence (also number of faces)
    """
    def __init__(self, id):
        self.logger = objectLogger(self)

        self.id = id
        self.faces = id + 1
        self.letters = []

    def __repr__(self):
        return repr(self.letters)

    def contains(self, letter):
        """
        Returns whether the brick currently contains a letter

        :param string letter: Letter to check
        """
        return letter in self.letters

    def add(self, letter):
        """
        Add a letter to a face on the brick

        If no faces are available or the letter already exists, ``BrickException`` is raised

        :param string letter: Letter to add to the brick face
        :raises: BrickException
        """
        self.logger.debug("Adding letter '%s' to brick" % letter)
        if len(self.letters) >= self.faces:
            raise BrickException("No free faces remaining")
        elif self.contains(letter):
            raise BrickException("Brick already contains '{0}'".format(letter))
        else:
            self.letters.append(letter)
        return self
        
    def remove(self, letter):
        """
        Remove a letter from the brick

        :param string letter: Letter to remove from the brick face
        :raises ValueError:
        """
        self.logger.debug("Removing letter '%s' from brick" % letter)
        self.letters.remove(letter)
        return self

    def replace(self, oldLetter, newLetter):
        self.remove(oldLetter)
        self.add(newLetter)
        return self

class Bricks(object):
    """
    A series of alphabet bricks
    """
    def __init__(self):
        self.logger = objectLogger(self)

        self.bricks = []
    
    def __repr__(self):
        return repr(self.bricks)

    def __getitem__(self, key):
        self.logger.debug("Getting brick with key '%d'" % key)
        return self.bricks[key]

    def data(self):
        """
        Returns raw brick data as a nested list
        """
        return [[l for l in brick.letters] for brick in self.bricks]

    def add(self):
        """
        Add another brick to the series with N+1 faces

        Returns the added brick
        """
        self.logger.debug("Adding another brick")
        brick = Brick(len(self.bricks))
        self.bricks.append(brick)
        return brick

    def contains(self, letter, ignore=[]):
        """
        Returns the first brick containing the letter

        Raises ValueError if the letter is not found

        :param string letter: Letter to check
        :param list ignore: List of brick ids to ignore during check
        :raises: ValueError
        :rtype: Brick
        """
        self.logger.debug("Checking if bricks contain '%s'", letter)
        self.logger.debug("Ignoring %s", ignore)
        series = [b.contains(letter) and b.id not in ignore for b in self.bricks]
        try:
            i = series.index(True)
        except ValueError:
            raise ValueError("'{0}' not found in bricks {1}".format(letter, self.bricks))
        return self.bricks[i]

class BricksHandler(object):
    """
    A handler for building a set of bricks
    """
    def __init__(self, bricks):
        self.logger = objectLogger(self)

        self.bricks = bricks

        self.ignoreBricks = []
        self.reset()

    def reset(self):
        self.logger.debug("Resetting")
        self.ignoreBricks = []

    def ignore(self, id):
        self.ignoreBricks.append(id)

    def addLetterToBrick(self, letter, brick):
        self.logger.debug("Trying to add letter to brick '%s'" % brick.id)
        brick.add(letter)
        self.ignore(brick.id)

    def ensureLetterInBricks(self, letter):
        self.logger.debug("Ensuring %s in bricks", letter)
        brickIndex = 0
        while True:
            try:
                brick = self.bricks.contains(letter, ignore=self.ignoreBricks)
                self.logger.debug("Letter already in brick %s" % brick.id)
                self.ignore(brick.id)
                break
            except ValueError:
                self.logger.debug("Letter not already in bricks")
                try:
                    brick = self.bricks[brickIndex]
                    if brick.id in self.ignoreBricks:
                        self.logger.debug("We are ignoring brick index '%d', incrementing" % brickIndex)
                        brickIndex += 1
                        continue
                    try:
                        self.addLetterToBrick(letter, brick)
                        break
                    except BrickException as e:
                        self.logger.debug("Could not add letter to brick index '%d' (%s), incrementing" % (brickIndex, e))
                        brickIndex += 1
                        continue

                except IndexError:
                    self.logger.debug("Reached the end of current bricks")
                    brick = self.bricks.add()
                    self.addLetterToBrick(letter, brick)
                    break


def sortedDictValues(inputDict, reverse=False):
    """
    Returns the given dictionary as a list of keys sorted deterministically by value then key::

        {"spam": 0, "eggs": 1, "ham": 1} => ["spam", "eggs", "ham"]

    :param dict inputDict:
    :param bool reverse: Reversed sorting
    :rtype: list
    """
    sortedDict = sorted(inputDict.items(), key=lambda item: (item[1], item[0]), reverse=reverse)
    values = [k for k, v in sortedDict]
    return values

def lettersDecreasing(para):
    """
    Return letters in the ``challengeInput`` in decreasing frequency order::

        "banana" => ["a", "n", "b"]

    :param string challengeInput:
    :rtype: list
    """
    letterFrequencies = collections.Counter(para)
    lettersDecreasing = sortedDictValues(letterFrequencies, reverse=True)
    return lettersDecreasing

def wordsDecreasing(words):
    """
    Return words in the ``challengeInput`` in decreasing length order::

        "spam\nbanana" => ["banana", "spam"]

    :param string challengeInput:
    :rtype: list
    """
    wordLengths = {w: len(w) for w in words}
    wordsDecreasing = sortedDictValues(wordLengths, reverse=True)
    return wordsDecreasing

def generateAlphabetBricks(words):
    """
    Accepts a list of words and returns an internal representation of a bricks sequence.

    :param list words:
    :rtype: list
    """
    words = wordsDecreasing(words)
    letters = lettersDecreasing("".join(words))

    bricks = Bricks()
    builder = BricksHandler(bricks)

    for word in words:
        logger.info("Processing '%s'" % word)
        builder.reset()
        for letter in sorted(word, key=lambda c: letters.index(c)):
            builder.ensureLetterInBricks(letter)
                
    return bricks.data()


def main(challengeInput):
    words = [w.strip() for w in challengeInput.split("\n")]
    bricksData = generateAlphabetBricks(words)
    faces = ["".join(brick) for brick in bricksData]
    challengeOutput = "\n".join(faces)
    return challengeOutput

if __name__ == "__main__":
    main()