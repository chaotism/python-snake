#coding: utf-8
from __future__  import generators, print_function, division, unicode_literals
from game_source.graphics import DIRECTION_UP,DIRECTION_DOWN,DIRECTION_LEFT,DIRECTION_RIGHT


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
    def __init__(self, render):
        self.render = render

    def update(self):
        key = self.render.screen.getch()
        if key > 0:
            #raise Exception(key)
            #TODO: переделать просто через словарь или extended choice
            if key == self.keys['DOWN']:
                return 'DOWN'
                
            elif key ==  self.keys['LEFT']:
                return 'LEFT'

            elif key ==  self.keys['RIGHT']:
                return 'RIGHT'

            elif key ==  self.keys['UP']:
                return 'UP'

            elif key ==  self.keys['Q']:
                return 'EXIT'

            elif key ==  self.keys['ENTER']:
                return 'ENTER'