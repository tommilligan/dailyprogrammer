#!/usr/bin/env python
"""
Installable dailyprogrammer package
"""

import argparse
import importlib
import logging
import sys
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def mainParser():
    """
    Command line parser
    """
    parser = argparse.ArgumentParser("dailyprogrammer working solutions")
    parser.add_argument("-v", "--verbose", action="count", help="Turn logging")
    parser.add_argument("challenge", help="Challenge id. Matches the regex 'c\d{8}[hme]\d+' and style cYYYYMMDD<level><serial>")
    parser.add_argument("input", nargs="?", default=None, help="Challenge input. Defaults to stdin")
    return parser

def main():
    """
    Command line entry point
    """
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    ch.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s"))
    root = logging.getLogger()
    root.handlers = [ch]

    parser = mainParser()
    args = parser.parse_args()

    if args.verbose == 1:
        ch.setLevel(logging.INFO)
    elif args.verbose == 2:
        ch.setLevel(logging.DEBUG)

    logger.debug(args)

    if args.input is None:
        challengeInput = sys.stdin.read()
    else:
        challengeInput = args.input
    
    challengeModule = "dailyprogrammer.challenges.{0}".format(args.challenge)
    challenge = importlib.import_module(challengeModule)

    t0 = time.time()
    result = challenge.main(challengeInput)
    t1 = time.time()
    elapsed = t1 - t0
    logger.warn("challenge ran in %0.3f s" % elapsed)

    print(result)

if __name__ == "__main__":
    main()
