#!/usr/bin/env python

import unittest

import dailyprogrammer.challenges.c20170811h0 as challenge

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
        testInput = ["banana"]
        expected = ["banana"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWords(self):
        testInput = ["spam", "banana"]
        expected = ["banana", "spam"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

    def testWordsDeterministic(self):
        testInput = ["eels", "spam", "banana"]
        expected = ["banana", "spam", "eels"]
        actual = challenge.wordsDecreasing(testInput)
        self.assertEqual(actual, expected)

class TestBrick(unittest.TestCase):
    def setUp(self):
        self.brick = challenge.Brick(2)

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

    def testAddTooMany(self):
        self.brick.add("F")
        self.brick.add("a")
        self.brick.add("c")
        with self.assertRaises(challenge.BrickException):
            self.brick.add("e")

    def testRemove(self):
        self.brick.add("F")
        self.brick.add("a")
        self.brick.remove("F")
        self.assertEqual(self.brick.letters, ["a"])

    def testRemoveInvalid(self):
        with self.assertRaises(ValueError):
            self.brick.remove("F")

    def testReplace(self):
        self.brick.add("F")
        self.brick.replace("F", "a")
        self.assertEqual(self.brick.letters, ["a"])

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

    def testRepr(self):
        self.bricks.add()
        self.bricks.add()
        brick = self.bricks.add()
        for c in "CAT":
            brick.add(c)
        expected = "[[], [], ['C', 'A', 'T']]"
        self.assertEqual(str(self.bricks), expected)

    def testContainsTrue(self):
        brick = self.bricks.add()
        brick = brick.add("x")
        expected = brick
        actual = self.bricks.contains("x")
        self.assertEqual(actual, expected)

    def testContainsFalse(self):
        with self.assertRaises(ValueError):
            self.bricks.contains("F")

class TestGenerateAlphabetBricks(unittest.TestCase):
    def testSimple(self):
        expected = [["s"], ["p"], ["m"], ["a"]]
        actual = challenge.generateAlphabetBricks(["spam"])
        self.assertEqual(actual, expected)

    def testSimpleRepeats(self):
        expected = [["a"], ["a"], ["a"], ["n"], ["n"], ["b"]]
        actual = challenge.generateAlphabetBricks(["banana"])
        self.assertEqual(actual, expected)

    def testSimpleOverlap(self):
        expected = [["a"], ["a"], ["a"], ["n"], ["n"], ["b"]]
        actual = challenge.generateAlphabetBricks(["banana", "ban"])
        self.assertEqual(actual, expected)

    def testSimpleDistinct(self):
        expected = [["a"], ["a", "s"], ["a", "p"], ["n", "m"], ["n"], ["b"]]
        actual = challenge.generateAlphabetBricks(["banana", "spam"])
        self.assertEqual(actual, expected)

    def testManyShort(self):
        expected = [["t"], ["u", "o"], ["e", "a"]]
        actual = challenge.generateAlphabetBricks(["ta", "te", "to", "tu"])
        self.assertEqual(actual, expected)

    def testManyShortSmart(self):
        expected = [["t"], ["b", "o"], ["b", "e", "a"], ["u"]]
        actual = challenge.generateAlphabetBricks(["ta", "te", "to", "tubb"])
        self.assertEqual(actual, expected)

    def testLongestLast(self):
        expected = [["t"], ["c", "o"], ["b", "e"]]
        actual = challenge.generateAlphabetBricks(["to", "te", "tbc"])
        self.assertEqual(actual, expected)

    def testLongestFirst(self):
        expected = [["t"], ["c", "o"], ["b", "e"]]
        actual = challenge.generateAlphabetBricks(["tbc", "te", "to"])
        self.assertEqual(actual, expected)

    def testLongestLastZ(self):
        expected = [["t"], ["z", "o"], ["x", "e"]]
        actual = challenge.generateAlphabetBricks(["to", "te", "txz"])
        self.assertEqual(actual, expected)

    def testLongestFirstZ(self):
        expected = [["t"], ["z", "o"], ["x", "e"]]
        actual = challenge.generateAlphabetBricks(["txz", "te", "to"])
        self.assertEqual(actual, expected)

class TestMain(unittest.TestCase):
    def testSimple(self):
        expected = "m\na\nsh\np"
        actual = challenge.main("spam\nham")
        self.assertEqual(actual, expected)

