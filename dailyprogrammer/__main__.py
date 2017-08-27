#!/usr/bin/env python
"""
Installable dailyprogrammer package
"""

import argparse
import importlib
import logging
import sys

def mainParser():
    """
    Command line parser
    """
    parser = argparse.ArgumentParser("dailyprogrammer working solutions")
    parser.add_argument("challenge", help="Challenge id. Matches the regex 'c\d{8}[hme]\d+' and style cYYYYMMDD<level><serial>")
    parser.add_argument("input", nargs="?", default=None, help="Challenge input. Defaults to stdin")
    return parser

def main():
    """
    Command line entry point
    """
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s"))
    root = logging.getLogger()
    root.handlers = [ch]

    parser = mainParser()
    args = parser.parse_args()

    if args.input is None:
        challengeInput = sys.stdin.read()
    else:
        challengeInput = args.input
    
    challengeModule = "dailyprogrammer.{0}".format(args.challenge)
    challenge = importlib.import_module(challengeModule)

    result = challenge.main(challengeInput)
    print(result)

if __name__ == "__main__":
    main()
