#!/usr/bin/env python
import sys
from game_source.engine import Engine

game = Engine()


def main():
    game = Engine()
    game = Engine().play()

if __name__ == '__main__':
    main()
    sys.exit(0)
