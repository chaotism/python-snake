# coding: utf-8
from __future__ import generators, print_function, division
import os
import curses
# from curses import (
#                     panel, initscr, start_color, init_pair, color_pair, curs_set, noecho,
#                     doupdate, napms, endwin, newwin,
#                     KEY_RIGHT,KEY_LEFT, KEY_DOWN, KEY_UP,
#                     COLOR_BLACK, COLOR_RED, COLOR_GREEN
#                     )

from game_source.graphics import Point


FORMS = {
    'food': '@',
    'block': '#',
    'snake': 'p',
}

import curses

# def init():
#     global screen
#
#     screen = curses.initscr()
#     curses.noecho()
#     curses.cbreak()
#     curses.curs_set(0)
#     curses.start_color()
#     screen.nodelay(1)
#
# init()
#
# raise Exception
#screen.addstr(y, x, tile, color)

class LevelRender(object):
    def __init__(self, level):
        self.level_obj = level
        self.draw_level(self.level_obj)
        # self.screen = curses.initscr()
        # curses.noecho()
        # curses.cbreak()
        # curses.curs_set(0)
        # curses.start_color()
        # self.screen.nodelay(1)

    def draw_level(self, vector, form='~'):
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

    def draw_text(self, position, text):  # TODO: сделать обработчик на случай если текст не лезет
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

    # def show_level(self):
    #
    #     os.system('clear')
    #     for l in self.level:
    #         print(l)  # TODO: переделать через logger
    #     return self.level

    def show_level(self):
         self.screen = curses.initscr()
         for y in xrange(self.level_obj[0].y, self.level_obj[1].y):
            for x in xrange(self.level_obj[0].x, self.level_obj[1].x):
                self.drawTile(x, y, self.level[y][x], curses.COLOR_RED)

    def drawTile(self, x, y, tile=' ', color=None):
        color = color or curses.COLOR_BLACK
        x = x * 2  + self.level_obj[1].x // 2
        y += self.level_obj[1].y // 2

        self.screen.addstr(y, x, tile, color)
