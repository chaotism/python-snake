# coding: utf-8
from __future__ import generators, print_function, division
import os
import curses
from game_source.graphics import Point


FORMS = {
    'food': '@',
    'block': '#',
    'snake': 'p',
}

class RenderException(Exception):
    pass

class LevelRender(object):
    def __init__(self, level):
        self.level_obj = level
        self.draw_level(self.level_obj)
        self.screen = curses.initscr()
        # curses.start_color()
        # curses.noecho()
        # curses.curs_set(False)
        self.screen.keypad(True)
        self.screen.nodelay(True)    # stops getch() from blocking the program

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

    def show_level(self):
         #TODO: сделать проверку размера игры и локации
         self.screen.redrawwin()
         self.screen.refresh()
         for y in xrange(self.level_obj[0].y, self.level_obj[1].y):
            for x in xrange(self.level_obj[0].x, self.level_obj[1].x):
                self.drawTile(x, y, self.level[y][x], curses.COLOR_RED)

    def drawTile(self, x, y, tile=' ', color=None):
        color = color or curses.COLOR_BLACK
        x = x * 2  + self.level_obj[1].x // 2
        y += self.level_obj[1].y // 2

        try:
            self.screen.addstr(y, x, tile, color)
        except curses.error, err:
            print(err)#TODO:Переделать через logger
            raise RenderException('need bigger console, use fullscreen mode')
