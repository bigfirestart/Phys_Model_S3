import pygame

from module1.settings.window import Window
from module1.settings.colors import Color
import math
window = Window()

stick_len = 300
ball_radius = 50

rot = 0
rot_speed = 2

stick = pygame.Surface((60, 60), pygame.SRCALPHA)

ball_x_0 = window.WIDTH / 2+5
ball_y_0 = 50+10+stick_len

max_degree = 180
degree = 0
go_left = True
go_right = False

while True:

    if not window.loop():
        break


    max_degree -= 0.1

    if go_left:
        if degree < max_degree:
            degree += 1
        elif degree > max_degree:
            go_left = False
            go_right = True

        delta_x = math.cos(math.radians(degree)) * stick_len
        delta_y = stick_len - math.sin(math.radians(degree)) * stick_len
        ball_x = ball_x_0 + delta_x
        ball_y = ball_y_0 - delta_y

    if go_right:
        if degree > 180-max_degree:
            degree -= 1
        elif degree < 180-max_degree:
            go_left = True
            go_right = False

        delta_x = math.cos(math.radians(degree)) * stick_len
        delta_y = stick_len - math.sin(math.radians(degree)) * stick_len
        ball_x = ball_x_0 + delta_x
        ball_y = ball_y_0 - delta_y

    print(degree, ball_x, ball_y)
    # базовая установка
    pygame.draw.rect(window.screen, Color.BLACK.value, (window.WIDTH/2-100, 50, 200, 30))

    # груз
    pygame.draw.circle(window.screen, Color.RED.value, (ball_x, ball_y) , ball_radius)

    # стержень
    pygame.draw.line(window.screen, Color.BLUE.value, (window.WIDTH / 2, 50 + 10), (ball_x, ball_y), 10)

    # крепление штатива
    pygame.draw.circle(window.screen, Color.WHITE.value, (window.WIDTH / 2 + 5, 50 + 10), 5)

    pygame.draw.circle(window.screen, Color.WHITE.value, (ball_x, ball_y) , 5)

    pygame.time.delay(10)

    window.update()



