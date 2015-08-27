# coding: utf-8
from __future__ import generators, print_function, division, unicode_literals
import unittest
from game_source.snake import Snake
from game_source.graphics import Point, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
from settings import SNAKE_SPEED_INITIAL, SNAKE_SPEED_INCREMENT, WORLD_SIZE


#==============================================================================
class utest_Snake(unittest.TestCase):
    
    def test_crash(self):
        """
        Tests the following crash:
        
        0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0               
        0 0 0 0 0 0    0 0 0 0 1 0    0 0 0 1 1 0    0 0 0 1 1 0               
        1 1 1 1 1 0 -> 0 1 1 1 1 0 -> 0 0 1 1 1 0 -> 0 0 0 2 1 0 <--- overlap 
        0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0      at 2
        0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0               
        0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0    0 0 0 0 0 0               
        """
        world_center = Point((WORLD_SIZE // 2, WORLD_SIZE // 2))
        snake = Snake(start=world_center, start_length=6)
        self.assertFalse(snake.self_intersecting())

        snake.change_direction(DIRECTION_UP)
        snake.timer = 0
        snake.update()
        self.assertFalse(snake.self_intersecting())
        snake.change_direction(DIRECTION_LEFT)
        snake.timer = 0
        snake.update()
        self.assertFalse(snake.self_intersecting())
        snake.change_direction(DIRECTION_DOWN)
        snake.timer = 0
        snake.update()
        self.assertTrue(snake.self_intersecting())

    def test_direction(self):
        world_center = Point((WORLD_SIZE // 2, WORLD_SIZE // 2))
        snake = Snake(start=world_center, start_length=6)
        self.assertEqual(snake.get_head(), world_center)
        snake.change_direction(DIRECTION_LEFT)
        snake.timer = 0
        snake.update()
        # opposite direction changes nothing
        self.assertEqual(snake.get_head(), world_center+DIRECTION_RIGHT)
        # no changes in the scales
        self.assertFalse(snake.update())

    def test_grow(self):
        """
        Test growing does this.

        0 0 0 0 0 0    0 0 0 0 0 0
        0 0 0 0 0 0 -> 0 0 0 0 0 0
        0 1 1 1 0 0    0 1 1 1 1 0
        0 0 0 0 0 0    0 0 0 0 0 0
        """
        world_center = Point((WORLD_SIZE // 2, WORLD_SIZE // 2))
        start_length = 5
        snake = Snake(start=world_center, start_length=start_length, growth_pending=1)
        snake.grow()
        self.assertEqual(snake.speed, SNAKE_SPEED_INITIAL+SNAKE_SPEED_INCREMENT)
        snake.timer = 0
        snake.update()
        self.assertEqual(len(snake), start_length+1)
