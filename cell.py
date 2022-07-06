import pygame
import random

pygame.init()
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

class Cell:
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.options = options
        self.collapsed = False

    def draw(self, win):        
        if len(self.options) == 1:
            self.options[0].draw(win, self.y * self.rez, self.x * self.rez)
            
        else:
            pygame.draw.rect(win, (0, 0, 0), (self.y * self.rez, self.x * self.rez, self.rez, self.rez))

        # cell_entrophy = font.render(f"{self.entropy()} {(self.x, self.y)}", 1, (255, 255, 255))
        # win.blit(cell_entrophy, ((self.y * self.rez) + (self.rez // 2 - 18), (self.x * self.rez) + (self.rez // 2 - 18)))

    def entropy(self):
        return len(self.options)

    def update(self):
        self.collapsed = bool(self.entropy() == 1)

    def observe(self):
        try:
            self.options = [random.choice(self.options)]
            self.collapsed = True
        except:
            return
