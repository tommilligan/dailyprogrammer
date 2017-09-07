#!/usr/bin/env python

import unittest

import dailyprogrammer.challenges.c20170904e2 as challenge

INF = float('inf')

class TestCoTangent(unittest.TestCase):
    def testSameSize(self):
        testInput = ((0, 0, 1), (2, 1, 1))
        expected = (0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSteep(self):
        testInput = ((0, 0, 1), (1, 2, 1))
        expected = (2, 2.2360679774997894)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSlopingDown(self):
        testInput = ((0, 0, 1), (2, -1, 1))
        expected = (-0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSlopingDownSteep(self):
        testInput = ((0, 0, 1), (1, -2, 1))
        expected = (-2, 2.23606797749979029)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeHorizontal(self):
        testInput = ((0, 0, 1), (1, 0, 1))
        expected = (0, 1)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeVertical(self):
        testInput = ((0, 0, 1), (0, 1, 1))
        expected = (INF, -1)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeReversedArguments(self):
        testInput = ((2, 1, 1), (0, 0, 1))
        expected = (0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeBottom(self):
        testInput = ((0, 0, 1), (2, 1, 1))
        expected = (0.5, -1.118033988749895)
        actual = challenge.coTangent(*testInput, bottom=True)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeHorizontalBottom(self):
        testInput = ((0, 0, 1), (1, 0, 1))
        expected = (0, -1)
        actual = challenge.coTangent(*testInput, bottom=True)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeVerticalBottom(self):
        testInput = ((0, 0, 1), (0, 1, 1))
        expected = (INF, 1)
        actual = challenge.coTangent(*testInput, bottom=True)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testLargerSize(self):
        testInput = ((0, 0, 1), (12, 10, 3))
        expected = (1.0784561912118524, 1.4707371472711144)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSmallerSize(self):
        testInput = ((0, 0, 1), (12, 10, 1 / 3))
        expected = (0.763438390645699, 1.2581089683774196)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)
   