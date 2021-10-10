import pygame
import random
import os


bus_texture = pygame.image.load(os.path.join("images/bus.png"))


class Player:
    def __init__(self, surf):
        self.surf = surf
        self.image = bus_texture
        self.rect = self.image.get_rect()
        self.jump_speed = 3
        self.jump_height = self.jump_speed * 40
        self.start_y = 750-self.rect.height
        self.x = 500-self.rect.width
        self.y = 750-self.rect.height
        self.invert = -1
        self.jumping = False
        self.falling = False

    def jump(self):
        if self.y >= self.start_y:
            self.jumping = True
        elif self.jumping and self.jump_height < 360:
            self.jump_height += self.jump_speed

    def update(self):
        if self.jumping:
            self.y -= self.jump_speed
        if self.y < self.start_y - self.jump_height:
            self.jumping = False
            self.falling = True
            self.jump_height = self.jump_speed * 40
        if self.falling:
            self.y += self.jump_speed/2
        if self.y >= self.start_y:
            self.falling = False


class Ground:
    def __init__(self, surf):
        self.surf = surf
        self.rocks = []
        self.gras = []
        for i in range(100):
            x = [random.randrange(0, 1920, 16), random.randrange(780, 1080, 16)]
            self.rocks.append(x)
        for i in range(200):
            x = [random.randrange(0, 1920, 8), random.randrange(1, 16)]
            self.gras.append(x)

    def draw(self):
        pygame.draw.rect(self.surf, (52, 28, 2), (0, 750, 1920, 330))
        pygame.draw.line(self.surf, (0, 80, 0), (0, 750), (1920, 750), 20)
        for i in self.rocks:
            pygame.draw.rect(self.surf, (40, 20, 2), (i[0], i[1], 16, 16))
        for i in self.gras:
            pygame.draw.rect(self.surf, (0, 80, 0), (i[0], 760, 8, i[1]))

    def update(self):
        for i in self.gras:
            i[0] -= 2
            if i[0] < 0:
                i[0] = 1920
        for i in self.rocks:
            i[0] -= 2
            if i[0] < 0:
                i[0] = 1920


class Block:
    def __init__(self, surf, x=2000):
        self.surf = surf
        self.image = student_textures[random.randrange(0, 2)]
        self.rect = self.image.get_rect()
        self.speed = 2
        self.start_x = x
        self.x = self.start_x
        self.y = 741 - self.rect.height

    def update(self):
        self.x -= self.speed
        self.hit()
        self.score()

    def hit(self):
        if abs((self.x + self.rect.width/2) - (player.x + player.rect.width/2)) <= self.rect.width/2 + player.rect.width/2 - 8:
            if abs((self.y + self.rect.height/2) - (player.y + player.rect.height/2)) <= self.rect.height/2 + player.rect.height/2 - 16:
                player.image = pygame.image.load(os.path.join("images/bus_dead.png"))
                redraw_screen()
                game_over()

    def score(self):
        if abs(self.x - (player.x+64)) == 0:
            global score
            score += 1


def spawn_blocks():
    global spawn_pause
    x = random.randrange(1, 4)
    if spawn_pause == 0:
        for i in range(x):
            block = Block(surface, (1920-64) + i*64)
            block_list.append(block)
            spawn_pause = 800


def timers():
    global spawn_pause
    if spawn_pause > 0:
        spawn_pause -= 1


def init_game():
    pygame.init()
    size = (1920, 1080)
    global surface
    surface = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption("Test 1!")
    global clock
    clock = pygame.time.Clock()
    global ground
    ground = Ground(surface)
    global player
    player = Player(surface)
    global block_list
    block_list = []
    global spawn_pause
    spawn_pause = 0
    global score
    score = 0
    global font
    font = pygame.font.SysFont("Palatino", 48)
    student1_texture = pygame.image.load(os.path.join("images/student1.png"))
    student2_texture = pygame.image.load(os.path.join("images/student2.png"))
    global student_textures
    student_textures = [student1_texture, student2_texture]
    game()


def handle_events():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.jump()

    return run


def update_game_state():
    clock.tick(600)
    player.update()
    ground.update()
    spawn_blocks()
    for i in block_list:
        i.update()
    timers()


def redraw_screen():
    surface.fill((135, 206, 235))
    surface.blit(player.image, (int(player.x), int(player.y)))
    for i in block_list:
        surface.blit(i.image, (int(i.x), int(i.y)))
    ground.draw()
    text = font.render(f"Score: {score}", True, (255,255,255))
    surface.blit(text, (100, 100))
    pygame.display.update()


def game():
    global running
    running = True
    while running:
        running = handle_events()
        update_game_state()
        redraw_screen()


def game_over():
    wait = True
    run = True
    text_s = font.render(f"Press ESCAPE to QUIT", True, (255,255,255))
    text = font.render(f"Press ENTER to RESTART", True, (255,255,255))
    surface.blit(text, (1920//2 - 180, 1080//2))
    surface.blit(text_s, (1920//2 - 160, 1080//2 - 50))
    while wait:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    wait = False
                    global running
                    running = False
                if event.key == pygame.K_RETURN:
                    wait = False
    if run:
        init_game()


# main
def start():
    init_game()
