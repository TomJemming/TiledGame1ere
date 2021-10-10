import pygame
from math import cos, sin
import time


pygame.init()
screen = pygame.display.set_mode([1920, 1080], pygame.FULLSCREEN)
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ball_x = int(1920 / 2)
        self.ball_y = 300
        self.ball_speed = 10
        self.ball_speed_x = int(cos(45) * self.ball_speed)
        self.ball_speed_y = int(sin(45) * self.ball_speed)

    def check_contact(self):
        if self.ball_x == int(1920 / 2) and self.ball_y == 300:
            time.sleep(2)
        self.ball_x -= self.ball_speed_x
        self.ball_y -= self.ball_speed_y
        if g.player1.player_x < self.ball_x < g.player1.player_x + 50 and g.player1.player_y < self.ball_y < g.player1.player_y + 200:
            self.ball_speed_x = - self.ball_speed_x
        elif g.enemy.enemy_x < self.ball_x < g.enemy.enemy_x + 50 and g.enemy.enemy_y < self.ball_y < g.enemy.enemy_y + 200:
            self.ball_speed_x = - self.ball_speed_x
        elif self.ball_y <= 30 or self.ball_y >= 1050:
            self.ball_speed_y = - self.ball_speed_y

    def reset(self):
        self.ball_x = int(1920 / 2)
        self.ball_y = 300
        self.ball_speed = 10
        self.ball_speed_x = int(cos(45) * self.ball_speed)
        self.ball_speed_y = int(sin(45) * self.ball_speed)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_x = 100
        self.player_y = 300
        self.player_speed = 20
        self.counter_player = 0

    def check_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            if self.player_y < 880:
                self.player_y += self.player_speed
            else:
                pass
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            if self.player_y > 0:
                self.player_y -= self.player_speed
            else:
                pass


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_x = 1800
        self.enemy_y = 300
        self.enemy_speed = 10
        self.counter_enemy = 0

    def move_enemy(self):
        self.enemy_y += self.enemy_speed
        if self.enemy_y >= 780:
            self.enemy_speed = - self.enemy_speed
        elif self.enemy_y <= 0:
            self.enemy_speed = - self.enemy_speed
        else:
            pass


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1920, 1080], pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.start_game()
        self.player1 = None
        self.ball = None
        self.enemy = None
        self.end = False

    def check_quit(self):
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                self.running = False
                self.end = True

    def check_end(self):
        if self.player1.counter_player == 2 or self.enemy.counter_enemy == 2:
            self.running = False

    def end_screen(self):
        if self.player1.counter_player == 2:
            text1 = self.font.render("VICTORY!!!", True, (255, 255, 255))
            screen.blit(text1, (960 - text1.get_width() // 2, 500 - text1.get_height() // 2))
            text2 = self.font.render("Press Escape to quit", True, (255, 255, 255))
            screen.blit(text2, (960 - text2.get_width() // 2, 600 - text2.get_height() // 2))
            pygame.display.flip()
            pygame.display.update()
        elif self.enemy.counter_enemy == 2:
            text1 = self.font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(text1, (960 - text1.get_width() // 2, 500 - text1.get_height() // 2))
            text2 = self.font.render("Press Escape to quit", True, (255, 255, 255))
            screen.blit(text2, (960 - text2.get_width() // 2, 600 - text2.get_height() // 2))
            pygame.display.flip()
            pygame.display.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 20, 1080))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 1920, 20))
        pygame.draw.rect(self.screen, (0, 0, 0), (1900, 0, 20, 1080))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 1060, 1920, 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.player1.player_x, self.player1.player_y, 50, 200))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.enemy.enemy_x, self.enemy.enemy_y, 50, 200))
        pygame.draw.circle(screen, (255, 255, 255), (self.ball.ball_x, self.ball.ball_y), 20, 0)
        text = self.font.render(str(self.player1.counter_player) + "               " + str(self.enemy.counter_enemy), True, (255, 255, 255))
        screen.blit(text, (960 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def start_game(self):
        self.player1 = Player()
        self.enemy = Enemy()
        self.ball = Ball()

    def check_score(self):
        if self.ball.ball_x <= self.player1.player_x:
            self.enemy.counter_enemy += 1
            self.ball.reset()
        elif self.ball.ball_x >= self.enemy.enemy_x + 50:
            self.player1.counter_player += 1
            self.ball.reset()

    def reset(self):
        self.enemy.counter_enemy = 0
        self.player1.counter_player = 0
        self.running = True
        self.end = False


g = Game()


# main
def start():
    g.start_game()
    g.draw()
    while g.running:
        g.check_quit()
        g.player1.check_movement()
        g.enemy.move_enemy()
        g.ball.check_contact()
        g.check_score()
        g.check_end()
        g.draw()

    while not g.end:
        g.end_screen()
        g.check_quit()
    g.reset()
