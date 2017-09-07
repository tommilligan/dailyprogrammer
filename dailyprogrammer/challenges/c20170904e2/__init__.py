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

class GeometryException(Exception):
    pass

def line(a, b):
    """
    Return a line 2-tuple (m, c) from the input points (x, y)

    :param tuple a: A 2-tuple point (x, y)
    :param tuple b: As above
    """
    logger.debug("Calculating line from points")
    dx, dy = (i[1] - i[0] for i in zip(a, b))
    try:
        m = (dy / dx)
        c = a[1] - (m * a[0])
    except ZeroDivisionError:
        m = INF
        c = a[0]
    line = (m, c)
    logger.debug("Calculated line; y = %.3fx + %.3f", m, c)
    return line

def coTangent(p, q, bottom=False):
    """
    Calculate the upper (edge-case, left) cotangent of two circles ``p`` and ``q``::

          /O q
         /
        /o   p

    If bottom is ``True``, the mirroring tangent on the bottom(right) is found.

    :param tuple p: A 3-tuple representing the circle (x, y, r)
    :param tuple q: As p
    :rtype: 2-tuple representing line (m, c)
    """
    logger.debug("Calculating cotangent of circles")

    if bottom:
        mirror = -1
    else:
        mirror = 1

    px, py, pr = p
    qx, qy, qr = q

    dx, dy, dr = (i[1] - i[0] for i in zip(p, q))

    l = sqrt(dx**2 + dy**2)
    if l == 0.0:
        raise GeometryException("Circles with the same center cannot have co-tangents")

    # phi is the angle at which the circle centres are aligned
    try:
        phi = atan(dy / dx)
    # If the circles are stacked horizontally, take leftmost tangent
    except ZeroDivisionError:
        phi = pi / 2
    
    # theta is the angle of the tangent compared to phi
    try:
        theta = asin(dr / l)
    # If there was a ValueError, |dr / l| was > 1, therefore circle areas subset
    except ValueError:
        raise GeometryException("One circle cannot be fully contained by the other")

    psi = phi + (mirror * theta)

    logger.debug("co-tanget constuction; phi %.3f, theta %.3f, psi %.3f", phi, theta, psi)

    tp = (px - (sin(psi) * pr * mirror),
          py + (cos(psi) * pr * mirror))
    tq = (qx - (sin(psi) * qr * mirror),
          qy + (cos(psi) * qr * mirror))

    for point in (tp, tq):
        logger.debug("Calculated tangent point; (%.3f, %.3f)", *point)
    tangent = line(tp, tq)
    return tangent

def findStartingCircle(circles):
    """
    Return the circle we should start at (leftmost edge of the list)

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    logger.debug("Finding circle to start from")
    # Array of (xmin, circle) tuples
    leftmostCircles = [(c[0] - c[2], c) for c in circles]
    leftmostEdge = min([k for k, c in leftmostCircles])
    logger.debug("Leftmost edge is %.3f", leftmostEdge)

    leftmostCircles = [i for i in leftmostCircles if i[0] == leftmostEdge]
    leftmostCircles = sorted(leftmostCircles, key=lambda i: i[1][1])
    circle = leftmostCircles[0][1]
    return circle

def intraTangents(startingCircle, circles):
    """
    Return all valid tangents from ``startingCircle`` to ``circles``

    Suppress geometric errors encountered during finding co-tangents

    :param startingCircle: Circle to use in each co-tangent pair
    :param circles: Other circles
    """
    for c in circles:
        try:
            tangent = coTangent(startingCircle, c)
            yield (tangent, c)
        except GeometryException as e:
            logger.warn("Could not form tangent from %s to %s; %s", startingCircle, c, e)

def convexHullDisks(circles):
    """
    Returns a set of lines describing the convex hull of the disk set..

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    # Ensure iterators are fulfiled, persist to memory
    circles = list(circles)

    startingCircle = findStartingCircle(circles)
    tangents = intraTangents(startingCircle, circles)
    tangents = list(tangents)
    return None 


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

