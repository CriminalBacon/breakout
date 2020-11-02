# imports
import pygame
from paddle import Paddle
from ball import Ball
from level import Level

pygame.init()


# Define colors
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

score = 0
lives = 3

# Open new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("B R E A K O U T")


# List that contains all the sprites
all_sprites_list = pygame.sprite.Group()

# create paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# create ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# create bricks
all_bricks = pygame.sprite.Group()

level_one = Level()
level_one.add_row(60, 60, RED, 7)
level_one.add_row(60, 100, ORANGE, 7)
level_one.add_row(60, 140, YELLOW, 7)

# add bricks to sprite Groups
all_sprites_list.add(level_one.brick_group)
all_bricks.add(level_one.brick_group)

# add paddle to sprite list
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# exit variable
carryOn = True

# used to control how fast the screen updates
clock = pygame.time.Clock()

# ---------------- Main Program Loop ----------------
while carryOn:
    # ---- main event loop ----
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            carryOn = False # flag that we are done
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_x: # x key
                carryOn = False

    # check for movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    # ---- Game Logic ----
    all_sprites_list.update()

    # Check if ball is bouncing against wall
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            # Display Game Over message
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            # Stop the game
            carryOn = False

    if ball.rect.y <= 40:
        ball.velocity[1] = -ball.velocity[1]

    # detect collisions between ball and paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # detect collisions between ball an brick
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks)== 0:
            # display level complete
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.time.wait(3000)

            # Stop game
            carryOn = False



    # ---- Drawing Code ----
    # clear the screen
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # Display the score & lives
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    # draw all sprites
    all_sprites_list.draw(screen)

    # ---- Update screen ----
    pygame.display.flip()

    # ---- limit fps
    clock.tick(60)

# exit code
pygame.quit()