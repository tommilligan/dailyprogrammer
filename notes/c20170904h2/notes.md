# [2017-09-04] Challenge #330 [Easy] Surround the circles

https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/

### TL;DR

Given a list of circles, find the smallest enclosing rectangle.

Approach:

* Find the convex hull of the set
    * For the upper/lower
        * Find the left/rightmost circle to start with
        * Find all left-handed cotangents between other circles (defined as the tangent vector having an acute anti-clockwise angle to the vector between the two circles)
        * Find the tangent with the most positive gradient (but less than the previous one)
        * Add this tangent to the hull
        * Loop with the newly found circle
* For each line in the hull
    * Rotate all circles by the line gradient
    * Find the bounding box by usual method
    * Find the area
    * Rotate the corner points back by the same gradient
* Pick the box with the smallest area

## Visualisation

```bash
python notes/c20170904h2/visualise.py > visualise.png
```

## Input

Each circle on a line in `x,y,r` format

## Output

List of bounding box points in `(x, y)` format:

`bottom-left, top-left, top-right, bottom-right"`

## References

* [A convex hull algorithm for discs, and applications (Rappaport D, 1992)](http://www.sciencedirect.com/science/article/pii/092577219290015K)
* [Solving Geometric Problems with the Rotating Calipers (Toussaint G, 1983)](https://www.cs.swarthmore.edu/~adanner/cs97/s08/pdf/calipers.pdf)

