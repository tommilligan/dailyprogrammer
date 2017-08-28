#!/usr/bin/env python

import unittest

import dailyprogrammer.__main__ as main

class TestMainParser(unittest.TestCase):
    def testParserCompiles(self):
        parser = main.mainParser()
