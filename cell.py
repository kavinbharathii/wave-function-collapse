import pygame
import random

class Cell:
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.options = [random.choice(options)]

    def draw(self, win):
        if len(self.options) == 1:
            self.options[0].draw(win, self.x * self.rez, self.y * self.rez)
        else:
            pygame.draw.rect(win, (100, 100, 100), (self.x * self.rez, self.y * self.rez, self.rez, self.rez), 2)