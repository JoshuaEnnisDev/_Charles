import pgzrun
import pygame
from random import randint, choice
from pgzhelper import Actor

WIDTH = 1000
HEIGHT = 800
cookies = []
points = 0
CHARLIE_GREEN = (17, 228, 45)
images = ["bat", "bee", "fishgreen", "flyfly1", "piranha"]

pygame.mouse.set_cursor(pygame.cursors.broken_x)

for i in range(100):
    cookie = Actor("bat", center=(WIDTH // 2, HEIGHT // 2))
    cookie.angle = randint(0, 360)
    cookies.append(cookie)


def draw():
    global points
    screen.fill(CHARLIE_GREEN)
    screen.draw.text(f"Points: {points}", (100, 100))
    for cookie in cookies:
        cookie.draw()


def on_mouse_down(pos):
    global points
    for cookie in cookies:
        if cookie.collidepoint(pos):
            points += 1
            cookies.remove(cookie)


def update():
    for cookie in cookies:
        cookie.move_forward(3)
        cookie.image = choice(images)
        if cookie.x < 10 or cookie. x > WIDTH - 40 or cookie.y < 10 or cookie.y > HEIGHT + 10:
            cookie.angle += randint(90, 270)
            cookie.pos = (randint(50, WIDTH - 50), randint(50, HEIGHT + 50))


pgzrun.go()
