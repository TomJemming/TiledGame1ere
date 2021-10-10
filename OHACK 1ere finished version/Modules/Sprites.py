import pygame as pg
from settings import *
from math import *
import random


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.spritegroup = game.all_sprites
        self.wallgroup = game.walls
        pg.sprite.Sprite.__init__(self, self.spritegroup, self.wallgroup)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Language(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.towergroup = game.towergroup
        pg.sprite.Sprite.__init__(self, self.groups, self.towergroup)
        self.game = game
        self.image = pg.image.load('Images\Language.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x+1/TILESIZE
        self.y = y+1/TILESIZE
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.timestohit = 5
        self.timeshit = 5
        self.e_hit = 3
        self.e_chit = 0

    def delete(self, pos):
        px, py = pos[0], pos[1]
        if self.rect.x == px+1:
            if self.rect.y == py+1:
                self.kill()
                return "t1"

    def check_for_ennemmy_and_money(self, list):
        self.e_chit = 0
        for i in list:
            x, y = i.get_pos()
            if hypot(self.rect.x-x, self.rect.y-y) < 100:
                i.damage(50)
                pg.draw.line(self.game.screen, RED, (self.rect.x+16, self.rect.y+16), (x+16, y+16), 3)
                for j in range(3):
                    if self.rect.x < x:
                        if self.rect.y < y:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                    else:
                        if self.rect.y < y:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                self.e_chit += 1
                if self.e_hit == self.e_chit:
                    break

    def get_pos(self):
        return self.rect.x, self.rect.y


class Chemie(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.towergroup = game.towergroup
        pg.sprite.Sprite.__init__(self, self.groups, self.towergroup)
        self.game = game
        self.image = pg.image.load('Images\Chemie.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x+1/TILESIZE
        self.y = y+1/TILESIZE
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.timestohit = 5
        self.timeshit = 5
        self.e_hit = 2
        self.e_chit = 0

    def delete(self, pos):
        px, py = pos[0], pos[1]
        if self.rect.x == px+1:
            if self.rect.y == py+1:
                self.kill()
                return "t2"

    def check_for_ennemmy_and_money(self, list):
        self.e_chit = 0
        for i in list:
            x, y = i.get_pos()
            if hypot(self.rect.x-x, self.rect.y-y) < 100:
                i.damage(250)
                pg.draw.line(self.game.screen, RED, (self.rect.x+16, self.rect.y+16), (x+16, y+16), 3)
                for j in range(3):
                    if self.rect.x < x:
                        if self.rect.y < y:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                    else:
                        if self.rect.y < y:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                self.e_chit += 1
                if self.e_hit == self.e_chit:
                    break

    def get_pos(self):
        return self.rect.x, self.rect.y


class Physik(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.towergroup = game.towergroup
        pg.sprite.Sprite.__init__(self, self.groups, self.towergroup)
        self.game = game
        self.image = pg.image.load('Images\Physics.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x+1/TILESIZE
        self.y = y+1/TILESIZE
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.timestohit = 5
        self.timeshit = 5
        self.e_hit = 8
        self.e_chit = 0

    def delete(self, pos):
        px, py = pos[0], pos[1]
        if self.rect.x == px+1:
            if self.rect.y == py+1:
                self.kill()
                return "t3"

    def check_for_ennemmy_and_money(self, list):
        self.e_chit = 0
        for i in list:
            x, y = i.get_pos()
            if hypot(self.rect.x-x, self.rect.y-y) < 100:
                i.damage(700)
                pg.draw.line(self.game.screen, RED, (self.rect.x+16, self.rect.y+16), (x+16, y+16), 3)
                for j in range(3):
                    if self.rect.x < x:
                        if self.rect.y < y:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                    else:
                        if self.rect.y < y:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                self.e_chit += 1
                if self.e_hit == self.e_chit:
                    break

    def get_pos(self):
        return self.rect.x, self.rect.y


class Mathe(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.towergroup = game.towergroup
        pg.sprite.Sprite.__init__(self, self.groups, self.towergroup)
        self.game = game
        self.image = pg.image.load('Images\Mathe.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x+1/TILESIZE
        self.y = y+1/TILESIZE
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.timestohit = 5
        self.timeshit = 5
        self.e_hit = 1
        self.e_chit = 0

    def delete(self, pos):
        px, py = pos[0], pos[1]
        if self.rect.x == px+1:
            if self.rect.y == py+1:
                self.kill()
                return "t4"

    def check_for_ennemmy_and_money(self, list):
        self.e_chit = 0
        for i in list:
            x, y = i.get_pos()
            if hypot(self.rect.x-x, self.rect.y-y) < 100:
                i.damage(2000)
                pg.draw.line(self.game.screen, RED, (self.rect.x+16, self.rect.y+16), (x+16, y+16), 16)
                for j in range(10):
                    if self.rect.x < x:
                        if self.rect.y < y:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(self.rect.x, x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                    else:
                        if self.rect.y < y:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(self.rect.y, y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                        else:
                            a = random.randint(x, self.rect.x)+16
                            b = random.randint(y, self.rect.y)+16
                            pg.draw.circle(self.game.screen, RED, (a, b), 1)
                self.e_chit += 1
                if self.e_hit == self.e_chit:
                    break

    def get_pos(self):
        return self.rect.x, self.rect.y


class Economie(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.towergroup = game.towergroup
        pg.sprite.Sprite.__init__(self, self.groups, self.towergroup)
        self.game = game
        self.image = pg.image.load('Images\Economie.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x+1/TILESIZE
        self.y = y+1/TILESIZE
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        self.pmonx = self.rect.x + 4
        self.pmony = self.rect.y
        self.spawnmoney = 200
        self.canspawnmoney = 50

    def delete(self, pos):
        px, py = pos[0], pos[1]
        if self.rect.x == px+1:
            if self.rect.y == py+1:
                self.kill()
                return "M"

    def check_for_ennemmy_and_money(self, list):
        if self.canspawnmoney % self.spawnmoney == 0:
            self.game.money += 20
        if self.canspawnmoney % self.spawnmoney < 50:
            font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 16)
            textt = font.render("+20", True, GREEN)
            textRect = textt.get_rect()
            textRect.topleft = (int(self.pmonx), int(self.pmony))
            self.game.screen.blit(textt, textRect)
            self.pmony -= 1/2
        if self.canspawnmoney % self.spawnmoney == 50:
            self.pmony = self.rect.y
        self.canspawnmoney += 1

    def get_pos(self):
        return self.rect.x, self.rect.y


class G(pg.sprite.Sprite):
    def __init__(self, game, x=902, y=1020, w=None, i=0):
        self.groups = game.all_sprites
        self.ennemylist = game.ennemylist
        pg.sprite.Sprite.__init__(self, self.groups, self.ennemylist)
        self.game = game
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
        self.image = font.render("G", True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4
        self.i = i
        if w is None:
            self.way = way[:]
        else:
            self.way = w[:]
        if self.game.difficulty == 1:
            self.health = 2000
        if self.game.difficulty == 2:
            self.health = 2500
        if self.game.difficulty == 3:
            self.health = 3000
        self.inithealth = self.health
        self.healthbefore = self.health
        self.rangelist = []
        for i in range(self.speed):
            self.rangelist.append(i)
            self.rangelist.append(-i)
        self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y, TILESIZE-1, self.way, self.i)
        self.mov_speed = 1

    def update(self):
        if self.mov_speed != 0:
            if self.health != self.healthbefore:
                Healthbar.awaybar(self.bar)
                x = int(32-(32*(1-self.health/self.inithealth)))
                self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y-3, x, self.way, self.i)
            self.move()

    def mov_stop(self):
        self.mov_speed = 0

    def mov_begin(self):
        self.mov_speed = 1

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
            self.game.health -= 1
            Healthbar.awaybar(self.bar)
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            self.game.money += 5
            Healthbar.awaybar(self.bar)
            self.game.k_ennemys += 1


class E(pg.sprite.Sprite):
    def __init__(self, game, x=902, y=1020, w=None, i=0):
        self.groups = game.all_sprites
        self.ennemylist = game.ennemylist
        pg.sprite.Sprite.__init__(self, self.groups, self.ennemylist)
        self.game = game
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
        self.image = font.render("E", True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4
        self.i = i
        if w is None:
            self.way = way[:]
        else:
            self.way = w[:]
        if self.game.difficulty == 1:
            self.health = 4000
        if self.game.difficulty == 2:
            self.health = 6000
        if self.game.difficulty == 3:
            self.health = 8000
        self.inithealth = self.health
        self.healthbefore = self.health
        self.rangelist = []
        for i in range(self.speed):
            self.rangelist.append(i)
            self.rangelist.append(-i)
        self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y, TILESIZE-1, self.way, self.i)
        self.mov_speed = 1

    def update(self):
        if self.mov_speed != 0:
            if self.health != self.healthbefore:
                Healthbar.awaybar(self.bar)
                x = int(32-(32*(1-self.health/self.inithealth)))
                self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y-3, x, self.way, self.i)
            self.move()

    def mov_stop(self):
        self.mov_speed = 0

    def mov_begin(self):
        self.mov_speed = 1

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
            self.game.health -= 4
            Healthbar.awaybar(self.bar)
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            Healthbar.awaybar(self.bar)
            G(self.game, self.rect.x, self.rect.y, self.way, self.i)
            G(self.game, self.rect.x, self.rect.y, self.way, self.i)
            self.game.k_ennemys += 1


class D(pg.sprite.Sprite):
    def __init__(self, game, x=902, y=1020, w=None, i=0):
        self.groups = game.all_sprites
        self.ennemylist = game.ennemylist
        pg.sprite.Sprite.__init__(self, self.groups, self.ennemylist)
        self.game = game
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
        self.image = font.render("D", True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4
        self.i = i
        if w is None:
            self.way = way[:]
        else:
            self.way = w[:]
        if self.game.difficulty == 1:
            self.health = 10000
        if self.game.difficulty == 2:
            self.health = 15000
        if self.game.difficulty == 3:
            self.health = 20000
        self.inithealth = self.health
        self.healthbefore = self.health
        self.rangelist = []
        for i in range(self.speed):
            self.rangelist.append(i)
            self.rangelist.append(-i)
        self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y, TILESIZE-1, self.way, self.i)
        self.mov_speed = 1

    def update(self):
        if self.mov_speed != 0:
            if self.health != self.healthbefore:
                Healthbar.awaybar(self.bar)
                x = int(32-(32*(1-self.health/self.inithealth)))
                self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y-3, x, self.way, self.i)
            self.move()

    def mov_stop(self):
        self.mov_speed = 0

    def mov_begin(self):
        self.mov_speed = 1

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
            self.game.health -= 8
            Healthbar.awaybar(self.bar)
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            Healthbar.awaybar(self.bar)
            E(self.game, self.rect.x, self.rect.y, self.way, self.i)
            E(self.game, self.rect.x, self.rect.y, self.way, self.i)
            self.game.k_ennemys += 1


class C(pg.sprite.Sprite):
    def __init__(self, game, x=902, y=1020, w=None, i=0):
        self.groups = game.all_sprites
        self.ennemylist = game.ennemylist
        pg.sprite.Sprite.__init__(self, self.groups, self.ennemylist)
        self.game = game
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
        self.image = font.render("C", True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 8
        self.i = i
        if w is None:
            self.way = way[:]
        else:
            self.way = w[:]
        if self.game.difficulty == 1:
            self.health = 20000
        if self.game.difficulty == 2:
            self.health = 25000
        if self.game.difficulty == 3:
            self.health = 30000
        self.inithealth = self.health
        self.healthbefore = self.health
        self.rangelist = []
        for i in range(self.speed):
            self.rangelist.append(i)
            self.rangelist.append(-i)
        self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y, TILESIZE-1, self.way, self.i, self.rangelist)
        self.mov_speed = 1

    def update(self):
        if self.mov_speed != 0:
            if self.health != self.healthbefore:
                Healthbar.awaybar(self.bar)
                x = int(32-(32*(1-self.health/self.inithealth)))
                self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y-3, x, self.way, self.i, self.rangelist)
            self.move()

    def mov_stop(self):
        self.mov_speed = 0

    def mov_begin(self):
        self.mov_speed = 1

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
            self.game.health -= 16
            Healthbar.awaybar(self.bar)
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            Healthbar.awaybar(self.bar)
            D(self.game, self.rect.x, self.rect.y, self.way, self.i)
            D(self.game, self.rect.x, self.rect.y, self.way, self.i)
            D(self.game, self.rect.x, self.rect.y, self.way, self.i)
            self.game.k_ennemys += 1


class B(pg.sprite.Sprite):
    def __init__(self, game, x=902, y=1020, w=None, i=0):
        self.groups = game.all_sprites
        self.ennemylist = game.ennemylist
        pg.sprite.Sprite.__init__(self, self.groups, self.ennemylist)
        self.game = game
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
        self.image = font.render("B", True, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 4
        self.i = i
        if w is None:
            self.way = way[:]
        else:
            self.way = w[:]
        if self.game.difficulty == 1:
            self.health = 30000
        if self.game.difficulty == 2:
            self.health = 40000
        if self.game.difficulty == 3:
            self.health = 60000
        self.inithealth = self.health
        self.healthbefore = self.health
        self.rangelist = []
        for i in range(self.speed):
            self.rangelist.append(i)
            self.rangelist.append(-i)
        self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y, TILESIZE-1, self.way, self.i)
        self.mov_speed = 1

    def update(self):
        if self.mov_speed != 0:
            if self.health != self.healthbefore:
                Healthbar.awaybar(self.bar)
                x = int(32-(32*(1-self.health/self.inithealth)))
                self.bar = Healthbar(self.game, self.speed, self.rect.x-4, self.rect.y-3, x, self.way, self.i)
            self.move()

    def mov_stop(self):
        self.mov_speed = 0

    def mov_begin(self):
        self.mov_speed = 1

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
            self.game.health -= 25
            Healthbar.awaybar(self.bar)
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.kill()
            Healthbar.awaybar(self.bar)
            C(self.game, self.rect.x, self.rect.y, self.way, self.i)
            C(self.game, self.rect.x, self.rect.y, self.way, self.i)
            C(self.game, self.rect.x, self.rect.y, self.way, self.i)
            C(self.game, self.rect.x, self.rect.y, self.way, self.i)
            self.game.k_ennemys += 1


class Healthbar(pg.sprite.Sprite):
    def __init__(self, game, speed, x, y, size, w, i, range=None):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = size
        self.image = pg.Surface((TILESIZE-1, 6))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 7
        self.speed = speed
        self.i = i
        self.way = w[:]
        if range is None:
            self.rangelist = [-3, -2, -1, 0, 1, 2, 3]
        else:
            self.rangelist = range
        self.bar = AnitHealthbar(self.game, self.speed, self.rect.x, self.rect.y, self.size, self.way, self.i, self.rangelist)

    def update(self):
        self.move()

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def awaybar(self):
        AnitHealthbar.awaybar(self.bar)
        self.kill()


class AnitHealthbar(pg.sprite.Sprite):
    def __init__(self, game, speed, x, y, size, w, i, range):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = size
        self.image = pg.Surface((self.size, 6))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.sczenario = 1
        self.i = i
        self.rangelist = range
        self.way = w[:]

    def update(self):
        self.move()

    def move(self):
        if self.way[self.i] in self.rangelist:
            self.i += 1
        if self.i == 26:
            self.kill()
        elif self.i % 2 == 0:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.y -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.y += self.speed
        elif self.i % 2 == 1:
            if self.way[self.i] <= 0:
                self.way[self.i] += self.speed
                self.rect.x -= self.speed
            else:
                self.way[self.i] -= self.speed
                self.rect.x += self.speed

    def get_pos(self):
        return self.rect.x, self.rect.y

    def awaybar(self):
        self.kill()
