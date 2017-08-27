#!/usr/bin/env python
"""
[2017-08-11] Challenge #326 [Hard] Multifaceted alphabet blocks
https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/
"""

import collections

class BrickException(Exception):
    pass

class Brick(object):
    """
    An alphabet brick with variable number of faces

    :param int faces: Number of faces
    """
    def __init__(self, faces):
        self.faces = faces
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
        if len(self.letters) >= self.faces:
            raise BrickException("No free faces remaining")
        elif self.contains(letter):
            raise BrickException("Brick already contains '{0}'".format(letter))
        else:
            self.letters.append(letter)
        
    def remove(self, letter):
        """
        Remove a letter from the brick

        :param string letter: Letter to remove from the brick face
        :raises ValueError:
        """
        self.letters.remove(letter)

    def replace(self, oldLetter, newLetter):
        self.remove(oldLetter)
        self.add(newLetter)

class Bricks(object):
    """
    A series of alphabet bricks
    """
    def __init__(self):
        self.bricks = []
    
    def __repr__(self):
        return repr(self.bricks)

    def __getitem__(self, key):
        return self.bricks[key]

    def add(self):
        """
        Add another brick to the series with N+1 faces

        Returns the added brick
        """
        brick = Brick(len(self.bricks) + 1)
        self.bricks.append(brick)
        return brick


def sortedDictValues(inputDict, reverse=False):
    """
    Returns the given dictionary as a list of keys sorted by value then key::

        {"spam": 0, "eggs": 1, "ham": 1} => ["spam", "eggs", "ham"]

    :param dict inputDict:
    :param bool reverse: Reversed sorting
    :rtype: list
    """
    sortedDict = sorted(inputDict.items(), key=lambda item: (item[1], item[0]), reverse=reverse)
    values = [k for k, v in sortedDict]
    return values

def lettersDecreasing(challengeInput):
    """
    Return letters in the ``challengeInput`` in decreasing frequency order::

        "banana" => ["a", "n", "b"]

    :param string challengeInput:
    :rtype: list
    """
    letterFrequencies = collections.Counter(challengeInput)
    lettersDecreasing = sortedDictValues(letterFrequencies, reverse=True)
    return lettersDecreasing

def wordsDecreasing(challengeInput):
    """
    Return words in the ``challengeInput`` in decreasing length order::

        "spam\nbanana" => ["banana", "spam"]

    :param string challengeInput:
    :rtype: list
    """
    words = [w.strip().upper() for w in challengeInput.split("\n")]
    wordLengths = {w: len(w) for w in words}
    wordsDecreasing = sortedDictValues(wordLengths, reverse=True)
    return wordsDecreasing

def main(challengeInput):
    words = wordsDecreasing(challengeInput)
    letters = lettersDecreasing("".join(words))

    bricks = Bricks()

    for word in words:
        currentBrickIndex = 0
        for letter in letters:
            if letter in word:
                try:
                    currentBrick = bricks[currentBrickIndex]
                except IndexError:
                    currentBrick = bricks.add()
                currentBrick.add(letter)
                

    print(bricks)
    return challengeInput

if __name__ == "__main__":
    main()