import pgzrun
from random import randint
from pgzhelper import Actor

WIDTH = 1000
HEIGHT = 800
cookies = []
points = 0

for i in range(10000):
    cookie = Actor("bat")
    cookie.angle = randint(0, 360)
    cookies.append(cookie)


def draw():
    global points
    screen.clear()
    screen.draw.text(f"Points: {points}", (100, 100))
    for cookie in cookies:
        cookie.draw()


def on_mouse_down(pos):
    global points
    for cookie in cookies:
        if cookie.collidepoint(pos):
            points += 1


def update():
    for cookie in cookies:
        cookie.move_forward(3)
        if cookie.x < 0 or cookie. x > HEIGHT or cookie.y < 0 or cookie.y > HEIGHT:
            cookie.angle += randint(90, 270)
pgzrun.go()