#!/usr/bin/env python

import unittest

import dailyprogrammer.c20170811h0 as challenge

class TestMain(unittest.TestCase):
    def testEcho(self):
        expected = "spam"
        actual = challenge.main(expected)
        self.assertEqual(actual, expected)