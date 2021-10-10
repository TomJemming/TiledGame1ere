import pygame, sys
from random import randint

size = (500, 1000)
fps = 15
white = (255, 255, 255)
darkgrey = (120, 120, 120)
light_grey = (169, 169, 169)
black = (0, 0, 0)
green = pygame.image.load("images/green.png")
blue = pygame.image.load("images/blue.png")
purple = pygame.image.load("images/purple.png")
orange = pygame.image.load("images/orange.png")
red = pygame.image.load("images/red.png")
yellow = pygame.image.load("images/yellow.png")
light_blue = pygame.image.load("images/light_blue.png")


forms = ["I", "T","O", "L", "J", "S", "Z"]
COLORS = {"I": blue, "O": yellow, "T": purple, "L": red,
          "J": green, "S": orange, "Z": light_blue}
SHAPES = {"I": [[[1, 1, 1, 1], [0, 0,0,0],[0,0,0,0],[0,0,0,0]], [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]], [[1, 1, 1, 1], [0, 0,0,0],[0,0,0,0],[0,0,0,0]], [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]],
          "O": [[[1, 1,0,0], [1, 1,0,0],[0,0,0,0],[0,0,0,0]], [[1, 1,0,0], [1, 1,0,0],[0,0,0,0],[0,0,0,0]],[[1, 1,0,0], [1, 1,0,0],[0,0,0,0],[0,0,0,0]],[[1, 1,0,0], [1, 1,0,0],[0,0,0,0],[0,0,0,0]]],
          "T": [[[1, 1, 1,0], [0, 1, 0,0],[0,0,0,0],[0,0,0,0]], [[0,0,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0]], [[0,1,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]]],
          "L": [[[1, 1, 1,0], [1, 0, 0,0],[0,0,0,0],[0,0,0,0]], [[1,1,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]],[[0,0,1,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]], [[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,0,0,0]]],
          "J": [[[1, 1, 1,0], [0,0,1,0],[0,0,0,0],[0,0,0,0]],[[0,0,1,0],[0,0,1,0],[0,1,1,0],[0,0,0,0]],[[1,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0]], [[1,1,0,0],[1,0,0,0],[1,0,0,0],[0,0,0,0]]],
          "S": [[[0, 1, 1,0], [1, 1, 0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]],[[0, 1, 1,0], [1, 1, 0,0],[0,0,0,0],[0,0,0,0]],[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]]],
          "Z": [[[1, 1, 0,0], [0, 1, 1,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]],[[1, 1, 0,0], [0, 1, 1,0],[0,0,0,0],[0,0,0,0]],[[0,1,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]]]}
pos_other_blocks = []


def init_game():
    pygame.init()
    global surface, clock
    surface = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()


def update_gamestate():
    surface.fill((80,80,80))
    for el in game.items:
        el.draw()
    clock.tick(2)


def check_row():
    for i in range(19):
        counter = 0
        for el in pos_other_blocks:
            if el[1] == i+1:
                counter += 1
        if counter >= 10:
            for el in game.items:
                el.y += 1
            break


def move_down():
    block = game.selected_item
    block.move(0, 1)


def choose_block():
    x = game.selected_item.get_cells()
    for el in x:
        pos_other_blocks.append(el)
    i = randint(0, 6)
    new = forms[i]
    t = Tetris(new)
    game.add(t)


def new_block():
    block = game.selected_item
    pos = block.get_cells()
    lowest_block = 0
    for i in range(len(pos)):
        if pos[i][1] > lowest_block:
            lowest_block = pos[i][1]
    if lowest_block >= 19:
        choose_block()
    else:
        for el in pos:
            if (el[0], el[1] + 1) in pos_other_blocks:
                choose_block()
                break


def handle_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            block = game.selected_item
            if event.key == pygame.K_RIGHT:
                right = False
                for el in block.get_cells():
                    if el[0] == 9:
                        right = True
                if not right:
                    block.move(1, 0)
            if event.key == pygame.K_LEFT:
                left = False
                for el in block.get_cells():
                    if el[0] == 0:
                        left = True
                if not left:
                    block.move(-1, 0)
            if event.key == pygame.K_DOWN:
                block.move(0, 1)
            if event.key == pygame.K_SPACE:
                block.rotate()
                check_border()


def check_border():
    collision = False
    block = game.selected_item
    pos = block.get_cells()
    for i in pos:
        if i[0] > 9:
            k = i[0]
            collision =True
    if collision:
        block.move(9 - k, 0)


class Tetris:

    def __init__(self, kind, x=4, y=0):
        self.x = x
        self.y = y
        self.shape = SHAPES[kind]
        self.shapescount = 0
        self.color = COLORS[kind]
        self.pos = 0

    def get_cells(self):
        o_cells = []
        for i in range(len(self.shape[self.shapescount])):
            for j in range(len(self.shape[self.shapescount][i])):
                if self.shape[self.shapescount][i][j] == 1:
                    o_cells.append((i + self.x, j + self.y))
        return o_cells

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shapescount -= 1
        if self.shapescount == -4:
            self.shapescount = 0


    def remove(self, coords):
        for el in self.shape[self.shapescount]:
            if el == [0,0,0,0]:
                pass


    def block(self, x, y):
        surface.blit(self.color, (x * 50, y * 50))


    def draw(self):
        o_cells = self.get_cells()
        for el in o_cells:
            self.block(el[0], el[1])
        pygame.display.flip()


class TetrominoesList:

    def __init__(self):
        self.items = []
        self.selected_item = None
        self.counts = {"I": 0, "O": 0, "T": 0, "L": 0, "J": 0, "S": 0, "Z": 0}

    def add(self, t):
        self.items.append(t)
        self.selected_item = t

    def remove(self, t):
        if t in self.items:
            self.items[self.items.index(t)] = 0
        self.selected_item = None

    def get_item_remaining(self, x, y):
        for el in self.items:
            if el.get_cells == (x, y):
                self.selected_item = self.items[el]

    def draw(self):
        for el in self.items:
            el.draw()

    def new_count(self, shape):
        self.counts[shape] += 1


# main
def start():
    global game, running, surface
    init_game()
    game = TetrominoesList()
    p = Tetris("I")
    game.add(p)
    p.draw()
    running = True
    while running:
        move_down()
        handle_events()
        new_block()
        check_row()
        update_gamestate()
    surface = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
