# coding: utf-8
from __future__ import generators, print_function, division
import importlib
import sys
from settings import CONTROLLER
from graphics import Point, DIRECTION_DOWN, DIRECTION_UP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_DR

try:
    controller_module = importlib.import_module(CONTROLLER)
    Controls = getattr(controller_module, 'Controls')
except ImportError, AttributeError:
    from adapters.controls.default import Controls


class Controller(object):
    KEY_DIRECTION = {
        'UP': DIRECTION_UP,

        'DOWN': DIRECTION_DOWN,

        'LEFT': DIRECTION_LEFT,

        'RIGHT': DIRECTION_RIGHT,

        'EXIT': 'EXIT'
    }

    def __init__(self, render):
        self.render = render
        self.controls = Controls(self.render)

    def update(self):
        key = self.controls.update()
        if key in self.KEY_DIRECTION:
            direction = self.KEY_DIRECTION.get(self.controls.update())
            if direction == 'EXIT':
                sys.exit(1)
            return direction
