#!/usr/bin/env python

from math import pi
import unittest

import dailyprogrammer.challenges.c20170904e2 as challenge

INF = float('inf')

# Testing functions

def exactZip(*args):
    """
    Zip, but raise a ValueError if the iterables are different length
    
    :param args: Multiple iterables to zip, each with a known length
    """
    lengths = [len(a) for a in args]
    if len(set(lengths)) <= 1:
        return zip(*args)
    else:
        raise ValueError("Iterables were of different lengths; {0}".format(args))

def assertTupleAlmostEqual(self, actual, expected):
    """
    Assert lines stored as a (float, float) are almost equal
    """
    try:
        for a, e in exactZip(actual, expected):
            self.assertAlmostEqual(a, e)
    except AssertionError as e:
        raise AssertionError("Tuple {0} was expected to be {1}; {2}".format(actual, expected, e))

def assertTuplesAlmostEqual(self, actual, expected):
    """
    Assert an array of lines are almost equal
    """
    try:
        for a, e in exactZip(actual, expected):
            assertTupleAlmostEqual(self, a, e)
    except AssertionError as e:
        raise AssertionError("Lines {0} were expected to be {1}; {2}".format(actual, expected, e))

class TestExactZip(unittest.TestCase):
    def testEqualLength(self):
        testInput = ((0.5, 1.0), (0.5, 1.0))
        expected = [(0.5, 0.5), (1.0, 1.0)]
        actual = list(exactZip(*testInput))
        self.assertEqual(actual, expected)

    def testUnequalLength(self):
        testInput = ((0.5, 1.0, 2.0), (0.5, 1.0))
        with self.assertRaises(ValueError):
            exactZip(*testInput)

class TestAssertLineEqual(unittest.TestCase):
    def testEqual(self):
        testInput = ((0.5, 1.0), (0.5, 1.0))
        assertTupleAlmostEqual(self, *testInput)

    def testAlmostEqual(self):
        testInput = ((0.5, 1.0), (0.5, 0.9999999999999))
        assertTupleAlmostEqual(self, *testInput)

    def testNotEqual(self):
        testInput = ((0.5, 1.1), (0.5, 1))
        with self.assertRaises(AssertionError):
            assertTupleAlmostEqual(self, *testInput)

class TestAssertLinesEqual(unittest.TestCase):
    def testEqual(self):
        testInput = ([(0.5, 1.0), (1.5, 2.0)], [(0.5, 1.0), (1.5, 2.0)])
        assertTuplesAlmostEqual(self, *testInput)

    def testAlmostEqual(self):
        testInput = ([(0.5, 1.0), (1.5, 2.0)], [(0.5, 1.0000000000001), (1.5, 2.0)])
        assertTuplesAlmostEqual(self, *testInput)

    def testNotEqual(self):
        testInput = ([(0.5, 1.0), (1.5, 2.0)], [(0.5, 6.0), (1.5, 2.0)])
        with self.assertRaises(AssertionError):
            assertTuplesAlmostEqual(self, *testInput)

# Actual module tests

