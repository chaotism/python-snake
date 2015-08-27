# coding: utf-8
from __future__ import generators, print_function, division
import importlib

import sys
import time

from level import Level
from snake import Snake
from graphics import Point
from controls import Controller
from settings import CONTROLLER, SNAKE_START_LENGTH, GROWTH_PENDING, SEGMENT_SCORE, WORLD_SIZE, TIME_DELTA


class GameOver(Exception):
    pass


class Engine(object):

    def __init__(self, world_size=WORLD_SIZE):
        self.world_center = Point((world_size // 2, world_size // 2))
        self.world_size = world_size
        self.snake = Snake(start=self.world_center, start_length=SNAKE_START_LENGTH, growth_pending = GROWTH_PENDING)
        self.level = Level(size=self.world_size, snake=self.snake)
        self.score = 0
        self.controller = Controller(self.level.level_render)

    def reset(self):
        """Start a new game."""
        self.playing = True
        self.score = 0
        self.snake = Snake(start=self.world_center,
                           start_length=SNAKE_START_LENGTH)
        self.level = Level(size=self.world_size, snake=self.snake)
        self.play()

    def update(self, dt):
        """Update the game by dt seconds."""

        self.check_input()
        # time.sleep(dt)
        if self.snake.update():
            self.level.update_level()  # todo: переделать через перерисовку уровня
            self.level.level_render.draw_text(
                Point((0, 0)), 'Score {}'.format(self.score))
            self.level.show_level()
            head = self.snake.get_head()
            # If snake hits a food block, then consume the food, add new
            # food and grow the snake.
            if head in self.level.food:
                self.level.food.remove(head)
                self.snake.grow()
                self.score += len(self.snake) * SEGMENT_SCORE

            if self.snake.self_intersecting() or head in self.level.blocks:
                self.playing = False
                raise GameOver(self.score)
        time.sleep(dt)

    def play(self):
        """Play game until the QUIT event is received."""
        while True:
            try:
                self.update(TIME_DELTA)
            except GameOver, err:
                print('You score {}'.format(str(err)))
                time.sleep(3)
                self.reset()

    def check_input(self):
        """Process keyboard event e."""
        direction = self.controller.update()
        if direction:
            self.snake.change_direction(direction)
            #raise Exception(self.snake.direction)
