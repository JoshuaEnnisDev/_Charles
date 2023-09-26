from pgzrun import go

WIDTH = 1000
HEIGHT = 400

dino = Actor("dino")
dino.x = 100
dino.bottom = 400

cactus = Actor("cactus")
cactus.x = 1100
cactus.bottom = 400


def draw():
    screen.fill("teal")
    dino.draw()
    cactus.draw()


def on_key_down():
    if keyboard.space:
        dino.y = dino.y - 100


# gets called 60 times a second
def update():
    cactus.x = cactus.x - 2
    if cactus.x <= 0:
        cactus.x = 1100


go()