class TestRotatePoint(unittest.TestCase):
    def testQuarter(self):
        testInput = ((1, 0), pi / 2)
        expected = (0, 1)
        actual = challenge.rotatePoint(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testHalf(self):
        testInput = ((1.6, 12.9), -pi)
        expected = (-1.6, -12.9)
        actual = challenge.rotatePoint(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

class TestRotateCircles(unittest.TestCase):
    def testSingle(self):
        testInput = ([(1, 0, 1)], pi / 2)
        expected = [(0, 1, 1)]
        actual = challenge.rotateCircles(*testInput)
        assertTuplesAlmostEqual(self, list(actual), expected)

    def testMultiple(self):
        testInput = ([(1.6, 12.9, 1000), (0, 0, 1)], -pi)
        expected = [(-1.6, -12.9, 1000), (0, 0, 1)]
        actual = challenge.rotateCircles(*testInput)
        assertTuplesAlmostEqual(self, list(actual), expected)

class TestCoTangent(unittest.TestCase):
    def testSameSize(self):
        testInput = ((0, 0, 1), (2, 1, 1))
        expected = (0.5, 1.118033988749895)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeSteep(self):
        testInput = ((0, 0, 1), (1, 2, 1))
        expected = (2, 2.2360679774997894)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeSlopingDown(self):
        testInput = ((0, 0, 1), (2, -1, 1))
        expected = (-0.5, 1.118033988749895)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeSlopingDownSteep(self):
        testInput = ((0, 0, 1), (1, -2, 1))
        expected = (-2, 2.23606797749979029)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeHorizontal(self):
        testInput = ((0, 0, 1), (1, 0, 1))
        expected = (0, 1)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeVertical(self):
        testInput = ((0, 0, 1), (0, 1, 1))
        expected = (INF, -1)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeReversedArguments(self):
        testInput = ((2, 1, 1), (0, 0, 1))
        expected = (0.5, -1.118033988749895)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeHorizontalReversed(self):
        testInput = ((1, 0, 1), (0, 0, 1))
        expected = (0, -1)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSameSizeVerticalReversed(self):
        testInput = ((0, 1, 1), (0, 0, 1))
        expected = (INF, 1)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testLargerSize(self):
        testInput = ((0, 0, 1), (12, 10, 3))
        expected = (1.0784561912118524, 1.4707371472711144)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testLargerSizeReversed(self):
        testInput = ((12, 10, 3), (0, 0, 1))
        expected = (0.6358295230738619, -1.1850228615568286)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testSmallerSize(self):
        testInput = ((0, 0, 1), (12, 10, 1 / 3))
        expected = (0.763438390645699, 1.2581089683774196)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

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
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testTouchingInnerReversed(self):
        testInput = ((0.5, 0, 0.5), (0, 0, 1))
        expected = (INF, 1)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testTouchingOuter(self):
        testInput = ((0, 0, 1), (1.5, 0, 0.5))
        expected = (-0.35355339059327373, 1.0606601717798212)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

    def testTouchingOuterReversed(self):
        testInput = ((1.5, 0, 0.5), (0, 0, 1))
        expected = (0.35355339059327373, -1.0606601717798212)
        points, actual = challenge.coTangent(*testInput)
        assertTupleAlmostEqual(self, actual, expected)

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
            assertTupleAlmostEqual(self, a[0], e[0])
            self.assertEqual(a[1], e[1])

    def testSimple(self):
        testInput = ((0, 0, 1), [(0, 0, 1), (3, 3, 1), (4, -1, 0.5)])
        expected = [((1.0, 1.414213562373095), (3, 3, 1)),
                    ((-0.38389448844241986, 1.0711559075393586), (4, -1, 0.5))]
        actual = challenge.intraTangents(*testInput)
        for a, e in zip(actual, expected):
            assertTupleAlmostEqual(self, a[0], e[0])
            self.assertEqual(a[1], e[1])


class TestConvexHullDisksHalf(unittest.TestCase):
    def testSimple(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.0, 1.414213562373095), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertTuplesAlmostEqual(self, actual, expected)

    def testSimpleBottom(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(0, -1)]
        actual = challenge.convexHullDisksHalf(testInput, bottom=True)
        assertTuplesAlmostEqual(self, actual, expected)

    def testStackedVertical(self):
        testInput = [(0, 0, 1), (0, 1, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(INF, -1), (0.6666666666666666, 2.201850425154663), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertTuplesAlmostEqual(self, actual, expected)

    def testStackedHorizontal(self):
        testInput = [(0, 0, 1), (2, 3, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.5, 1.8027756377319948), (0.0, 4.0), (-1, 7.414213562373094)]
        actual = challenge.convexHullDisksHalf(testInput)
        assertTuplesAlmostEqual(self, actual, expected)

class TestConvexHullDisks(unittest.TestCase):
    def testSingle(self):
        testInput = [(0, 0, 1)]
        with self.assertRaises(ValueError):
            challenge.convexHullDisks(testInput)

    def testEffectivelySingle(self):
        testInput = [(0, 0, 1), (0, 0, 0.1)]
        with self.assertRaises(ValueError):
            challenge.convexHullDisks(testInput)

    def testDoublePillar(self):
        testInput = [(0, 0, 1), (0, 10, 1)]
        with self.assertRaises(ValueError):
            challenge.convexHullDisks(testInput)
    """
    def testDoublePointyVertical(self):
        testInput = [(0, 0, 1), (0, 10, 0.5)]
        expected = [(19.974984355438178, 20.0), (-19.974984355438178, 20.0), (0.0, -1)]
        actual = challenge.convexHullDisks(testInput)
        assertTuplesAlmostEqual(self, actual, expected)
    """
    def testDoublePointyHorizontal(self):
        testInput = [(0, 0, 1), (10, 0, 0.5)]
        with self.assertRaises(ValueError):
            challenge.convexHullDisks(testInput)

    def testSimple(self):
        testInput = [(0, 0, 1), (3, 3, 1), (6, 0, 1)]
        expected = [(1.0, 1.414213562373095), (-1, 7.414213562373094), (0, -1)]
        actual = challenge.convexHullDisks(testInput)
        assertTuplesAlmostEqual(self, actual, expected)

    def testOverlapping(self):
        testInput = [(0, 0, 1), (10, 0, 1), (5, -10, 1), (5, -3, 1)]
        expected = [(0.0, 1.0), (2, -22.236067977499786), (-2.0, -2.23606797749979)]
        actual = challenge.convexHullDisks(testInput)
        assertTuplesAlmostEqual(self, actual, expected)

class BoundingBoxesDisks(unittest.TestCase):
    def testSingle(self):
        testInput = [(0, 0, 1), (10, 0, 1), (5, 2, 1)]
        expected = [(((0.82222433029643, -4.748143229308327),
                        (-1.299867367239363, 0.5570860145311558),
                        (9.17777566970357, 4.748143229308328),
                        (11.299867367239361, -0.5570860145311549)),
                        64.48010596547691),
                    (((-1.299867367239363, -0.5570860145311556),
                        (0.8222243302964303, 4.748143229308328),
                        (11.299867367239361, 0.5570860145311558),
                        (9.17777566970357, -4.748143229308328)),
                        64.48010596547691),
                    (((-1.0, -1.0),
                        (-1.0, 3.0),
                        (11.0, 3.0),
                        (11.0, -1.0)),
                        48.0)]
        actual = challenge.boundingBoxesDisks(testInput)
        for a, e in zip(actual, expected):
            assertTuplesAlmostEqual(self, a[0], e[0])
            self.assertAlmostEqual(a[1], e[1])

