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

def coTangent(p, q, anticlockwise=False):
    """
    Calculate the cotangent that sits to the left of the line p -> q

          /O q
         /
        /o   p

    If anticlockwise is ``True``, the mirroring tangent is found.

    :param tuple p: A 3-tuple representing the circle (x, y, r)
    :param tuple q: As p
    :rtype: 2-tuple representing line (m, c)
    """
    logger.debug("Calculating cotangent of circles; %s, %s", p, q)

    px, py, pr = p
    qx, qy, qr = q

    dx, dy, dr = (i[1] - i[0] for i in zip(p, q))

    lowerHull = (dx < 0.0) or (dx == 0.0 and dy < 0.0)
    # only mirror if XOR we are bottom hull or asking for anticlockwise outer tangents
    shouldMirror = lowerHull != anticlockwise
    if shouldMirror:
        mirror = -1
    else:
        mirror = 1
    logger.debug("cotangent choice; lowerHull {0}, anticlockwise {1}, shouldMirror {2}".format(lowerHull, anticlockwise, shouldMirror))

    l = sqrt(dx**2 + dy**2)
    if l == 0.0:
        raise GeometryException("Circles with the same center cannot have co-tangents")

    # phi is the angle at which the circle centres are aligned
    try:
        phi = atan(dy / dx)
    # If the circles are stacked horizontally, take leftmost tangent if q above p
    except ZeroDivisionError:
        phi = pi / 2
    
    # theta is the angle of the tangent compared to phi
    try:
        theta = asin(dr / l)
    # If there was a ValueError, |dr / l| was > 1, therefore circle areas subset
    except ValueError:
        raise GeometryException("One circle cannot be fully contained by the other")

    psi = (mirror * phi) + theta

    logger.debug("co-tanget constuction; phi %.3f, theta %.3f, psi %.3f", phi, theta, psi)

    tp = (px - (sin(psi) * pr),
          py + (cos(psi) * pr * mirror))
    tq = (qx - (sin(psi) * qr),
          qy + (cos(psi) * qr * mirror))

    for point in (tp, tq):
        logger.debug("Calculated tangent point; (%.3f, %.3f)", *point)
    tangent = line(tp, tq)
    return tangent

def findStartingCircle(circles, bottom=False):
    """
    Return the circle we should start at (leftmost edge of the list, rightmost for bottom)

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    logger.debug("Finding circle to start from")
    # Array of (xmin, circle) tuples (or (xmax, circle) tuple if bottom)
    if bottom:
        extremeCircles = [(c[0] + c[2], c) for c in circles]
        extremeEdge = max([k for k, c in extremeCircles])
    else:
        extremeCircles = [(c[0] - c[2], c) for c in circles]
        extremeEdge = min([k for k, c in extremeCircles])
    
    logger.debug("%s edge is %.3f", "Leftmost" if bottom else "Rightmost", extremeEdge)

    extremeCircles = [i for i in extremeCircles if i[0] == extremeEdge]
    extremeCircles = sorted(extremeCircles, key=lambda i: i[1][1], reverse=bottom)
    circle = extremeCircles[0][1]
    logger.debug("Starting circle is %s", circle)
    return circle

def intraTangents(startingCircle, circles, bottom=False):
    """
    Return all valid tangents from ``startingCircle`` to ``circles``

    Suppress geometric errors encountered during finding co-tangents

    Returns (tangent, circle), where tangent is a line of the form (m, c)
    and circle is the circle (x, y, r) the tangent was found to.

    :param startingCircle: Circle to use in each co-tangent pair
    :param circles: Other circles
    :rtype: 2-tuple of (tangent, circle)
    """
    for c in circles:
        try:
            tangent = coTangent(startingCircle, c, bottom=bottom)
            yield (tangent, c)
        except GeometryException as e:
            logger.warn("Could not form tangent from %s to %s; %s", startingCircle, c, e)

def convexHullDisksHalf(circles, bottom=False):
    """
    Returns a set of lines describing half a convex hull of the disk set.

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    logger.debug("Finding convex half-hull")

    # Ensure iterators are fulfiled, persist to memory
    circles = list(circles)

    currentCircle = findStartingCircle(circles, bottom=bottom)
    hullLines = []
    while True:
        validTangents = intraTangents(currentCircle, circles, bottom=bottom)

        # Filter out all tangents that have more positive gradient
        # than the last tangent (i.e. would make hull concave)
        if hullLines:
            previousGradient = hullLines[-1][0]
            logger.debug("The previous gradient was %.3f", previousGradient)
            validTangents = [vT for vT in validTangents if vT[0][0] < previousGradient]

        # Reverse sort tangents by gradient
        validTangents = sorted(validTangents, reverse=True, key=lambda validTangent: validTangent[0][0])
        if validTangents:
            nextHullLine, nextCircle = validTangents[0]
            logger.debug("Next hull line is %s to circle %s", nextHullLine, nextCircle)
            hullLines.append(nextHullLine)
            currentCircle = nextCircle
        else:
            logger.debug("No remaining valid tangents, hull section complete")
            break
    return hullLines 

def convexHullDisks(circles):
    """
    Returns a set of lines describing the convex hull of the disk set.

    :param list circles: A list of circle 3-tuples (x, y, r)
    """
    logger.debug("Finding convex hull")

    # Ensure iterators are fulfiled, persist to memory
    circles = list(circles)

    hullLines = convexHullDisksHalf(circles)
    hullLines.extend(convexHullDisksHalf(circles, bottom=True))

    return hullLines

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

