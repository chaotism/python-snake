# coding: utf-8
from __future__ import generators, print_function, division
import os
from collections import deque

from subprocess import Popen, PIPE


class Point(deque):
    """A deque that supports some vector operations.

    >>> v, w = Point((1, 2)), Point((3, 4))
    >>> v + w, w - v, v * 10, 100 * v, -v
    ((4, 6), (2, 2), (10, 20), (100, 200), (-1, -2))
    """

    def __init__(self, seq, *args, **kwargs):
        if len(seq) != 2:
            raise TypeError('only 2 coordinate needed')
        self.x = seq[0] #TODO: сделать обратную зависимость
        self.y = seq[1]
        return super(Point, self).__init__(seq, *args, **kwargs)

    def __add__(self, other): return Point([v + w for v, w in zip(self, other)])

    def __radd__(self, other): return Point([w + v for v, w in zip(self, other)])

    def __sub__(self, other): return Point([v - w for v, w in zip(self, other)])

    def __rsub__(self, other): return Point([w - v for v, w in zip(self, other)])

    def __mul__(self, s): return Point([v * s for v in self])

    def __rmul__(self, s): return Point([v * s for v in self])

    def __neg__(self): return Point([-1 * v for v in self])


class Vector(Point):
    def __init__(self, seq, *args, **kwargs):
        if len(seq) != 2:
            raise TypeError('only 2 point needed')
        for point in seq:
            if not isinstance(point, Point):
                raise TypeError('only Points supported')

        return super(Vector, self).__init__(seq, *args, **kwargs)


class Blocks(deque):
    """
    deque with basic level block
    """

    def __init__(self, seq, form='block', eatable=False):
        for point in seq:
            if not isinstance(point, Point):
                raise TypeError('only Points supported')
        self.form = form
        self.eatable = eatable

        return super(Blocks, self).__init__(seq)

    def __add__(self, other):
        return self.__iadd__(other)


DIRECTION_UP = Point((0, -1))
DIRECTION_DOWN = Point((0, 1))
DIRECTION_LEFT = Point((-1, 0))
DIRECTION_RIGHT = Point((1, 0))
DIRECTION_DR = DIRECTION_DOWN + DIRECTION_RIGHT
