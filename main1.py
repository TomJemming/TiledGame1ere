import pygame as pg
import random
import sys
import os

HEIGHT = 1080
WIDTH = 1920
FPS = 10

GRID_SIZE = 64
GRID_HEIGHT = HEIGHT/GRID_SIZE
GRID_WIDTH = WIDTH/GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (80, 80, 80)


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(GREEN)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def movement(self, mx=0, my=0):
        self.x += mx
        if g.wall_collision():
            self.x -= mx
        self.y += my
        if g.wall_collision():
            self.y -= my

    def update(self):
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(BLUE)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption("Allo.")
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1, 200)
        self.running = True

    def load(self):
        g_location = os.path.dirname(__file__)
        self.map = []
        with open(os.path.join(g_location, "map.txt"), "rt") as file:
            for line in file:
                self.map.append(line)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.all_walls = []
        self.load()
        self.create_map()
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            self.update()

    def grid(self):
        for i in range(0, WIDTH, GRID_SIZE):
            pg.draw.line(self.screen, DARKGREY, (i, 0), (i, HEIGHT))
        for i in range(0, HEIGHT, GRID_SIZE):
            pg.draw.line(self.screen, DARKGREY, (0, i), (WIDTH, i))

    def create_map(self):
        for posy, line in enumerate(self.map):
            for posx, symbol in enumerate(line):
                if symbol == "W":
                    w = Wall(self, x=posx, y=posy)
                    self.all_sprites.add(w)
                    self.all_walls.append((posx, posy))
                if symbol == "P":
                    self.player = Player(self, posx, posy)
                    self.all_sprites.add(self.player)

    def wall_collision(self):
        player_cords = (self.player.x, self.player.y)
        for wall in self.all_walls:
            if wall == player_cords:
                return True
        return False

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.movement(my=-1)
                if event.key == pg.K_s:
                    self.player.movement(my=+1)
                if event.key == pg.K_a:
                    self.player.movement(mx=-1)
                if event.key == pg.K_d:
                    self.player.movement(mx=+1)
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        self.all_sprites.update()
        self.clock.tick(FPS)


g = Game()
while g.running:
    g.new()
pg.quit()
