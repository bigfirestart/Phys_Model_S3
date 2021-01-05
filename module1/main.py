import pygame
from module1.settings.window import Window
from module1.settings.colors import Color
from phys_calc import find_freq
import math


window = Window()

# Изначельные параметры
stick_len = 300
ball_radius = 50
ball_m_per_r_unit = 0.2
stick_m_per_l_unit = 1

stick_m = stick_len/100 * stick_m_per_l_unit
ball_m = ball_radius/100 * ball_m_per_r_unit

freq = find_freq(m1=stick_m, m2=ball_m, L=stick_len/100, R=ball_radius/100)
T = 1/freq

max_degree = 180
degree = 0
move_sign = +1
global_diff = 0
ball_x_0 = window.WIDTH / 2+5
ball_y_0 = 50+10+stick_len

while True:
    if not window.loop():
        break

    if degree > max_degree:
        move_sign = -1
    if degree < 180 - max_degree:
        move_sign = + 1
    if max_degree > 90:
        degree += 1 * move_sign

    delta_x = math.cos(math.radians(degree)) * stick_len
    delta_y = stick_len - math.sin(math.radians(degree)) * stick_len
    ball_x = ball_x_0 + delta_x
    ball_y = ball_y_0 - delta_y

    #print(degree, ball_x, ball_y)

    # базовая установка
    pygame.draw.rect(window.screen, Color.BLACK.value, (window.WIDTH/2-100, 50, 200, 30))

    # груз
    pygame.draw.circle(window.screen, Color.RED.value, (ball_x, ball_y), ball_radius)

    # стержень
    pygame.draw.line(window.screen, Color.BLUE.value, (window.WIDTH / 2, 50 + 10), (ball_x, ball_y), 10)

    # крепление штатива
    pygame.draw.circle(window.screen, Color.WHITE.value, (window.WIDTH / 2, 50 + 10), 5)

    # крепление груза
    pygame.draw.circle(window.screen, Color.WHITE.value, (ball_x, ball_y), 5)

    pygame.time.delay(round((T*1000-2000)/360))
    window.update()


pygame.quit()
