import pgzrun
import random

WIDTH = 800
HEIGHT = 500

player = Rect(100, HEIGHT - 32, 32, 32)
gravity = 0
dy = 0


def create_platform(x, y, width):
    rect = Rect(x, y, width, 40)
    platforms.append(rect)


platforms = []

create_platform(0, HEIGHT - 40, WIDTH)
first_platform = platforms[0]
last_platform = platforms[0]


def create_platforms():
    # index = 1
    # while len(platforms) < num_platforms:
    #    # create_platform(WIDTH + 100 * index, random.randint(3, 5) * 100, 100)
    create_platform(platforms[len(platforms) - 1].right + 100, random.randint(3, 4) * 100, 100)


def move_platforms( ):
        global first_platform
        global last_platform

        if last_platform.right < WIDTH:
            create_platforms()
            last_platform = platforms[len(platforms) - 1]
            
            # create_platform(WIDTH, HEIGHT - 40, 100)
        
        if first_platform.right < 0:
            platforms.remove(first_platform)
            first_platform = platforms[0]
            
        for platform in platforms:
            platform.x -= 5


def jump():
    global gravity
    global dy
    if keyboard.space:
        gravity = -10


def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")
    for platform in platforms:
        screen.draw.filled_rect(platform, "green")


def update():
    global gravity
    dy = 0
   # player.bottom = min(player.bottom, HEIGHT - 40)
    jump()
    
    gravity += 1
    dy += gravity
    move_platforms()
   
    for platform in platforms:
        if (platform).colliderect(player.left, player.top + dy, player.width, player.height):
            if gravity > 0:
                dy = platform.top - player.bottom
                gravity = 0
    
    player.y += dy
    


pgzrun.go()