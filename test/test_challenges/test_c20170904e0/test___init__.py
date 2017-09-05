#!/usr/bin/env python

import unittest

import dailyprogrammer.challenges.c20170904e0 as challenge

class TestMinimumBoundingOrthogonal(unittest.TestCase):
    def testSingle(self):
        testInput = [(0, 0, 1)]
        expected = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        actual = challenge.minimumBoundingOrthogonal(testInput)
        self.assertEqual(actual, expected)

    def testMultiple(self):
        testInput = [(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0, 0.5, 0.5)]
        expected = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        actual = challenge.minimumBoundingOrthogonal(testInput)
        self.assertEqual(actual, expected)


class TestMain(unittest.TestCase):
    def testConversion(self):
        testInput = "0,0,1\n0.5,-0.5,1"
        expected = "(-1.000, -1.500), (-1.000, 1.000), (1.500, 1.000), (1.500, -1.500)"
        actual = challenge.main(testInput)
        self.assertEqual(actual, expected)

