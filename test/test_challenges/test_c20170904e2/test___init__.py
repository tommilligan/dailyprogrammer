#!/usr/bin/env python

import unittest

import dailyprogrammer.challenges.c20170904e2 as challenge

INF = float('inf')

def assertLineEqual(self, actual, expected):
    """
    Assert lines stored as a (float, float) are almost equal
    """
    try:
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)
    except AssertionError as e:
        raise AssertionError("Line %s was expected to be %s; %s" % (actual, expected, e))

def assertLinesEqual(self, actual, expected):
    """
    Assert an array of lines are almost equal
    """
    try:
        for a, e in zip(actual, expected):
            assertLineEqual(self, a, e)
    except AssertionError as e:
        raise AssertionError("Lines %s were expected to be %s; %s" % (actual, expected, e))

class TestCoTangent(unittest.TestCase):
    def testSameSize(self):
        testInput = ((0, 0, 1), (2, 1, 1))
        expected = (0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeSteep(self):
        testInput = ((0, 0, 1), (1, 2, 1))
        expected = (2, 2.2360679774997894)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeSlopingDown(self):
        testInput = ((0, 0, 1), (2, -1, 1))
        expected = (-0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeSlopingDownSteep(self):
        testInput = ((0, 0, 1), (1, -2, 1))
        expected = (-2, 2.23606797749979029)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeHorizontal(self):
        testInput = ((0, 0, 1), (1, 0, 1))
        expected = (0, 1)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeVertical(self):
        testInput = ((0, 0, 1), (0, 1, 1))
        expected = (INF, -1)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeReversedArguments(self):
        testInput = ((2, 1, 1), (0, 0, 1))
        expected = (0.5, 1.118033988749895)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameSizeBottom(self):
        testInput = ((0, 0, 1), (2, 1, 1))
        expected = (0.5, -1.118033988749895)
        actual = challenge.coTangent(*testInput, bottom=True)
        assertLineEqual(self, actual, expected)

    def testSameSizeHorizontalBottom(self):
        testInput = ((0, 0, 1), (1, 0, 1))
        expected = (0, -1)
        actual = challenge.coTangent(*testInput, bottom=True)
        assertLineEqual(self, actual, expected)

    def testSameSizeVerticalBottom(self):
        testInput = ((0, 0, 1), (0, 1, 1))
        expected = (INF, 1)
        actual = challenge.coTangent(*testInput, bottom=True)
        assertLineEqual(self, actual, expected)

    def testLargerSize(self):
        testInput = ((0, 0, 1), (12, 10, 3))
        expected = (1.0784561912118524, 1.4707371472711144)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSmallerSize(self):
        testInput = ((0, 0, 1), (12, 10, 1 / 3))
        expected = (0.763438390645699, 1.2581089683774196)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testSameCenter(self):
        testInput = ((0, 0, 1), (0, 0, 2))
        with self.assertRaises(challenge.GeometryException):
            challenge.coTangent(*testInput)

    def testSubsetting(self):
        testInput = ((0, 0, 1), (0.25, 0, 0.25))
        with self.assertRaises(challenge.GeometryException):
            challenge.coTangent(*testInput)

    def testTouchingInner(self):
        testInput = ((0, 0, 1), (0.5, 0, 0.5))
        expected = (INF, 1)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testTouchingInnerBottom(self):
        testInput = ((0, 0, 1), (0.5, 0, 0.5))
        expected = (INF, 1)
        actual = challenge.coTangent(*testInput, bottom=True)
        assertLineEqual(self, actual, expected)

    def testTouchingOuter(self):
        testInput = ((0, 0, 1), (1.5, 0, 0.5))
        expected = (-0.35355339059327373, 1.0606601717798212)
        actual = challenge.coTangent(*testInput)
        assertLineEqual(self, actual, expected)

    def testTouchingOuterBottom(self):
        testInput = ((0, 0, 1), (1.5, 0, 0.5))
        expected = (0.35355339059327373, -1.0606601717798212)
        actual = challenge.coTangent(*testInput, bottom=True)
        assertLineEqual(self, actual, expected)

class TestFindStartingCircle(unittest.TestCase):
    def testSingle(self):
        testInput = [(0, 0, 1)]
        expected = (0, 0, 1)
        actual = challenge.findStartingCircle(testInput)
        self.assertEqual(actual, expected)

    def testSimple(self):
        testInput = [(0, 0, 1), (2, 2, 1)]
        expected = (0, 0, 1)
        actual = challenge.findStartingCircle(testInput)
        self.assertEqual(actual, expected)

    def testDouble(self):
        testInput = [(0, 0, 1), (0, -2, 1)]
        expected = (0, -2, 1)
        actual = challenge.findStartingCircle(testInput)
        self.assertEqual(actual, expected)

    def testOverlapping(self):
        testInput = [(0, 0, 1), (0, 2, 5), (4, -1, 0.5)]
        expected = (0, 2, 5)
        actual = challenge.findStartingCircle(testInput)
        self.assertEqual(actual, expected)

    def testSimpleBottom(self):
        testInput = [(0, 0, 1), (2, 2, 1)]
        expected = (2, 2, 1)
        actual = challenge.findStartingCircle(testInput, bottom=True)
        self.assertEqual(actual, expected)

    def testDouble(self):
        testInput = [(0, 0, 1), (0, -2, 1)]
        expected = (0, 0, 1)
        actual = challenge.findStartingCircle(testInput, bottom=True)
        self.assertEqual(actual, expected)

class TestIntraTangents(unittest.TestCase):
    def testSingle(self):
        testInput = ((0, 0, 1), [(0, 0, 1)])
        expected = []
        actual = challenge.intraTangents(*testInput)
        for a, e in zip(actual, expected):
            assertLineEqual(self, a[0], e[0])
            self.assertEqual(a[1], e[1])

    def testSimple(self):
        testInput = ((0, 0, 1), [(0, 0, 1), (3, 3, 1), (4, -1, 0.5)])
        expected = [((1.0, 1.414213562373095), (3, 3, 1)),
                    ((-0.38389448844241986, 1.0711559075393586), (4, -1, 0.5))]
        actual = challenge.intraTangents(*testInput)
        for a, e in zip(actual, expected):
            assertLineEqual(self, a[0], e[0])
            self.assertEqual(a[1], e[1])


class TestConvexHullDisksHalf(unittest.TestCase):
    def testSimple(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.0, 1.414213562373095), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertLinesEqual(self, actual, expected)

    def testSimpleBottom(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(0, -1)]
        actual = challenge.convexHullDisksHalf(testInput, bottom=True)
        assertLinesEqual(self, actual, expected)

    def testStackedVertical(self):
        testInput = [(0, 0, 1), (0, 1, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(INF, -1), (0.6666666666666666, 2.201850425154663), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertLinesEqual(self, actual, expected)

    def testStackedHorizontal(self):
        testInput = [(0, 0, 1), (2, 3, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.5, 1.8027756377319948), (0.0, 4.0), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertLinesEqual(self, actual, expected)

class TestConvexHullDisks(unittest.TestCase):
    def testSimple(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.0, 1.414213562373095), (-1, 7.414213562373094), (0, -1)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertLinesEqual(self, actual, expected)
