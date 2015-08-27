# coding: utf-8
from __future__ import generators, print_function, division
import os
import pygame
from pygame.locals import Rect
from game_source.graphics import Point, Vector, DIRECTION_DR


BLOCK_SIZE = 33

BACKGROUND_COLOR = 45, 45, 45
SNAKE_COLOR = 0, 0, 255
FOOD_COLOR = 0, 255, 0
BLOCK_COLOR = 255, 0, 255
TEXT_COLOR = 255, 255, 255

FORMS = {
    'food': '@',
    'block': '#',
    'snake': 'p',
}

COLORS = {
    '@': FOOD_COLOR,
    '#': BLOCK_COLOR,
    'p': SNAKE_COLOR,
    '~': BACKGROUND_COLOR
}



class RenderException(Exception):
    pass


class LevelRender(object):

    def __init__(self, level, block_size=BLOCK_SIZE):
        self.level_obj = level
        self.draw_level(self.level_obj)
        pygame.init()
        pygame.display.set_caption('PyGame Snake')
        self.block_size = block_size
        self.window = pygame.display.set_mode(level[1] * self.block_size)
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font('freesansbold.ttf', self.block_size)
        self.world = Rect((0, 0), (11,11)) # вынести в графику
        self.clock = pygame.time.Clock()

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

    def draw_text(self, position, text):
        if not isinstance(position, Point):
            raise TypeError('need point')
        self.level[position.y][position.x] = text
        return self.level

    def render_text(self, position, text):
        position = position * self.block_size
        """Draw text at position p."""
        self.screen.blit(self.font.render(text, 1, TEXT_COLOR), position)

    def render_block(self, point):
        """Return the screen rectangle corresponding to the position p."""
        return Rect(point * self.block_size, DIRECTION_DR * self.block_size)

    def show_level(self):
        self.screen.fill(BACKGROUND_COLOR)
        texts = []
        for y in xrange(self.level_obj[0].y, self.level_obj[1].y):
            for x in xrange(self.level_obj[0].x, self.level_obj[1].x):
                color = COLORS.get(self.level[y][x], None)
                if color:
                    pygame.draw.rect(self.screen, color, self.render_block(Point((x,y))))
                else:
                    texts.append(Point((x,y)))
        for text in texts:
            self.render_text(text, self.level[text.y][text.x])
        pygame.display.flip()

    def render_block(self, point):
        return Rect(point * self.block_size, DIRECTION_DR * self.block_size)