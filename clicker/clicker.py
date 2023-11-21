import pgzrun


class ProgressBar(Rect):
    def __init__(self, title, left, top, width=0, height=100):
        super().__init__(left, top, width, height, anchor=("center", "center"))
        self.progress = width
        self.left = left
        self.top = top
        self.background = Rect(left, top, 300, height)
        self.add_progress = False
        self.title = title
        
    def draw(self):
        screen.draw.filled_rect(self.background, "gray")
        screen.draw.filled_rect(Rect(self.left, self.top, self.progress, self.height), "red")
        screen.draw.text(
            self.title,
            (self.left, self.top - 30),
            color="green",
            fontsize=40
        )
    
    def on_click(self, pos):
        if self.background.collidepoint(pos) and not self.add_progress:
            self.add_progress = True
    
    def update_progress(self):
        if self.add_progress:
            self.progress += 1
            if self.progress >= 300:
                self.progress = 0
                self.add_progress = False


bar = ProgressBar("Life", 20, 50)
bar2 = ProgressBar("Magicstuff", 20, 250)

bars = []
bars.append(bar)
bars.append(bar2)


def draw():
    bar.draw()
    bar2.draw()


def on_mouse_down(pos):
    for bar in bars:
        bar.on_click(pos)


def update():
    for bar in bars:
        bar.update_progress()


pgzrun.go()
