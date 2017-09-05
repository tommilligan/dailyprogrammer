#!/usr/bin/env python
"""
Installable dailyprogrammer package
"""

import argparse
import importlib
import logging
import sys

import dailyprogrammer.challenges
from dailyprogrammer.utils.inspection import listModules
from dailyprogrammer.utils.logging import moduleLogger, timeit

logger = moduleLogger(__name__)

def challengeTimer(elapsed):
    """
    Log the challenge duration

    :param float elapsed: In seconds
    """
    logger.warn("challenge ran in %0.3f s" % elapsed)

def mainParser():
    """
    Command line parser
    """
    parser = argparse.ArgumentParser("dailyprogrammer")
    parser.add_argument("-v", "--verbose", action="count", help="Turn logging")
    parser.add_argument("-l", "--list", action="store_true", help="List available challanges and exit")
    parser.add_argument("challenge", nargs="?", help="Challenge id. Matches the regex 'c\d{8}[hme]\d+' and style cYYYYMMDD<level><serial>")
    parser.add_argument("input", nargs="?", default=None, help="Challenge input. Defaults to stdin (one-read only)")
    return parser

def main():
    """
    Command line entry point
    """
    # Setup logging
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    ch.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s"))
    root = logging.getLogger()
    root.handlers = [ch]

    # Take cli arguments
    parser = mainParser()
    args = parser.parse_args()

    # Alter logging
    if args.verbose == 1:
        ch.setLevel(logging.INFO)
    elif args.verbose == 2:
        ch.setLevel(logging.DEBUG)

    logger.debug(args)

    # Listing challanges
    if args.list:
        for module, isPackage in listModules(dailyprogrammer.challenges):
            print(module)
    else:
        # Running challanges
        if args.input is None:
            challengeInput = sys.stdin.read()
        else:
            challengeInput = args.input
        
        challengeModule = "dailyprogrammer.challenges.{0}".format(args.challenge)
        challenge = importlib.import_module(challengeModule)

        result = timeit(challengeTimer)(challenge.main)(challengeInput)
        print(result)

if __name__ == "__main__":
    main()
