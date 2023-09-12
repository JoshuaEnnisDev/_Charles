from pgzrun import go

WIDTH = 1000
HEIGHT = 400

kemo = Actor("dino")
kemo.x = 100
kemo.bottom = 400


def draw():
    kemo.draw()


go()
