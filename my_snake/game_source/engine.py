#coding: utf-8
from __future__  import generators, print_function, division
from collections import deque
import pygame
from random import randrange
import sys
import time
from pygame.locals import *
from level import Level
from snake import Snake, TIME_DELTA
from graphics import Point
from controls import KEY_DIRECTION


SNAKE_START_LENGTH = 2
SEGMENT_SCORE = 50

class GameOver(Exception):
    pass

class Engine(object):
    def __init__(self, world_size=10):
        self.world_center = Point((world_size//2, world_size//2))
        self.world_size = world_size
        self.snake = Snake(start=self.world_center, start_length=2)
        self.level = Level(size=self.world_size, snake=self.snake)
        self.score = 0
        #взять размер поля и размер ячейки поля - хотя вначале наверное есть смысл захардкодить
        #выбрать либу, выбрать рендер графики и рендер текста
        #приделать свой рендер
        pass

    def draw_level(self):
        pass
    """Draw game (while playing)."""

    def reset(self):
        """Start a new game."""
        self.playing = True
        self.level.update_level()
        self.score = 0
        self.snake = Snake(start=self.world_center, start_length=SNAKE_START_LENGTH)
        self.level = Level(size=self.world_size, snake=self.snake)

    def update(self, dt):
        """Update the game by dt seconds."""
        time.sleep(dt)
        if self.level.snake.update():
            self.level.update_level()
            self.level.level_render.draw_text(Point((0,0)), 'Score {}'.format(self.score))
            self.level.show_level()
            head = self.level.snake.get_head()
            # If snake hits a food block, then consume the food, add new
            # food and grow the snake.
            if head in self.level.food:
                self.level.food.remove(head)
                self.snake.grow()
                self.score += len(self.snake) * SEGMENT_SCORE

            if self.snake.self_intersecting() or head in self.level.blocks:
                self.playing = False
                raise GameOver(self.score)

    def play(self):
        """Play game until the QUIT event is received."""
        while True:
            try:
                self.update(TIME_DELTA)
            except GameOver, err:
                print('You score {}'.format(str(err)))
                break

    # def draw_text(self, text, p):
    #     """Draw text at position p."""
    #     self.screen.blit(self.font.render(text, 1, TEXT_COLOR), p)
    #
    # def input(self, e):
    #     """Process keyboard event e."""
    #     if e.key in KEY_DIRECTION:
    #         self.level.snake.change_direction(KEY_DIRECTION[e.key])
    #     elif e.key == K_SPACE and not self.playing:
    #         self.reset()


