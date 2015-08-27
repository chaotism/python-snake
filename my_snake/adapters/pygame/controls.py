# coding: utf-8
from __future__ import generators, print_function, division, unicode_literals
import pygame
from pygame.locals import Rect, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
from game_source.graphics import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT


class Controls(object):
    # Map from curses key event to the corresponding direction.
    keys = {
        'DOWN': ord('s'),
        'LEFT': ord('a'),
        'RIGHT': ord('d'),
        'UP': ord('w'),
        'Q': ord('q'),
        'ENTER': 10,
    }

    # KEY_DIRECTION = {
    #     'K_w': DIRECTION_UP, K_UP: DIRECTION_UP,
    #     'K_s': DIRECTION_DOWN, K_DOWN: DIRECTION_DOWN,
    #     'K_a': DIRECTION_LEFT, K_LEFT: DIRECTION_LEFT,
    #     'K_d': DIRECTION_RIGHT, K_RIGHT: DIRECTION_RIGHT,
    # }

    def __init__(self, render):
        pygame.event.pump()
        self.render = render

    def update(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                key = e.key
                # print(key)
                if key == self.keys['DOWN']:
                    return 'DOWN'

                elif key == self.keys['LEFT']:
                    return 'LEFT'

                elif key == self.keys['RIGHT']:
                    return 'RIGHT'

                elif key == self.keys['UP']:
                    return 'UP'

                elif key == self.keys['Q']:
                    return 'EXIT'

                elif key == self.keys['ENTER']:
                    return 'ENTER'
