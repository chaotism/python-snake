# python imports
import random

# local imports
        
#==============================================================================
class Snake(object):
    """
    The snake lives in a XxY box.
    """

    def __init__(self, crash, board):
        direction = (1, 0)
        self.board = board
        self.scales = [
            Scale(9, 9, direction, self.board),
            Scale(8, 9, direction, self.board),
            Scale(7, 9, direction, self.board),
            ]
        self.crash_callback = crash

    def __contains__(self, coord):
        for scale in self.scales:
            if (scale.x == coord.x and scale.y == coord.y):
                return True
        return False

    def chomp(self):
        """
        Retuns if the snake has eaten itself.
        """
        coords = []
        for scale in self.scales:
            coord = (scale.x, scale.y)
            if (coord in coords):
                return True
            coords.append(coord)
        return False

    def grow(self):
        # add a non-moving scale
        end_scale = self.scales[-1]
        for scale in reversed(self.scales):
            if (scale.direction != (0, 0)):
                direction = scale.direction
                break
        scale = Scale(end_scale.x, end_scale.y, (0, 0), self.board)
        scale.change_direction(1, direction)
        for change in end_scale.changes:
            if (not change.done()):
                scale.change_direction(change.count + 1, change.direction)
        self.scales.append(scale)

    def step(self):
        for scale in self.scales:
            scale.step()
        if (self.chomp()):
            self.crash_callback()

    def change_direction(self, direction):
        opposite_direction = (
            -self.scales[0].direction[0],
            -self.scales[0].direction[1],
             )
        if (direction not in [opposite_direction, self.scales[0].direction]):
            for i, scale in enumerate(self.scales):
                scale.change_direction(i, direction)
    
    @property
    def direction(self):
        return self.scales[0].direction

    def up(self):
        self.change_direction((0, -1))

    def down(self):
        self.change_direction((0, 1))

    def left(self):
        self.change_direction((-1, 0))

    def right(self):
        self.change_direction((1, 0))

#==============================================================================
class Scale(object):
    """
    One of the snakes scales, it has it's own direction and coordinate
    """
    
    def __init__(self, x, y, direction, board):
        self.x = x
        self.y = y
        self.board = board
        self.direction = direction
        self.changes = []

    def step(self):
        for change in self.changes:
            change.step()
        self.x = (self.x + self.direction[0]) % self.board.x
        self.y = (self.y + self.direction[1]) % self.board.y

    def change_direction(self, change_number, direction):
        change = Change(change_number, direction, self)
        self.changes.append(change)

#==============================================================================
class Change(object):

    def __init__(self, count, direction, scale):
        self.count = count
        self.direction = direction
        self.scale = scale

    def step(self):
        if (self.count == 0):
            self.scale.direction = self.direction
        self.count -= 1

    def done(self):
        """
        If the count is no longer useful.
        """
        return self.count <= 0

#==============================================================================
class Fruit(object):

    def __init__(self, snake, board):
        """
        Pass in the snake so this can avoid it, and a callback for when this
        is eaten.
        """
        while (True):
            self.x = random.randrange(board.x)
            self.y = random.randrange(board.y)
            if (not self in snake):
                break

#==============================================================================
class SnakeController(object):

    KEYS = {
        "Up": lambda self: self.up(),
        "Down": lambda self: self.down(),
        "Left": lambda self: self.left(),
        "Right": lambda self: self.right(),
        "w": lambda self: self.up(),
        "s": lambda self: self.down(),
        "a": lambda self: self.left(),
        "d": lambda self: self.right(),
        }

    def __init__(self, view, game_over, board):
        self.board = board
        self.snake = Snake(game_over, self.board)
        self.fruit = None
        self.view = view
        self.view.parent.bind("<Key>", self.key)

    def up(self):
        self.change_direction(self.snake.up)

    def down(self):
        self.change_direction(self.snake.down)

    def left(self):
        self.change_direction(self.snake.left)

    def right(self):
        self.change_direction(self.snake.right)

    def change_direction(self, direction_function):
        if (not self.block):
            direction_function()
            self.block = True

    def key(self, event):
        if (event.keysym in SnakeController.KEYS):
            SnakeController.KEYS[event.keysym](self)

    def step(self):
        """
        Moves the snake one step.
        """
        self.block = False
        self.snake.step()
        self.check_fruit()
        self.view.draw_snake(self.snake)
        self.view.draw_fruit(self.fruit)
        # recurse this
        self.view.after(300, self.step)

    def start(self):
        self.add_fruit()
        self.step()

    def check_fruit(self):
        if (self.fruit in self.snake):
            self.snake.grow()
            self.add_fruit()
    
    def add_fruit(self):
        self.fruit = Fruit(self.snake, self.board)
        
#==============================================================================
if (__name__ == "__main__"):
    pass
