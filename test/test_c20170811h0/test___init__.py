#!/usr/bin/env python

import unittest

import dailyprogrammer.c20170811h0 as challenge

class TestSortedDictValues(unittest.TestCase):
    def testIntegers(self):
        testInput = {"a": 0, "b": 1, "c": 2}
        expected = ["a", "b", "c"]
        actual = challenge.sortedDictValues(testInput)
        self.assertEqual(actual, expected)

    def testReverse(self):
        testInput = {"a": 0, "b": 1, "c": 2}
        expected = ["c", "b", "a"]
        actual = challenge.sortedDictValues(testInput, reverse=True)
        self.assertEqual(actual, expected)

    def testStrings(self):
        testInput = {"a": "x", "b": "y", "c": "z"}
        expected = ["a", "b", "c"]
        actual = challenge.sortedDictValues(testInput)
        self.assertEqual(actual, expected)

class TestLettersDecreasing(unittest.TestCase):
    def testWord(self):
        testInput = "banana"
        expected = ["a", "n", "b"]
        actual = challenge.lettersDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWordDeterministic(self):
        testInput = "brick"
        expected = ["r", "k", "i", "c", "b"]
        actual = challenge.lettersDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWords(self):
        testInput = "".join(["banana", "spam"])
        expected = ["a", "n", "s", "p", "m", "b"]
        actual = challenge.lettersDecreasing(testInput)
        self.assertEqual(actual, expected)

class TestWordsDecreasing(unittest.TestCase):
    def testWord(self):
        testInput = "banana"
        expected = ["banana"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWords(self):
        testInput = "spam\nbanana"
        expected = ["banana", "spam"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWordsDeterministic(self):
        testInput = "eels\nspam\nbanana"
        expected = ["banana", "spam", "eels"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)
