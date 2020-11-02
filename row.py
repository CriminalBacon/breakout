import pygame
from brick import Brick

WIDTH = 80
HEIGHT = 30

class Row:
    def __init__(self, x, y, color, count):
        self.x = x
        self.y = y
        self.color = color
        self.count = count
        self.bricks = pygame.sprite.Group()

    def create(self):
        for i in range(self.count):
            brick = Brick(self.color, WIDTH, HEIGHT)
            brick.rect.x = self.x + i * 100
            brick.rect.y = self.y
            self.bricks.add(brick)

