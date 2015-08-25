#coding: utf-8
from __future__  import generators, print_function, division, unicode_literals
from collections import deque
import pygame
from random import randrange
import sys
from pygame.locals import *


class Point(tuple): #TODO: its point
    """A tuple that supports some vector operations.

    >>> v, w = Point((1, 2)), Point((3, 4))
    >>> v + w, w - v, v * 10, 100 * v, -v
    ((4, 6), (2, 2), (10, 20), (100, 200), (-1, -2))
    """
    def __init__(self, seq, *args, **kwargs):
        if len(seq) != 2:
            raise TypeError('only 2 coordinate needed')
        self.x = seq[0]
        self.y = seq[1]
        return super(Point, self).__init__(seq, *args, **kwargs)

    def __add__(self, other): return Point([v + w for v, w in zip(self, other)])

    def __radd__(self, other): return Point([w + v for v, w in zip(self, other)])

    def __sub__(self, other): return Point([v - w for v, w in zip(self, other)])

    def __rsub__(self, other): return Point([w - v for v, w in zip(self, other)])

    def __mul__(self, s): return Point([v * s for v in self])

    def __rmul__(self, s): return Point([v * s for v in self])

    def __neg__(self): return  Point([-1 * v for v in self])


class Vector(Point):
    """A tuple that supports some vector operations.

    >>> v, w = Vector((1, 2)), Vector((3, 4))
    >>> v + w, w - v, v * 10, 100 * v, -v
    ((4, 6), (2, 2), (10, 20), (100, 200), (-1, -2))
    """
    def __init__(self, seq, *args, **kwargs):
        if len(seq) != 2:
            raise TypeError('only 2 point needed')
        for point in seq:
            if not isinstance(point, Point):
                raise TypeError('only Points supported')

        return super(Vector, self).__init__(seq, *args, **kwargs)


class Level(object):

    def __init__(self, world_size):
        self.world_vector = Vector((Point([0, 0]), world_size*Point([1, 1])))

        return super(Level, self).__init__()

    snake_points = (Point((2,2)), Point((2,3)), Point((2,4)) )

    aplles_points = (Point((3,3)), Point((1,2)), Point((3,6)) )

    block_points = (Point((4,4)), Point((4,5)), Point((4,6)), Point((4,3)))

    objects = {'snake':{'form':'@', 'points':snake_points}, 'aplles':{'form':'*', 'points':aplles_points}, 'blocks':{'form':'#', 'points':block_points},}

    def __init__(self, world_size):

        lev_render = LevelRender()
        world_vector = Vector((Point([0, 0]), world_size*Point([1, 1])))
        lev_render.draw_level(world_vector)

        for object in self.objects:
            obj = self.objects[object]
            for point in obj['points']:
                lev_render.draw_point(point, obj['form'])

        self.show_level = lev_render.show_level
        self.show_level()


class LevelRender(object):

    # def __init__(self, end_points, start_points=Vector()):
    #     self.level = self.draw_level()
    #     return super(Render, self).__init__()

    def draw_level(self, vector, form='~'):
        if not isinstance(vector, Point):
            raise TypeError('need vector')
        level = []
        for y in range(vector[0].y, vector[1].y):
            level.append(([form for x in range(vector[0].x, vector[1].x)]))
            #
            # print([1 if x== vector.x else 0 for x in range(vector.x)])
        self.level = level
        return level

    def draw_point(self, point, form='0'):
        if not isinstance(point, Point):
            raise TypeError('need point')
        try:
            self.level[point.y][point.x] = form
        except IndexError, err:
            print(str(err))
            return self.level
        return self.level

    def draw_text(self, position, text):#TODO: сделать обработчик на случай если текст не лезет
        if not isinstance(position, Point):
            raise TypeError('need point')
        start = position.x
        for letter in text:
            try:
                self.level[position.y][start] = letter
            except IndexError:
                break
            start +=1
        return self.level

    def show_level(self):
        for l in self.level:
            print(l)
        return self.level


level = Level(10)

class Engine(object):
    def __init__(self):
        #взять размер поля и размер ячейки поля - хотя вначале наверное есть смысл захардкодить
        #выбрать либу, выбрать рендер графики и рендер текста
        #приделать свой рендер
        pass

    def draw_level(self):
        pass
    """Draw game (while playing)."""
