#!/usr/bin/env python
"""
[2017-09-04] Challenge #330 [Easy] Surround the circles
https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/

Self challenge
--------------
Find the smallest possible bounding box for a given set of circles

Method:

* Form a convex hull from a given set of circles (Rappaport D, A convex hull algorithm for disks)
* Try a bounding box against each flat arc
* Determine the smallest bounding bx by area

In this module:

* a line is represented as a (rho, theta) tuple
* a circular arc is represented as a circle-sector (x, y, r, start, end)
* 

"""

from math import sqrt, atan, asin, sin, cos, pi

from dailyprogrammer.utils.logging import moduleLogger, objectLogger

logger = moduleLogger(__name__)

INF = float('inf')

def coTangent(p, q, bottom=False):
    """
    Calculate the upper (edge-case, left) cotangent of two circles ``p`` and ``q``::

          /O q
         /
        /o   p

    If bottom is ``True``, the mirroring tangent on the bottom is found.

    :param tuple p: A 3-tuple representing the circle (x, y, r)
    :param tuple q: As p
    :rtype: 2-tuple representing line (m, c)
    """
    px, py, pr = p
    qx, qy, qr = q

    dx, dy, dr = (i[1] - i[0] for i in zip(p, q))

    l = sqrt(dx**2 + dy**2)

    try:
        phi = atan(dy / dx)
    # If the circles are stacked horizontally, take leftmost tangent
    except ZeroDivisionError:
        phi = pi / 2
    theta = asin(dr / l)

    psi = phi + theta

    tp = (px - (sin(psi) * pr),
          py + (cos(psi) * pr))
    tq = (qx - (sin(psi) * qr),
          qy + (cos(psi) * qr))

    logger.debug("Calculated tangent points; %s, %s", tp, tq)

    tdx, tdy = (i[1] - i[0] for i in zip(tp, tq))
    try:
        tm = (tdy / tdx)
        tc = tp[1] - (tm * tp[0])
    except ZeroDivisionError:
        tm = INF
        tc = tp[0]
    tangent = (tm, tc)
    return tangent


def alpha(L1, L2):
    """
    Returns the positive angle swept clockwise from L1 to L2
    """
    pass

def mergeHulls(hullP, hullQ):
    """
    Returns a set of arcs describing the convex hull of two convex hulls
    """
    return hullP

def convexHullDiskPair(circleP, circleQ):
    """
    Returns a set of arcs describing the convex hull of the disk pair.

    Curved sections are converted to a series of flat ars parallel to each opposing face.

    :param tuple circleP: A circle 3-tuple (x, y, r)
    :param tuple circleQ: A circle 3-tuple (x, y, r)
    """
    return circleP

def convexHullDisks(circles):
    """
    Returns a set of arcs describing the convex hull of the disk set.

    Curved sections are converted to a series of flat ars parallel to each opposing face.

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    circles = list(circles)
    lenCircles = len(circles)
    if lenCircles > 2:
        midIndex = int(lenCircles / 2)
        setP = circles[:midIndex]
        setQ = circles[midIndex:]
        hull = mergeHulls(convexHullDisks(setP),
                          convexHullDisks(setQ))
    elif lenCircles == 2:
        convexHullDiskPair(*circles)
    else:
        hull = circles[0]


def minimumBounding(circles):
    """
    Returns the minimum bounding box in the format::

        ((x0, y0), (x1, y1), (x2, y2), (x3, y3))

    Where the tuples are x, y coordinates from the leftmost point clockwise

    :param list circles: A list of circle 3-tuples (x, y, r)
    :rtype: tuple
    """
    extrema = [(x - r, x + r, y - r, y + r) for x, y, r in circles]
    xmins, xmaxs, ymins, ymaxs = zip(*extrema)
    xmin, xmax, ymin, ymax = (min(xmins), max(xmaxs), min(ymins), max(ymaxs))
    return ((xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin))

def main(challengeInput):
    circles = [(float(s) for s in l.split(",")) for l in challengeInput.split("\n")]
    points = minimumBounding(circles)
    challengeOutput = ", ".join("({0:.3f}, {1:.3f})".format(*point) for point in points)
    return challengeOutput

