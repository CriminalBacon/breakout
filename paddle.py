import pygame
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    # derives from "Sprite"

    def __init__(self, color, width, height):
        # call parent class (Sprite) constructor
        super().__init__()

        # Pass color and it's x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # fetch the rectangle object that has the dimensions ofr the image
        self.rect = self.image.get_rect()

    def move_left(self, pixels):
        self.rect.x -= pixels

        # check if are going off screen
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pixels):
        self.rect.x += pixels

        # check if going off screen
        if self.rect.x > 700:
            self.rect.x = 700
