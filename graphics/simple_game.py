import pygame
import sys
from pygame.color import THECOLORS
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Cannon:
    def __init__(self):
        self.color = (0, 255, 0)
        self.speed = 10
        self.v_1 = [WIDTH / 2 - 25, HEIGHT]
        self.v_2 = [WIDTH / 2, HEIGHT - 50]
        self.v_3 = [WIDTH / 2 + 25, HEIGHT]
        self.surface = (self.v_1, self.v_2, self.v_3)

    def draw(self):
        pygame.draw.polygon(screen, self.color, self.surface)


class Bullet:
    def __init__(self):
        self.center = [cannon.v_2[0], cannon.v_2[1]]
        self.radius = 5
        self.color = (255, 0, 0)
        self.speed = 20

    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def move(self):
        self.center[1] -= self.speed


class Target:
    def __init__(self):
        self.color = (0, 0, 255)
        self.speed = 5
        self.rect = pygame.Rect((0, 0), (50, 25))

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right >= WIDTH:
            self.speed = -self.speed
        elif self.rect.left <= 0:
            self.speed = -self.speed

colors = list(THECOLORS.values())

def get_random_color():
    random_color = random.choice(colors)
    return random_color if random_color != THECOLORS['black'] else get_random_color()

cannon = Cannon()
target = Target()
bullet = Bullet()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(THECOLORS['black'])

    target.move()
    bullet.move()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if cannon.v_3[0] >= WIDTH:
                continue
            for v in cannon.surface:
                v[0] += cannon.speed
        elif event.key == pygame.K_LEFT:
            if cannon.v_1[0] <= 0:
                continue
            for v in cannon.surface:
                v[0] -= cannon.speed

    if bullet.center[1] <= 0:
        bullet.center[1] = cannon.v_2[1]
        bullet.center[0] = cannon.v_2[0]
    elif target.rect.collidepoint(bullet.center[0], bullet.center[1]):
        bullet.center[1] = cannon.v_2[1]
        bullet.center[0] = cannon.v_2[0]
        target.color = get_random_color()

    cannon.draw()
    target.draw()
    bullet.draw()

    pygame.display.update()
    pygame.time.wait(30)
