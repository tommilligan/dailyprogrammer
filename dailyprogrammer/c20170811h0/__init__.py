#!/usr/bin/env python
"""
[2017-08-11] Challenge #326 [Hard] Multifaceted alphabet blocks
https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/
"""

import collections

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
    words = [w.strip() for w in challengeInput.split("\n")]
    wordLengths = {w: len(w) for w in words}
    wordsDecreasing = sortedDictValues(wordLengths, reverse=True)
    return wordsDecreasing

def main(challengeInput):
    words = wordsDecreasing(challengeInput)
    letters = lettersDecreasing("".join(words))
    return challengeInput

if __name__ == "__main__":
    main()