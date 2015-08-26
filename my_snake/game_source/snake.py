#coding: utf-8
from __future__ import generators, print_function, division, unicode_literals
from collections import deque
import pygame
from random import randrange
import sys
from pygame.locals import *
from graphics import Blocks, Point, DIRECTION_RIGHT

SNAKE_SPEED_INITIAL = 4.0  # Initial snake speed (squares per second)
SNAKE_SPEED_INCREMENT = 0.25  # Snake speeds up this much each time it grows
TIME_DELTA = 0.15
GROWTH_PENDING = 1  # Number of segments still to grow.


class Snake(Blocks):

    def __init__(self, start=Point((1, 1)), start_length=2):
        self.speed = SNAKE_SPEED_INITIAL  # Speed in squares per second.
        self.timer = self.get_timer()  # Time remaining to next movement.
        self.timedelta = TIME_DELTA #need to config
        self.growth_pending = GROWTH_PENDING  # Number of segments still to grow.
        self.direction = DIRECTION_RIGHT  # Current movement direction.
        seq = [start - self.direction * i for i in range(start_length)]
        return super(Snake, self).__init__(seq, form='snake', eatable=False)

    def get_timer(self):
        return 1.0 / self.speed

    def change_direction(self, direction):
        """Update the direction of the snake."""
        # Moving in the opposite direction of current movement is not allowed.
        if self.check_timer():
            if self.direction != -direction:
                self.direction = direction

    def get_head(self):
        """Return the position of the snake's head."""
        return self[0]

    def check_timer(self):
        """Update the snake by dt seconds and possibly set direction."""
        self.timer -= self.timedelta
        if self.timer > 0:
            return True
        else:
            self.timer = self.get_timer()
            return False

    def update(self):
        if self.check_timer():
            return False
        self.appendleft(self.get_head() + self.direction)
        if self.growth_pending > GROWTH_PENDING:
            self.growth_pending -= GROWTH_PENDING
        else:
            # Remove tail.
            self.pop()
        # raise Exception(self)
        return True

    def grow(self):
        """Grow snake by one segment and speed up."""
        self.growth_pending += 1
        self.speed += SNAKE_SPEED_INCREMENT

    def self_intersecting(self):
        """Is the snake currently self-intersecting?"""
        it = iter(self)
        head = next(it)
        return head in it

    def bound(self, world_size):
        """Detect border"""
        self[0][0] = self[0][0] % (world_size-1)
        self[0][1] = self[0][1] % (world_size-1)