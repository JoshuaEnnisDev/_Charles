from pgzrun import go

WIDTH = 1000
HEIGHT = 400

dino = Actor("dino")
dino.x = 100
dino.bottom = 400


def draw():
    screen.fill("blue")
    dino.draw()


def update():
    dino.x = dino.x + 3


go()
