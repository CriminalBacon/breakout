import pygame
from brick import Brick

BRICK_WIDTH = 80
BRICK_HEIGHT = 30

class Level:
    def __init__(self):
        self.brick_group = pygame.sprite.Group()


    def add_row(self, x, y, color, count):
        for i in range(count):
            brick = Brick(color, BRICK_WIDTH, BRICK_HEIGHT)
            brick.rect.x = x + i * 100
            brick.rect.y = y
            self.brick_group.add(brick)


