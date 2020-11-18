import pygame as pg
import random
import os

HEIGHT = 1080
WIDTH = 1920
FPS = 240

GRID_SIZE = 32
GRID_HEIGHT = HEIGHT/GRID_SIZE
GRID_WIDTH = WIDTH/GRID_SIZE

SPEED = GRID_SIZE/4

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
        self.mx = 0
        self.my = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE
        self.R = 0
        self.G = 255
        self.B = 0

    def movement(self, mx=0, my=0):
        if not self.wall_collision(mx=mx):
            if self.rect.x == self.x * GRID_SIZE:
                self.x += mx
                self.mx = mx

        if not self.wall_collision(my=my):
            if self.rect.y == self.y * GRID_SIZE:
                self.y += my
                self.my = my

    def wall_collision(self, mx=0, my=0):
        player_cords = (self.x + mx, self.y + my)
        for wall in g.all_walls:
            if wall == player_cords:
                return True
        return False

    def interact(self):
        for i in g.all_npcs:
            i.interact()

    def update(self):
        if self.rect.x != self.x * GRID_SIZE:
            self.rect.x += self.mx * SPEED
            self.R = random.randrange(0,255)
            self.G = random.randrange(0,255)
            self.B = random.randrange(0,255)
        if self.rect.y != self.y * GRID_SIZE:
            self.rect.y += self.my * SPEED
            self.R = random.randrange(0,255)
            self.G = random.randrange(0,255)
            self.B = random.randrange(0,255)
        self.image.fill((self.R, self.G, self.B))


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(color)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE



class Npc(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((GRID_SIZE, GRID_SIZE))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE
        self.R = 255
        self.G = 0
        self.B = 0
        self.image.fill((self.R, self.G, self.B))

    def interact(self):
        for i in range(g.player.x - 1, g.player.x + 2):
            for j in range(g.player.y - 1, g.player.y + 2):
                if i == self.x:
                    if j == self.y:
                        self.do_smth()

    def do_smth(self):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.image.fill((self.R, self.G, self.B))


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def get_offset(self, object):
        return object.rect.move(self.camera.topleft)

    def update(self, player):
        x = -player.rect.x + int(WIDTH/2)
        y = -player.rect.y + int(HEIGHT/2) - 28

        #print(f"g_map_width: {g.map_width}, playerrecty: {player.rect.y/32}, x: {x/32}, y:{y/32}")

        x = min(-1*GRID_SIZE, x)
        y = min(-1*GRID_SIZE, y)
        x = max(-76*GRID_SIZE, x)
        y = max(-91*GRID_SIZE, y)
        self.camera = pg.Rect(x, y, self.width, self.height)


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption("Allo.")
        self.clock = pg.time.Clock()
        #pg.key.set_repeat(1, 200)
        self.running = True

    def load(self):
        g_location = os.path.dirname(__file__)
        self.map = []
        with open(os.path.join(g_location, "map.txt"), "rt") as file:
            for line in file:
                self.map.append(line)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player_list = pg.sprite.Group()
        self.all_walls = []
        self.all_npcs = []
        self.load()
        self.create_map()
        self.camera = Camera(self.map_width, self.map_height)
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
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)

        for posy, line in enumerate(self.map):
            for posx, symbol in enumerate(line):
                if symbol == "W":
                    w = Wall(self, x=posx, y=posy, color=BLUE)
                    self.all_sprites.add(w)
                    self.all_walls.append((posx, posy))

                if symbol == "G":
                    g = Wall(self, x=posx, y=posy, color=DARKGREY)
                    self.all_sprites.add(g)

                if symbol == "T":
                    t = Npc(self, x=posx, y=posy)
                    self.all_sprites.add(t)
                    self.all_walls.append((posx, posy))
                    self.all_npcs.append(t)

                if symbol == "P":
                    self.player = Player(self, posx, posy)
                    self.player_list.add(self.player)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.key == pg.K_SPACE:
                    self.player.interact()

        keys_pressed = pg.key.get_pressed()

        if keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]:
            self.player.movement(mx=-1)
        if keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]:
            self.player.movement(mx=1)
        if keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]:
            self.player.movement(my=-1)
        if keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]:
            self.player.movement(my=1)

    def draw(self):
        self.screen.fill(BLACK)
        #self.grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.get_offset(sprite))
        for sprite in self.player_list:
            self.screen.blit(sprite.image, self.camera.get_offset(sprite))
        pg.display.flip()

    def update(self):
        self.all_sprites.update()
        self.player_list.update()
        self.camera.update(self.player)

        self.clock.tick(FPS)


g = Game()
while g.running:
    g.new()
pg.quit()
