import pygame

HEIGHT = 1080
WIDTH = 1920

def start(surf, tx="Test"):
    global screen
    screen = surf
    global font
    font = pygame.font.SysFont("Palatino", 48)
    global playing
    playing = True
    global running
    running = True
    global text
    text = tx
    global play
    play = None
    draw()
    update()


def draw(color1=(255,255,255), color2=(255,255,255)):
    text1 = font.render(text, True, (255, 255, 255))
    screen.blit(text1, (WIDTH//2-(len(text)*7), HEIGHT-200))
    text2 = font.render("No!", True, color1)
    screen.blit(text2, (WIDTH//2+120, HEIGHT-120))
    text3 = font.render("Yes!", True, color2)
    screen.blit(text3, (WIDTH//2-120, HEIGHT-120))
    pygame.display.flip()


def events():
    global playing
    global running
    global play
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if playing:
                playing = False
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                draw(color2=(0,255,255))
                play = 2
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                draw(color1=(0,255,255))
                play = 1
            if event.key == pygame.K_SPACE:
                if play != None:
                    running = False
                    playing = False


def check_play():
    return play


def update():
    while playing:
        events()
