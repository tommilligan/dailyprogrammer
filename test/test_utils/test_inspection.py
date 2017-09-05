#!/usr/bin/env python

import unittest

import dailyprogrammer.utils.inspection as inspection

class TestListModules(unittest.TestCase):
    def testUnittest(self):
        testInput = unittest
        actual = inspection.listModules(unittest)
        self.assertTrue(("mock", False) in actual)
        self.assertFalse(("spam", True) in actual)
