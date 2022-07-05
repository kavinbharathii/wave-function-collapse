import pygame
import random

class Cell:
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.options = options
        self.collapsed = False

    def draw(self, win):
        if len(self.options) == 1:
            self.options[0].draw(win, self.x * self.rez, self.y * self.rez)
        else:
            pygame.draw.rect(win, (100, 100, 100), (self.x * self.rez, self.y * self.rez, self.rez, self.rez), 2)

    def entrophy(self):
        return len(self.options)

    def update(self):
        self.collapsed = bool(self.entrophy() == 1)

    def observe(self):
        self.options = [random.choice(self.options)]
        self.collapsed = True
