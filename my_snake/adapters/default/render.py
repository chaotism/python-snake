# coding: utf-8
from __future__ import generators, print_function, division
import os
from game_source.graphics import Point


FORMS = {
    'food': '@',
    'block': '#',
    'snake': 'p',
}


class LevelRender(object):

    def __init__(self, level):
        self.level_obj = level
        self.draw_level(self.level_obj)

    def draw_level(self, vector, form=' '):
        if not isinstance(vector, Point):
            raise TypeError('need vector')
        level = []
        for y in xrange(vector[0].y, vector[1].y):
            level.append(([form for x in xrange(vector[0].x, vector[1].x)]))
        self.level = level
        return self.level

    def draw_point(self, point, form='block'):
        if not isinstance(point, Point):
            raise TypeError('need point')
        try:
            self.level[point.y][point.x] = FORMS[form]
        except IndexError, err:
            print(str(err))  # TODO: переделать через logger
            return self.level
        return self.level

    # TODO: сделать обработчик на случай если текст не лезет
    def draw_text(self, position, text):
        if not isinstance(position, Point):
            raise TypeError('need point')
        start = position.x
        for letter in text:
            try:
                self.level[position.y][start] = letter
            except IndexError:
                break
            start += 1
        return self.level

    def show_level(self):
        os.system('clear')
        for l in self.level:
            print(l)  # TODO: переделать через logger
        return self.level
