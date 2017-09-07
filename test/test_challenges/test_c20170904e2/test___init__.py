#!/usr/bin/env python

import unittest

import dailyprogrammer.challenges.c20170904e2 as challenge

INF = float('inf')

class TestCoTangent(unittest.TestCase):
    def testSameSize(self):
        testInput = ((0.5, 0.5, 1), (2.5, 1.5, 1))
        expected = (0.5, 1.3680339887498947)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSteep(self):
        testInput = ((0.5, 0.5, 1), (1.5, 2.5, 1))
        expected = (2, 1.7360679774997898)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSlopingDown(self):
        testInput = ((0.5, 0.5, 1), (2.5, -0.5, 1))
        expected = (-0.5, 1.8680339887498947)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeSlopingDownSteep(self):
        testInput = ((0.5, 0.5, 1), (1.5, -1.5, 1))
        expected = (-2, 3.73606797749979)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeHorizontal(self):
        testInput = ((0.5, 0.5, 1), (1.5, 0.5, 1))
        expected = (0, 1.5)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeVertical(self):
        testInput = ((0.5, 0.5, 1), (0.5, 1.5, 1))
        expected = (INF, -0.5)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def testSameSizeReversed(self):
        testInput = ((2.5, 1.5, 1), (0.5, 0.5, 1))
        expected = (0.5, 1.3680339887498947)
        actual = challenge.coTangent(*testInput)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)



"""
class TestMain(unittest.TestCase):
    def testConversion(self):
        testInput = "0,0,1\n0.5,-0.5,1"
        expected = "(-1.000, -1.500), (-1.000, 1.000), (1.500, 1.000), (1.500, -1.500)"
        actual = challenge.main(testInput)
        self.assertEqual(actual, expected)
"""
