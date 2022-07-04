class Tile:
    def __init__(self, img):
        self.img = img

    def draw(self, win, x, y):
        win.blit(self.img, (x, y))
