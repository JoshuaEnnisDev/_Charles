import pgzrun



class ProgressBar(Rect):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
        self.progress = width
        self.left = left
        self.top = top
        self.background = Rect(left, top, 300, height)
        self.add_progress = False
    
    def draw(self):
        screen.draw.filled_rect(self.background, "gray")
        screen.draw.filled_rect(self, "red")
        

bar = ProgressBar(20, 20, 0, 100)


def draw():
    bar.draw()


def on_mouse_down(pos):
    if bar.background.collidepoint(pos):
        bar.add_progress = True


def update():
    
    if bar.add_progress:
        print("yop")
        bar.progress += 1
        if bar.progress >= 300:
            bar.progress = 0
            bar.add_progress = False


pgzrun.go()
