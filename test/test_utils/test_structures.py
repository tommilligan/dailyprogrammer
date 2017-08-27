#!/usr/bin/env python

import unittest

import dailyprogrammer.utils.structures as structures

class Example(object):
    pass

class TestSortedDictValues(unittest.TestCase):
    def testIntegers(self):
        testInput = {"a": 0, "b": 1, "c": 2}
        expected = ["a", "b", "c"]
        actual = structures.sortedDictValues(testInput)
        self.assertEqual(actual, expected)

    def testReverse(self):
        testInput = {"a": 0, "b": 1, "c": 2}
        expected = ["c", "b", "a"]
        actual = structures.sortedDictValues(testInput, reverse=True)
        self.assertEqual(actual, expected)

    def testStrings(self):
        testInput = {"a": "x", "b": "y", "c": "z"}
        expected = ["a", "b", "c"]
        actual = structures.sortedDictValues(testInput)
        self.assertEqual(actual, expected)

    def testDuplicateValues(self):
        testInput = {"a": 0, "b": 1, "c": 2, "z": 1, "y": 1}
        expected = ["a", "b", "y", "z", "c"]
        actual = structures.sortedDictValues(testInput)
        self.assertEqual(actual, expected)

    def testDuplicateValuesReversed(self):
        testInput = {"a": 0, "b": 1, "c": 2, "z": 1, "y": 1}
        expected = ["c", "z", "y", "b", "a"]
        actual = structures.sortedDictValues(testInput, reverse=True)
        self.assertEqual(actual, expected)

