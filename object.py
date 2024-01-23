import pygame
import random
from define import *


class object():
    x = 0
    y = 0
    color = ''

    def __init__(self, color, x, y) -> None:
        self.x = x
        self.y = y
        self.color = color


class Player(object):
    def __init__(self, color, x, y) -> None:
        super().__init__(color, x, y)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def showPlayer(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))

    def move_up(self):
        self.y -= PLAYER_VELOCITY
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += PLAYER_VELOCITY
        if self.y > WINDOW_HEIGHT-PLAYER_HEIGHT:
            self.y = WINDOW_HEIGHT-PLAYER_HEIGHT

    def move_Auto(self, ball):

        target_y = ball.y - PLAYER_HEIGHT / 2  # Điều chỉnh tâm của trình phát

        # Tính hướng và khoảng cách di chuyển
        direction = 1 if target_y > self.y else -1
        distance = abs(target_y - self.y)

        self.y += direction * PLAYER_VELOCITY

        # Di chuyển với vận tốc không đổi
        steps = int(distance / PLAYER_VELOCITY)
        for _ in range(steps):
            self.y += direction * PLAYER_VELOCITY

        if target_y < 0:
            target_y = 0
        elif target_y > WINDOW_HEIGHT-PLAYER_HEIGHT:
            target_y = WINDOW_HEIGHT-PLAYER_HEIGHT

        # Di chuyển đến vị trí mục tiêu chính xác (cập nhập vị trí)
        self.y = target_y


class Ball(object):

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BALL_SIZE, BALL_SIZE)

    def showBall(self, surface):
        pygame.draw.ellipse(surface, self.color,
                            (self.x, self.y, BALL_SIZE, BALL_SIZE))

    def ballMove(self):
        self.x = self.x + BALL_VELOCITY[0]
        self.y = self.y + BALL_VELOCITY[1]
        # va cham tren duoi
        if self.y <= 0 or self.y >= WINDOW_HEIGHT-BALL_SIZE:
            BALL_VELOCITY[1] *= -1
        # va cham trai phai
        if self.x <= 0 or self.x >= WINDOW_WIDTH-BALL_SIZE:
            # BALL_VELOCITY[0] *= -1
            self.x = WINDOW_WIDTH/2 - BALL_SIZE/2
            self.y = WINDOW_HEIGHT/2-BALL_SIZE/2
            BALL_VELOCITY[0] *= random.choice((1, -1))
            BALL_VELOCITY[1] *= random.choice((1, -1))


ball = Ball(COLOR_YELLOW, WINDOW_WIDTH/2 -
            BALL_SIZE/2, WINDOW_HEIGHT/2-BALL_SIZE/2)

# init player
playerLeft = Player(COLOR_WHITE, 0, WINDOW_HEIGHT/2-PLAYER_HEIGHT/2)
playerRight = Player(COLOR_WHITE, WINDOW_WIDTH-PLAYER_WIDTH,
                     WINDOW_HEIGHT/2-PLAYER_HEIGHT/2)
