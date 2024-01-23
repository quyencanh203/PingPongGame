import pygame
import sys
import os

from define import *
from object import *

# Khởi tạo Pygame
pygame.init()

WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pingpong Game")
pygame.display.set_icon(pygame.image.load(PATH_IMAGES + 'icon.png'))

WINDOW_COLOR = COLOR_BLACK  # mau cho cua so screen

# su kien di chuyen


def key_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # su kien click vao dau cheo do (close)
            pygame.quit
            sys.exit()

        if event.type == pygame.KEYDOWN:  # bat cac su kien ban phim

            if event.key == pygame.K_w:
                playerLeft.move_up()
            if event.key == pygame.K_s:
                playerLeft.move_down()


clock = pygame.time.Clock()

while True:
    # pygame.time.delay(100)
    WINDOW_GAME.fill(WINDOW_COLOR)

    # key event
    key_events()

    # ve duong line o giua
    pygame.draw.line(WINDOW_GAME, COLOR_WHITE, (WINDOW_WIDTH/2, 0),
                     (WINDOW_WIDTH/2, WINDOW_HEIGHT), width=LINE_WIDTH)

    # ve player
    playerLeft.showPlayer(WINDOW_GAME)
    playerRight.showPlayer(WINDOW_GAME)

    # ve ball
    ball.showBall(WINDOW_GAME)

    # ball move
    ball.ballMove()

    # xu ly va cham ball player
    if ball.get_rect().colliderect(playerLeft.get_rect()) or ball.get_rect().colliderect(playerRight.get_rect()):
        BALL_VELOCITY[0] *= -1

    playerRight.move_Auto(ball)  # Pass the clock to move_auto

    # update lai giao dien
    pygame.display.update()

    pygame.display.flip()
    # pygame.time.Clock().tick(30)
    clock.tick(30)

pygame.quit()
