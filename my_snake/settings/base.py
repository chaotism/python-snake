# coding: utf-8
# Default config
SNAKE_START_LENGTH = 2
SEGMENT_SCORE = 50
WORLD_SIZE = 20
TIME_DELTA = 0.15

# Default config snake
SNAKE_SPEED_INITIAL = 4.0  # Initial snake speed (squares per second)
SNAKE_SPEED_INCREMENT = 0.25  # Snake speeds up this much each time it grows
SNAKE_START_LENGTH = 2
GROWTH_PENDING = 1

# Default render config
RENDER = 'adapters.curses.render'
#TODO: учитывая, что управление зависит от текущей библиотеки для рендига, есть смысл просто указывать адаптер
# Default control config
CONTROLLER = 'adapters.curses.controls'
