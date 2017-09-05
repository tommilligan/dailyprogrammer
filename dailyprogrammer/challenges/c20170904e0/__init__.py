#!/usr/bin/env python
"""
[2017-09-04] Challenge #330 [Easy] Surround the circles
https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/
"""

from dailyprogrammer.utils.logging import moduleLogger, objectLogger

logger = moduleLogger(__name__)

def minimumBoundingOrthogonal(circles):
    """
    Returns the minimum bounding box (axis-aligned) in the format::

        ((x0, y0), (x1, y1), (x2, y2), (x3, y3))

    Where the tuples are x, y coordinates from the bottom-left point clockwise

    :param list circles: A list of circle 3-tuples (x, y, r)
    :rtype: tuple
    """
    extrema = [(x - r, x + r, y - r, y + r) for x, y, r in circles]
    xmins, xmaxs, ymins, ymaxs = zip(*extrema)
    xmin, xmax, ymin, ymax = (min(xmins), max(xmaxs), min(ymins), max(ymaxs))
    return ((xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin))

def main(challengeInput):
    circles = [(float(s) for s in l.split(",")) for l in challengeInput.split("\n")]
    points = minimumBoundingOrthogonal(circles)
    challengeOutput = ", ".join("({0:.3f}, {1:.3f})".format(*point) for point in points)
    return challengeOutput

