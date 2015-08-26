#coding: utf-8
from __future__  import generators, print_function, division, unicode_literals
import importlib
#from pygame.locals import *
from settings import CONTROLLER
from graphics import Point, DIRECTION_DOWN, DIRECTION_UP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_DR

control_module = importlib.import_module(CONTROLLER)
Controls = getattr(control_module, 'Controls')


# Map from PyGame key event to the corresponding direction. #TODO: move to control
KEY_DIRECTION = {
    'w': DIRECTION_UP,
     #K_UP: DIRECTION_UP,
    's': DIRECTION_DOWN,
   #K_DOWN: DIRECTION_DOWN,
    'a': DIRECTION_LEFT,
   #K_LEFT: DIRECTION_LEFT,
    'd': DIRECTION_RIGHT,
  #K_RIGHT: DIRECTION_RIGHT,
}
