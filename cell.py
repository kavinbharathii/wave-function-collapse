
# --------------------------------------------------------------------------------- #
# required libraries
import pygame
import random

pygame.init()
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

# --------------------------------------------------------------------------------- #

# Cell class
class Cell:
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.options = options
        self.collapsed = False

    # method for drawing the cell
    def draw(self, win):        
        if len(self.options) == 1:
            self.options[0].draw(win, self.y * self.rez, self.x * self.rez)
            
    # return the entropy/the length of options
    def entropy(self):
        return len(self.options)

    # update the collapsed variable
    def update(self):
        self.collapsed = bool(self.entropy() == 1)

    # observe the cell/collapse the cell
    def observe(self):
        try:
            self.options = [random.choice(self.options)]
            self.collapsed = True
        except:
            return
