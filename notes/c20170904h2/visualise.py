#!/usr/bin/env python
"""
Generate visualisations for the main script
"""

from io import BytesIO
import sys

from PIL import Image, ImageDraw

import dailyprogrammer.challenges.c20170904e2 as challenge
from dailyprogrammer.utils.logging import moduleLogger

logger = moduleLogger(__name__)

INF = float('inf')

def getY(line, x):
    """
    Get a y coordinate for a line
    """
    m, c = line
    y = int((m * x) + c)
    return y

def main(circles):
    multiplier = 50
    im = Image.new("RGB", (10*multiplier, 10*multiplier), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    # Draw circles
    logger.warn("Drawing circles")
    for circle in circles:
        x, y, r = circle
        coords = [i * multiplier for i in (x-r, y-r, x+r, y+r)]
        draw.ellipse(coords, outline=(127, 127, 127))

    # Draw tangent lines
    logger.warn("Drawing tangent lines")
    hull = challenge.convexHullDisks(circles)
    for line in hull:
        m, c = line

        c = c * multiplier

        xs = [-im.width, im.width]
        if abs(m) != INF:
            points = list((x, getY((m, c), x)) for x in xs)
        else:
            points = list((c, y) for y in xs)

        draw.line(points, fill=(255, 0, 0), width=1)

    # Draw smallest box
    logger.warn("Drawing box")
    box = challenge.minimumBounding(circles)
    for i, point in enumerate(box):
        a = box[i]
        try:
            b = box[i+1]
        except IndexError:
            b = box[0]
        points = [a, b]
        points = list(tuple(p * multiplier for p in point) for point in points)
        draw.line(points, fill=(0, 0, 255), width=1)

    im = im.transpose(Image.FLIP_TOP_BOTTOM)

    # write to stdout
    imagefile = BytesIO()
    im.save(imagefile, "PNG")
    imagedata = imagefile.getvalue()
    sys.stdout.buffer.write(imagedata)

if __name__ == "__main__":
    circles = [(3, 3, 1), (3, 6, 1), (4, 7, 1.5), (8, 6, 0.5), (7, 5, 0.75), (5, 4.5, 2), (5.5, 3.5, 0.125)]
    main(circles)

