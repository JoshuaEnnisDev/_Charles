from pgzrun import go

WIDTH = 1000
HEIGHT = 600

dino = Actor("dino")
dino.x = 100
dino.bottom = 500

cactus = Actor("cactus")
cactus.x = 1100
cactus.bottom = 500

bg1 = Actor("_05_hill1")
bg1.y = 200

bg2 = Actor("_05_hill1")
bg2.y = 200


def draw():

    screen.blit("_11_background", (0, 0))
    bg1.draw()
    screen.blit("_01_ground", (0, -710))
    screen.blit("_08_clouds", (0, -1300))
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
    
    bg2.left = bg1.right  
    bg1.x -= 2
    if bg1.right <= WIDTH:
        bg1.left = 0

    


go()
