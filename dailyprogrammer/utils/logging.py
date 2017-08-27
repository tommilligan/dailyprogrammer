#!/usr/bin/env python

import logging
import time

def moduleLogger(name):
    """
    Returns a logger for a module. Called as::

        logger = moduleLogger(__name__)

    :param string name: Module name to provie a logger for
    """
    newLogger = logging.getLogger(name)
    newLogger.setLevel(logging.DEBUG)
    return newLogger

logger = moduleLogger(__name__)

def objectLogger(o):
    """
    Returns a correctly named logger for an object. Called as::

        def __init__(self):
            self.logger = objectLogger(self)

    :param object o: Object to provie a logger for
    """
    name = o.__module__ + "." + o.__class__.__name__
    logger.debug("Generating object logger; '%s'", name)
    newLogger = logging.getLogger(name)
    newLogger.setLevel(logging.DEBUG)
    return newLogger


def timeit(callback):
    """
    Decorator to time a method in seconds.
    
    Passes a float value to a callback (normally a print or log function).

    :param function wrapped: Function to time
    :param function callback: Function to call with the timed value in seconds
    """
    def decorator(wrapped):
        def timed(*args, **kw):
            t0 = time.time()
            result = wrapped(*args, **kw)
            t1 = time.time()
            elapsed = t1 - t0

            callback(elapsed)
            return result

        return timed
    return decorator

