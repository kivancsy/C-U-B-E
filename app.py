import os
import time
import math

WIDTH = 80
HEIGHT = 40

CUBE_SIZE = 10

buffer = [" "] * (WIDTH * HEIGHT)


def plot(x, y, char="*"):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        buffer[y * WIDTH + x] = char


def project(x, y, z, A, B):
    x2 = x
    y2 = y * math.cos(A) - z * math.sin(A)
    z2 = y * math.sin(A) + z * math.cos(A)

    x3 = x2 * math.cos(B) + z2 * math.sin(B)
    y3 = y2
    z3 = -x2 * math.sin(B) + z2 * math.cos(B)

    f = 30 / (z3 + 40)
    screen_x = int(WIDTH / 2 + x3 * f)
    screen_y = int(HEIGHT / 2 + y3 * f)

    return screen_x, screen_y


cube_points = [
    (-CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE),
    (CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE),
    (CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE),
    (-CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE),
    (-CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE),
    (CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE),
    (CUBE_SIZE, CUBE_SIZE, CUBE_SIZE),
    (-CUBE_SIZE, CUBE_SIZE, CUBE_SIZE),
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return
    x_step = dx / steps
    y_step = dy / steps
    x, y = x1, y1
    for _ in range(steps):
        plot(int(x), int(y), "*")
        x += x_step
        y += y_step


A = 0
B = 0

while True:
    buffer = [" "] * (WIDTH * HEIGHT)

    projected = []
    for (x, y, z) in cube_points:
        px, py = project(x, y, z, A, B)
        projected.append((px, py))
        plot(px, py, "@")

    for (a, b) in edges:
        x1, y1 = projected[a]
        x2, y2 = projected[b]
        draw_line(x1, y1, x2, y2)

    os.system("clear")

    for i in range(HEIGHT):
        print("".join(buffer[i * WIDTH: (i + 1) * WIDTH]))

    A += 0.05
    B += 0.03

    time.sleep(0.02)
