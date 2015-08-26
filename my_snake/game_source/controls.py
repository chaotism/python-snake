#coding: utf-8
from __future__  import generators, print_function, division, unicode_literals
from collections import deque
import pygame
from random import randrange
import sys
from pygame.locals import *
from level import Level
from snake import Snake
from graphics import Point, DIRECTION_DOWN, DIRECTION_UP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_DR

# Map from PyGame key event to the corresponding direction. #TODO: move to control
KEY_DIRECTION = {
    'w': DIRECTION_UP,
     K_UP: DIRECTION_UP,
    's': DIRECTION_DOWN,
   K_DOWN: DIRECTION_DOWN,
    'a': DIRECTION_LEFT,
   K_LEFT: DIRECTION_LEFT,
    'd': DIRECTION_RIGHT,
  K_RIGHT: DIRECTION_RIGHT,
}
