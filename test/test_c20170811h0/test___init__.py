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
        expected = ["BANANA"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWords(self):
        testInput = "spam\nbanana"
        expected = ["BANANA", "SPAM"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWordsDeterministic(self):
        testInput = "eels\nspam\nbanana"
        expected = ["BANANA", "SPAM", "EELS"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

class TestBrick(unittest.TestCase):
    def setUp(self):
        self.brick = challenge.Brick(3)

    def testDefault(self):
        self.assertEqual(self.brick.letters, [])
        self.assertEqual(self.brick.faces, 3)

    def testAdd(self):
        self.brick.add("F")
        self.assertEqual(self.brick.letters, ["F"])

    def testAddRepeat(self):
        self.brick.add("F")
        with self.assertRaises(challenge.BrickException):
            self.brick.add("F")

    def testRemove(self):
        self.brick.add("F")
        self.brick.add("A")
        self.brick.remove("F")
        self.assertEqual(self.brick.letters, ["A"])

    def testRemoveInvalid(self):
        with self.assertRaises(ValueError):
            self.brick.remove("F")

    def testReplace(self):
        self.brick.add("F")
        self.brick.replace("F", "A")
        self.assertEqual(self.brick.letters, ["A"])

    def testContainsTrue(self):
        self.brick.add("F")
        expected = True
        actual = self.brick.contains("F")
        self.assertEqual(actual, expected)

    def testContainsFalse(self):
        expected = False
        actual = self.brick.contains("F")
        self.assertEqual(actual, expected)

    def testRepr(self):
        for c in "CAT":
            self.brick.add(c)
        expected = "['C', 'A', 'T']"
        self.assertEqual(str(self.brick), expected)

class TestBricks(unittest.TestCase):
    def setUp(self):
        self.bricks = challenge.Bricks()
    
    def testDefault(self):
        self.assertEqual(self.bricks.bricks, [])

    def testAdd(self):
        self.bricks.add()
        self.assertEqual(len(self.bricks.bricks), 1)
        self.assertEqual(self.bricks.bricks[0].faces, 1)

    def testAddReturn(self):
        actual = self.bricks.add()
        self.assertEqual(actual.faces, 1)

    def testGetBrick(self):
        self.bricks.add()
        expected = self.bricks.bricks[0]
        actual = self.bricks[0]
        self.assertEqual(actual, expected)

