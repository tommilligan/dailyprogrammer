#!/usr/bin/env python

import logging
import time
import unittest

import dailyprogrammer.utils.logging as dp_logging

class Example(object):
    pass

class TestModuleLogger(unittest.TestCase):
    def testDefault(self):
        name = "spam"
        logger = dp_logging.moduleLogger(name)
        self.assertEqual(logger.name, name)
        self.assertEqual(logger.level, logging.DEBUG)

class TestObjectLogger(unittest.TestCase):
    def testDefault(self):
        example = Example()
        logger = dp_logging.objectLogger(example)
        self.assertEqual(logger.name, "test_utils.test_logging.Example")
        self.assertEqual(logger.level, logging.DEBUG)

class TestTimeit(unittest.TestCase):
    def testSleepy(self):
        sleepDuration = 0.25

        @dp_logging.timeit(lambda actual: self.assertTrue(sleepDuration - actual < 0.01))
        def sleepy():
            time.sleep(sleepDuration)
        
        sleepy()

