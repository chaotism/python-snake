# coding: utf-8
from __future__ import generators, print_function, division

import math

import random
import copy
from graphics import Point, Vector, Blocks
from settings import RENDER
import importlib

try:
    render_module = importlib.import_module(RENDER)
    LevelRender = getattr(render_module, 'LevelRender')
except ImportError, AttributeError:
    from adapters.default.render import LevelRender


class Level(object):

    snake = Blocks((), form='snake', eatable=False)
    food = Blocks((), form='food', eatable=True)
    blocks = Blocks((), form='block', eatable=False)

    def __init__(self, size, snake=None, food=None, blocks=None):
        self.snake = snake or None
        self.food_count = food or size//2
        self.blocks_count = blocks or size//2
        self.objects = (self.snake, self.food, self.blocks)
        self.world_size = size
        self.world_vector = Vector((Point([0, 0]), size * Point([1, 1])))
        self.level_render = LevelRender(self.world_vector)
        self.update_level()

    def update_level(self):
        """Draw game (while playing)."""
        self.snake.bound(self.world_size)
        self.level_render.draw_level(self.world_vector)
        if not self.food:
            self.seed_food()

        if not self.blocks:
            self.seed_blocks()

        for object in self.objects:
            for point in object:
                self.level_render.draw_point(point, object.form)
        # if self.snake.update():
        #     return True

    def create_block(self):
        random.seed()
        x = random.choice(xrange(self.world_size))
        y = random.choice(xrange(self.world_size))
        block = Point((x, y))
        for obj in self.objects:
            if block in obj:
                return
        return block

    def seed_food(self, num=None):
        num = num or self.food_count
        for x in xrange(0, num):
            meal = self.create_block()
            if meal:
                self.food.append(meal)

    def seed_blocks(self, num=None):
        num = num or self.blocks_count
        for x in xrange(0, num):
            block = self.create_block()
            if block:
                self.blocks.append(block)

    def show_level(self):
        self.level_render.show_level()
