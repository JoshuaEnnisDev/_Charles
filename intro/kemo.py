from pgzrun import go

WIDTH = 1000
HEIGHT = 600

# actors
ground = Actor("grass1000")
ground.bottom = HEIGHT

dino = Actor("dino")
dino.x = 100
# charlie needs to adddino.bottom = ground.top
dino.gravity = 0

cactus = Actor("cactus")
cactus.x = 1100
cactus.bottom = HEIGHT

zombie = Actor("attack4")
zombie.bottom = 399


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
    if dino.bottom >= HEIGHT:
        dino.bottom = HEIGHT

    # moving the cactus
    cactus.x = cactus.x - 2
    if cactus.x <= 0:
        cactus.x = 1100

    # check for collision
    if dino.colliderect(cactus):
        print("ouch")


go()
