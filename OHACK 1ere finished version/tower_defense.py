import sys
from Sprites import *


class TowerGame:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.font.init()
        self.money = 150
        self.round = 1
        self.health = 20
        self.ennemys = []
        self.delay = 30
        self.updated = 0
        self.difficulty = 1
        self.pause = 0
        self.costt1 = 50
        self.costt2 = 400
        self.costt3 = 900
        self.costt4 = 1600
        self.costt5 = 1000
        self.canquit = 0
        self.ending = True
        self.k_ennemys = 0
        self.all_sprites = pg.sprite.Group()
        self.towergroup = pg.sprite.Group()
        self.ennemylist = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.canspawn = 0
        self.spawncoords = [0, 0]
        self.spawnplusx = 0
        self.spawnplusy = 0
        self.playing = True

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            if self.canquit == 0:
                self.draw()
                self.events()
                self.update()
            else:
                self.playing = False

    def checkforennemyormoney(self):
        for j in self.towergroup:
            j.check_for_ennemmy_and_money(self.ennemylist)

    def quit(self):
        self.playing = False

    def update(self):
        if self.pause != 0:
            if self.health <= 0:
                self.ending_screen()
            self.all_sprites.update()
            self.spawn()

    def spawn(self):
        if len(self.ennemylist) == 0:
            if len(self.ennemys) == 0:
                self.round += 1
                self.rounds()
        if len(self.ennemylist) != 0 or len(self.ennemys) != 0:
            if self.updated % self.delay == 0:
                if 10 < self.round < 40:
                    self.delay = random.randint(20, 30)
                if 40 <= self.round < 80:
                    self.delay = random.randint(10, 20)
                if 80 <= self.round:
                    self.delay = random.randint(1, 10)
                try:
                    x = random.choice(self.ennemys)
                    self.ennemys.remove(x)
                    if x == "G":
                        G(self)
                    if x == "E":
                        E(self)
                    if x == "D":
                        D(self)
                    if x == "C":
                        C(self)
                    if x == "B":
                        B(self)
                except IndexError:
                        pass
        self.updated += 1

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY, (0, y), (WIDTH, y))

    def draw(self):
        pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT))
        background_image = pg.image.load("Images\Map.png").convert()
        self.screen.blit(background_image, [0, 0])
        self.all_sprites.draw(self.screen)
        self.drawtext()
        pg.draw.rect(self.screen, BLUE, (1281, 915, 140, 50), 3)
        pg.draw.rect(self.screen, BLUE, (1421, 915, 140, 50), 3)
        pg.draw.rect(self.screen, RED, (1875, 996, 40, 25), 3)
        if self.difficulty != 3:
            pg.draw.rect(self.screen, RED, (1295, 395, 305, 35), 3)
        if self.pause != 0:
            self.checkforennemyormoney()
        pos = pg.mouse.get_pos()
        if pos[0] < TILESIZE*39 and pos[1] < TILESIZE*32 and self.canspawn == 0:
            pg.draw.rect(self.screen, BLUE, (pos[0]-pos[0] % TILESIZE, pos[1]-pos[1] % TILESIZE, TILESIZE, TILESIZE), 1)
        self.spawntower()
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                for i in range(140):
                    for j in range(50):
                        if pos[0] == 1281+i and pos[1] == 915+j:
                            self.pause = 0
                        if pos[0] == 1421+i and pos[1] == 915+j:
                            self.pause = 1
                for i in range(40):
                    for j in range(25):
                        if pos[0] == 1875+i and pos[1] == 996+j:
                            if self.canquit == 1:
                                self.ending = False
                                self.quit()
                            self.ending_screen()
                if self.health > 0:
                    for i in range(70):
                        for j in range(25):
                            if pos[0] == 1775+i and pos[1] == 996+j:
                                if self.canquit == 1:
                                    self.canquit = 0
                                    self.run()
                            if pos[0] == 1675+i and pos[1] == 996+j:
                                if self.canquit == 1:
                                    tg = TowerGame()
                                    tg.start_screen()
                                    tg.run()
                else:
                    for i in range(70):
                        for j in range(25):
                            if pos[0] == 1775+i and pos[1] == 996+j:
                                if self.canquit == 1:
                                    tg = TowerGame()
                                    tg.start_screen()
                                    tg.run()
                if self.difficulty != 3:
                    if self.money >= 40000:
                        for i in range(305):
                            for j in range(35):
                                if pos[0] == 1295+i and pos[1] == 395+j:
                                    for _ in range(5):
                                        for e in self.ennemylist:
                                            Healthbar.awaybar(e.bar)
                                            e.kill()
                                    self.money -= 40000
                if pg.mouse.get_pressed() == (True, False, False):
                    if pos[0] < TILESIZE*39 and pos[1] < TILESIZE*32:
                        if self.canspawn == 1:
                            self.canspawn = 0
                            if not self.check_for_tower():
                                for i in range(TILESIZE):
                                    for j in range(TILESIZE):
                                        if self.spawncoords[0]+i == pos[0] and self.spawncoords[1]+j == pos[1]:
                                            if self.money >= self.costt1:
                                                Language(self, (self.spawncoords[0]-self.spawnplusx)//TILESIZE, (self.spawncoords[1]-self.spawnplusy)//TILESIZE)
                                                self.money -= self.costt1
                                        if self.spawncoords[0]+32+i == pos[0] and self.spawncoords[1]+j == pos[1]:
                                            if self.money >= self.costt2:
                                                Chemie(self, (self.spawncoords[0]-self.spawnplusx)//TILESIZE, (self.spawncoords[1]-self.spawnplusy)//TILESIZE)
                                                self.money -= self.costt2
                                        if self.spawncoords[0]+64+i == pos[0] and self.spawncoords[1]+j == pos[1]:
                                            if self.money >= self.costt3:
                                                Physik(self, (self.spawncoords[0]-self.spawnplusx)//TILESIZE, (self.spawncoords[1]-self.spawnplusy)//TILESIZE)
                                                self.money -= self.costt3
                                        if self.spawncoords[0]+96+i == pos[0] and self.spawncoords[1]+j == pos[1]:
                                            if self.money >= self.costt4:
                                                Mathe(self, (self.spawncoords[0]-self.spawnplusx)//TILESIZE, (self.spawncoords[1]-self.spawnplusy)//TILESIZE)
                                                self.money -= self.costt4
                                        if self.spawncoords[0]+128+i == pos[0] and self.spawncoords[1]+j == pos[1]:
                                            if self.money >= self.costt5:
                                                Economie(self, (self.spawncoords[0]-self.spawnplusx)//TILESIZE, (self.spawncoords[1]-self.spawnplusy)//TILESIZE)
                                                self.money -= self.costt5
                        else:
                            self.canspawn = 1
                            if TILESIZE < pos[0] < TILESIZE*2 and TILESIZE < pos[1] < TILESIZE*32:
                                self.spawnplusx = -32
                                self.spawnplusy = -32
                            elif pos[0] < TILESIZE and TILESIZE < pos[1] < TILESIZE*32:
                                self.spawnplusx = 0
                                self.spawnplusy = -32
                            elif TILESIZE*2 < pos[0] < TILESIZE*37 and pos[1] < TILESIZE:
                                self.spawnplusx = -64
                                self.spawnplusy = 32
                            elif pos[0] < TILESIZE and pos[1] < TILESIZE:
                                self.spawnplusx = 0
                                self.spawnplusy = 32
                            elif TILESIZE < pos[0]< TILESIZE * 2 and pos[1] < TILESIZE:
                                self.spawnplusx = -32
                                self.spawnplusy = 32
                            elif TILESIZE*37 < pos[0] < TILESIZE*38 and TILESIZE < pos[1] < TILESIZE*32:
                                self.spawnplusx = -96
                                self.spawnplusy = -32
                            elif TILESIZE*38 < pos[0] < TILESIZE*39 and TILESIZE < pos[1] < TILESIZE*32:
                                self.spawnplusx = -128
                                self.spawnplusy = -32
                            elif TILESIZE*37 < pos[0] < TILESIZE*38 and pos[1] < TILESIZE:
                                self.spawnplusx = -96
                                self.spawnplusy = 32
                            elif TILESIZE*38 < pos[0] < TILESIZE*39 and pos[1] < TILESIZE:
                                self.spawnplusx = -128
                                self.spawnplusy = 32
                            else:
                                self.spawnplusx = -64
                                self.spawnplusy = -32
                            self.spawncoords = [pos[0]-pos[0] % TILESIZE + self.spawnplusx, pos[1]-pos[1] % TILESIZE + self.spawnplusy]
                if pg.mouse.get_pressed() == (False, False, True):
                    for tw in self.towergroup:
                        pos = pg.mouse.get_pos()
                        t = tw.delete((pos[0]-pos[0] % TILESIZE, pos[1]-pos[1] % TILESIZE))
                        if t == "t1":
                            self.money += self.costt1*9/10
                        if t == "t2":
                            self.money += self.costt2*9/10
                        if t == "t3":
                            self.money += self.costt3*9/10
                        if t == "t4":
                            self.money += self.costt4*9/10
                        if t == "t5":
                            self.money += self.costt5*9/10

    def drawtext(self):
        self.printtext(f"Round: {self.round}", 1300, 10, 48, GREEN)
        self.printtext(f"Health: {self.health}", 1650, 10, 48, GREEN)
        self.printtext(f"Money: {self.money:.0f}", 1300, 100, 32)
        self.printtext(f"Language cost: {self.costt1}", 1300, 150)
        self.printtext(f"Chemistry cost: {self.costt2}", 1300, 180)
        self.printtext(f"Physics cost: {self.costt3}", 1300, 210)
        self.printtext(f"Math cost: {self.costt4}", 1300, 240)
        self.printtext(f"Economy cost: {self.costt5}", 1300, 270)
        self.printtext("Pause", 1301, 920, 32, BLUE)
        self.printtext("Play", 1441, 920, 32, BLUE)
        self.printtext("Exit", 1880, 1000, 16, RED)
        self.printtext(f"Ennemys currently onscreen: {len(self.ennemylist)}", 1300, 970)
        self.printtext(f"Ennemys killed so far: {self.k_ennemys}", 1300, 990)
        if self.difficulty != 3:
            self.printtext("Kill all ennemys cost: 40000", 1300, 400, color=RED)
        if self.difficulty == 1:
            self.printtext("Difficulty: Easy", 1600, 100, 32)
        elif self.difficulty == 2:
            self.printtext("Difficulty: Medium", 1600, 100, 32)
        else:
            self.printtext("Difficulty: Hard", 1600, 100, 32)

    def rounds(self):
        if self.round == 1:
            for _ in range(10):
                self.ennemys.append("G")
        if self.round == 2:
            for _ in range(15):
                self.ennemys.append("G")
        if self.round == 3:
            for _ in range(8):
                self.ennemys.append("E")
        if self.round == 4:
            for _ in range(4):
                self.ennemys.append("E")
            for _ in range(8):
                self.ennemys.append("G")
        if self.round == 5:
            for _ in range(10):
                self.ennemys.append("E")
            for _ in range(10):
                self.ennemys.append("G")
        if self.round == 6:
            for _ in range(5):
                self.ennemys.append("D")
        if self.round == 7:
            for _ in range(10):
                self.ennemys.append("G")
            for _ in range(4):
                self.ennemys.append("D")
        if self.round == 8:
            for _ in range(5):
                self.ennemys.append("E")
            for _ in range(8):
                self.ennemys.append("G")
            for _ in range(4):
                self.ennemys.append("D")
        if self.round == 9:
            for _ in range(10):
                self.ennemys.append("E")
            for _ in range(12):
                self.ennemys.append("G")
            for _ in range(8):
                self.ennemys.append("D")
        if self.round == 10:
            for _ in range(14):
                self.ennemys.append("E")
            for _ in range(8):
                self.ennemys.append("D")
        if 10 < self.round < 40:
            for _ in range(int(self.round*2.5)):
                x = random.randint(1, 3)
                if x == 1:
                    self.ennemys.append("G")
                if x == 2:
                    self.ennemys.append("E")
                else:
                    self.ennemys.append("D")
        if self.round == 40:
            for i in range(10):
                self.ennemys.append("C")
        if 40 < self.round < 80:
            for i in range(int(self.round*3.5)):
                    x = random.randint(2, 4)
                    if x == 2:
                        self.ennemys.append("E")
                    if x == 3:
                        self.ennemys.append("D")
                    else:
                        self.ennemys.append("C")
        if self.round == 80:
            for _ in range(10):
                self.ennemys.append("B")
        if self.round > 80:
            for _ in range(int(self.round*4.5)):
                    x = random.randint(3, 5)
                    if x == 3:
                        self.ennemys.append("D")
                    if x == 4:
                        self.ennemys.append("C")
                    else:
                        self.ennemys.append("B")

    def check_for_tower(self):
        for tower in self.towergroup:
            coords = (self.spawncoords[0]-self.spawnplusx, self.spawncoords[1]-self.spawnplusy)
            t = tower.get_pos()
            if coords[0] - coords[0] % TILESIZE + 1 == t[0] and coords[1]-coords[1] % TILESIZE + 1 == t[1]:
                return True
        return False

    def spawntower(self):
        if self.canspawn == 1:
            image1 = pg.image.load('Images\Language.png').convert_alpha()
            self.screen.blit(image1, [self.spawncoords[0], self.spawncoords[1]])
            image2 = pg.image.load('Images\Chemie.png').convert_alpha()
            self.screen.blit(image2, [self.spawncoords[0]+32, self.spawncoords[1]])
            image3 = pg.image.load('Images\Physics.png').convert_alpha()
            self.screen.blit(image3, [self.spawncoords[0]+64, self.spawncoords[1]])
            image4 = pg.image.load('Images\Mathe.png').convert_alpha()
            self.screen.blit(image4, [self.spawncoords[0]+96, self.spawncoords[1]])
            image5 = pg.image.load('Images\Economie.png').convert_alpha()
            self.screen.blit(image5, [self.spawncoords[0]+128, self.spawncoords[1]])
            pg.draw.circle(self.screen, LIGHTGRAY, (self.spawncoords[0]-self.spawnplusx+16, self.spawncoords[1]-self.spawnplusy+16), 100, 3)
            if self.money >= self.costt1:
                pg.draw.rect(self.screen, GREEN, (self.spawncoords[0], self.spawncoords[1], TILESIZE, TILESIZE), 1)
            else:
                pg.draw.rect(self.screen, RED, (self.spawncoords[0], self.spawncoords[1], TILESIZE, TILESIZE), 1)
            if self.money >= self.costt2:
                pg.draw.rect(self.screen, GREEN, (self.spawncoords[0]+32, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            else:
                pg.draw.rect(self.screen, RED, (self.spawncoords[0]+32, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            if self.money >= self.costt3:
                pg.draw.rect(self.screen, GREEN, (self.spawncoords[0]+64, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            else:
                pg.draw.rect(self.screen, RED, (self.spawncoords[0]+64, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            if self.money >= self.costt4:
                pg.draw.rect(self.screen, GREEN, (self.spawncoords[0]+96, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            else:
                pg.draw.rect(self.screen, RED, (self.spawncoords[0]+96, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            if self.money >= self.costt5:
                pg.draw.rect(self.screen, GREEN, (self.spawncoords[0]+128, self.spawncoords[1], TILESIZE, TILESIZE), 1)
            else:
                pg.draw.rect(self.screen, RED, (self.spawncoords[0]+128, self.spawncoords[1], TILESIZE, TILESIZE), 1)

    def printtext(self, text, x, y, size=24, color=WHITE):
        font = pg.font.Font('C:\Windows\Fonts\Arial.ttf', size)
        textt = font.render(text, True, color)
        textRect = textt.get_rect()
        textRect.topleft = (x, y)
        self.screen.blit(textt, textRect)

    def start_screen(self):
        self.starting = True
        while self.starting:
            pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT))
            self.printtext("School", 50, 100, 150, CYAN)
            self.printtext("Defense", 50, 250, 150, CYAN)
            self.printtext("Easy", 1000, 200, 100, LIGHTGRAY)
            pg.draw.rect(self.screen, BLUE, (998, 198, 240, 120), 2)
            self.printtext("Medium", 1000, 400, 100, LIGHTGRAY)
            pg.draw.rect(self.screen, BLUE, (998, 398, 360, 120), 2)
            self.printtext("Hard", 1000, 600, 100, LIGHTGRAY)
            pg.draw.rect(self.screen, BLUE, (998, 598, 240, 120), 2)
            self.printtext("Exit", 1880, 1000, 16, RED)
            pg.draw.rect(self.screen, RED, (1875, 996, 40, 25), 3)
            self.starting_events()
            pg.display.flip()
        if self.difficulty == 1:
            self.health = 200
        if self.difficulty == 3:
            self.money = 200
            self.costt1 = 100
            self.costt2 = 600
            self.costt3 = 1200
            self.costt4 = 2500
            self.costt5 = 2000
            self.health = 50

    def starting_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                for i in range(240):
                    for j in range(120):
                        if pos[0] == 998+i and pos[1] == 198+j:
                            self.difficulty = 1
                            self.starting = 0
                for i in range(360):
                    for j in range(120):
                        if pos[0] == 998+i and pos[1] == 398+j:
                            self.difficulty = 2
                            self.starting = 0
                for i in range(240):
                    for j in range(120):
                        if pos[0] == 998+i and pos[1] == 598+j:
                            self.difficulty = 3
                            self.starting = 0
                for i in range(40):
                    for j in range(25):
                        if pos[0] == 1875+i and pos[1] == 996+j:
                            self.starting = 0
                            self.quit()

    def ending_screen(self):
        pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT))
        self.printtext("Exit", 1880, 1000, 16, RED)
        pg.draw.rect(self.screen, RED, (1875, 996, 40, 25), 3)
        if self.health > 0:
            self.printtext("Resume", 1780, 1000, 16, GREEN)
            pg.draw.rect(self.screen, GREEN, (1775, 996, 70, 25), 3)
            self.printtext("Restart", 1680, 1000, 16, BLUE)
            pg.draw.rect(self.screen, BLUE, (1675, 996, 70, 25), 3)
        else:
            self.printtext("Restart", 1780, 1000, 16, BLUE)
            pg.draw.rect(self.screen, BLUE, (1775, 996, 70, 25), 3)

        if self.difficulty == 1:
            with open("Modules/highscoreE.txt", "r+") as hisc:
                hi = hisc.read(10)
            if not hi:
                hi = '0'
            with open("Modules/highscoreE.txt", "w+") as hisc:
                self.printtext(f"Highscore on Easy: {hi}", 100, 900, 48, LIGHTGRAY)
                if self.round > int(hi):
                    hisc.write(str(self.round))
                    self.printtext(f"New Highscore: {self.round}", 700, 900, 32, LIGHTGRAY)
                else:
                    hisc.write(hi)
        if self.difficulty == 2:
            with open("Modules/highscoreM.txt", "r+") as hisc:
                hi = hisc.read(10)
            if not hi:
                hi = '0'
            with open("Modules/highscoreM.txt", "w+") as hisc:
                self.printtext(f"Highscore on Medium: {hi}", 100, 900, 48, LIGHTGRAY)
                if self.round > int(hi):
                    hisc.write(str(self.round))
                    self.printtext(f"New Highscore: {self.round}", 800, 900, 48, LIGHTGRAY)
                else:
                    hisc.write(hi)
        if self.difficulty == 3:
            with open("Modules/highscoreH.txt", "r+") as hisc:
                hi = hisc.read(10)
            if not hi:
                hi = '0'
            with open("Modules/highscoreH.txt", "w+") as hisc:
                self.printtext(f"Highscore on Hard: {hi}", 100, 900, 48, LIGHTGRAY)
                if self.round > int(hi):
                    hisc.write(str(self.round))
                    self.printtext(f"New Highscore: {self.round}", 700, 900, 48, LIGHTGRAY)
                else:
                    hisc.write(hi)
        if self.health <= 0:
            self.printtext(f"You lost on round: {self.round}", 100, 100, 112, CYAN)
        else:
            self.printtext(f"You stopped on round: {self.round}", 100, 100, 112, CYAN)
            self.printtext("but you can resume", 100, 250, 112, CYAN)
        while self.ending:
            self.canquit = 1
            self.events()
            pg.display.flip()

def start():
    g = TowerGame()
    g.start_screen()
    g.run()

if "__main__" == __name__:
    start()
