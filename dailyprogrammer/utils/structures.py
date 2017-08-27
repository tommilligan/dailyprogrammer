#!/usr/bin/env python

from dailyprogrammer.utils.logging import moduleLogger

logger = moduleLogger(__name__)

def sortedDictValues(inputDict, reverse=False):
    """
    Returns the given dictionary as a list of keys sorted deterministically by value then key::

        {"spam": 0, "eggs": 1, "ham": 1} => ["spam", "eggs", "ham"]

    :param dict inputDict:
    :param bool reverse: Reversed sorting
    :rtype: list
    """
    sortedDict = sorted(inputDict.items(), key=lambda item: (item[1], item[0]), reverse=reverse)
    values = [k for k, v in sortedDict]
    return values

