import pgzrun

progress = 0
add_progress = False
bar_background = Rect(20, 20, 300, 100)


class ProgressBar(Rect):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
        self.progress = width
        self.add_progress = False


bar = ProgressBar(20, 20, 0, 100)


def draw():
    screen.draw.filled_rect(bar_background, "gray")
    
    screen.draw.filled_rect(ProgressBar(20, 20, bar.progress, 100), "red")


def on_mouse_down(pos):
    if bar_background.collidepoint(pos):
        bar.add_progress = True


def update():
    
    if bar.add_progress:
        print("yop")
        bar.progress += 1
        if bar.progress >= 300:
            bar.progress = 0
            bar.add_progress = False


pgzrun.go()
