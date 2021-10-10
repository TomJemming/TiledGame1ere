import pygame as pg
import random
import os
import pong
import dinosaur_game as dino
import tower_defense as tower
import tetris
import write_text

HEIGHT = 1080
WIDTH = 1920
FPS = 240

GRID_SIZE = 32
GRID_HEIGHT = HEIGHT/GRID_SIZE
GRID_WIDTH = WIDTH/GRID_SIZE

SPEED = GRID_SIZE/2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (80, 80, 80)

font = pg.font.SysFont("Palatino", 48)


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
            i.interact(i.game_type)

    def update(self):
        if self.rect.x != self.x * GRID_SIZE:
            self.rect.x += int(self.mx * SPEED)
            self.R = random.randrange(0, 255)
            self.G = random.randrange(0, 255)
            self.B = random.randrange(0, 255)
        if self.rect.y != self.y * GRID_SIZE:
            self.rect.y += int(self.my * SPEED)
            self.R = random.randrange(0, 255)
            self.G = random.randrange(0, 255)
            self.B = random.randrange(0, 255)
        self.image.fill((self.R, self.G, self.B))


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = color
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE


class Npc(pg.sprite.Sprite):
    def __init__(self, game, x, y, game_type, color):
        pg.sprite.Sprite.__init__(self)
        self.image = color
        self.game_type = game_type
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GRID_SIZE
        self.rect.y = self.y * GRID_SIZE

    def interact(self, game):
        if abs(self.x - g.player.x) + abs(self.y - g.player.y) <= 1:
            self.do_smth(game)

    def do_smth(self, game):
        if game == pong:
            write_text.start(g.screen, "Start pong?")
        if game == dino:
            write_text.start(g.screen, "Start dinosaur game?")
        if game == tower:
            write_text.start(g.screen, "Start school defense?")
        if game == tetris:
            write_text.start(g.screen, "Start tetris?")
        if write_text.check_play() == 2:
            game.start()


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def get_offset(self, obj):
        return obj.rect.move(self.camera.topleft)

    def update(self, player):
        x = -player.rect.x + int(WIDTH/2)
        y = -player.rect.y + int(HEIGHT/2) - 28

        self.camera = pg.Rect(x, y, self.width, self.height)


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption("Allo.")
        self.clock = pg.time.Clock()
        self.running = True

    def load(self):
        g_location = os.path.dirname(__file__)
        self.map = []
        with open(os.path.join(g_location, "map.txt"), "rt") as file:
            for line in file:
                self.map.append(line)
        self.all_textures = {}
        self.all_textures_hitbox = {}
        self.all_textures_hitbox["D"] = pg.image.load(os.path.join("images/glas_v.png"))
        self.all_textures_hitbox["S"] = pg.image.load(os.path.join("images/glas_h.png"))
        self.all_textures_hitbox["U"] = pg.image.load(os.path.join("images/glas_u.png"))
        self.all_textures_hitbox["W"] = pg.image.load(os.path.join("images/wall.png"))
        self.all_textures_hitbox["Q"] = pg.image.load(os.path.join("images/table.png"))
        self.all_textures["f"] = pg.image.load(os.path.join("images/wooden_tiles.png"))
        self.all_textures["l"] = pg.image.load(os.path.join("images/tiles_big.png"))
        self.all_textures["g"] = pg.image.load(os.path.join("images/tiles.png"))
        self.all_textures["p"] = pg.image.load(os.path.join("images/tiles_big.png"))
        self.all_textures_hitbox["pong_0"] = pg.image.load(os.path.join("images/pong_1.png"))
        self.all_textures_hitbox["pong_1"] = pg.image.load(os.path.join("images/pong_2.png"))
        self.all_textures_hitbox["pong_2"] = pg.image.load(os.path.join("images/pong_2.png"))
        self.all_textures_hitbox["pong_3"] = pg.image.load(os.path.join("images/pong_3.png"))
        self.all_textures_hitbox["dino_0"] = pg.image.load(os.path.join("images/dino_1.png"))
        self.all_textures_hitbox["dino_1"] = pg.image.load(os.path.join("images/dino_2.png"))
        self.all_textures_hitbox["dino_2"] = pg.image.load(os.path.join("images/dino_3.png"))
        self.all_textures_hitbox["dino_3"] = pg.image.load(os.path.join("images/dino_4.png"))
        self.all_textures_hitbox["tower_0"] = pg.image.load(os.path.join("images/tower_1.png"))
        self.all_textures_hitbox["tower_1"] = pg.image.load(os.path.join("images/tower_2.png"))
        self.all_textures_hitbox["tower_2"] = pg.image.load(os.path.join("images/tower_3.png"))
        self.all_textures_hitbox["tower_3"] = pg.image.load(os.path.join("images/tower_4.png"))
        self.all_textures_hitbox["tetris_0"] = pg.image.load(os.path.join("images/tetris_1.png"))
        self.all_textures_hitbox["tetris_1"] = pg.image.load(os.path.join("images/tetris_2.png"))
        self.all_textures_hitbox["tetris_2"] = pg.image.load(os.path.join("images/tetris_3.png"))
        self.all_textures_hitbox["tetris_3"] = pg.image.load(os.path.join("images/tetris_4.png"))

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
                if symbol.islower():
                    for item in self.all_textures:
                        if item == symbol:
                            w = Wall(self, x=posx, y=posy, color=self.all_textures[item])
                            self.all_sprites.add(w)

                if symbol.isupper():
                    for item in self.all_textures_hitbox:
                        if item == symbol:
                            g = Wall(self, x=posx, y=posy, color=self.all_textures_hitbox[item])
                            self.all_sprites.add(g)
                            self.all_walls.append((posx, posy))

                if symbol == "#":
                    x = 0
                    for i in range(2):
                        for j in range(2):
                            t = Npc(self, x=posx + i, y=posy + j, game_type=pong, color=self.all_textures_hitbox[f"pong_{x}"])
                            self.all_sprites.add(t)
                            self.all_walls.append((posx, posy))
                            self.all_npcs.append(t)
                            x += 1

                if symbol == "*":
                    x = 0
                    for i in range(2):
                        for j in range(2):
                            t = Npc(self, x=posx + i, y=posy + j, game_type=dino, color=self.all_textures_hitbox[f"dino_{x}"])
                            self.all_sprites.add(t)
                            self.all_walls.append((posx, posy))
                            self.all_npcs.append(t)
                            x += 1

                if symbol == "'":
                    x = 0
                    for i in range(2):
                        for j in range(2):
                            t = Npc(self, x=posx + i, y=posy + j, game_type=tower, color=self.all_textures_hitbox[f"tower_{x}"])
                            self.all_sprites.add(t)
                            self.all_walls.append((posx, posy))
                            self.all_npcs.append(t)
                            x += 1

                if symbol == "&":
                    x = 0
                    for i in range(2):
                        for j in range(2):
                            t = Npc(self, x=posx + i, y=posy + j, game_type=tetris, color=self.all_textures_hitbox[f"tetris_{x}"])
                            self.all_sprites.add(t)
                            self.all_walls.append((posx, posy))
                            self.all_npcs.append(t)
                            x += 1

                if symbol == "p":
                    self.player = Player(self, posx, posy)
                    self.player_list.add(self.player)

                if symbol == "+":
                    self.all_walls.append((posx, posy))

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
