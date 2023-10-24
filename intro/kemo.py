from pgzrun import go

WIDTH = 1000
HEIGHT = 600

# actors
ground = Actor("grass1000")
ground.bottom = HEIGHT

dino = Actor("dino")
dino.x = 100
dino.bottom = ground.top
dino.gravity = 0

cactus = Actor("cactus")
cactus.x = 1100
cactus.bottom = ground.top
cactus.speed = 3

zombie = Actor("attack4")
zombie.bottom = ground.top
zombie.speed = 5


def draw():
    screen.fill("teal")
    dino.draw()
    cactus.draw()
    ground.draw()


def on_key_down():
    if keyboard.space:
        dino.gravity = -20


# gets called 60 times a second
def update():
    # jumping stuff
    dino.gravity = dino.gravity + 1
    dino.y = dino.y + dino.gravity

    if dino.bottom >= ground.top:
        dino.bottom = ground.top

    # moving the cactus
    cactus.x = cactus.x - cactus.speed
    if cactus.x <= 0:
        cactus.x = 1100

    # check for collision
    if dino.colliderect(cactus):
        cactus.x = 1100


go()
