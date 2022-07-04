
from grid import Grid
from tile import Tile
import pygame

width = 600
height = 600
rez = 20
display = pygame.display.set_mode((width, height))


tile0_img = pygame.image.load("./assets/0.png").convert_alpha()
tile0_img = pygame.transform.scale(tile0_img, (rez, rez))
tile1_img = pygame.image.load("./assets/1.png").convert_alpha()
tile1_img = pygame.transform.scale(tile1_img, (rez, rez))
tile2_img = pygame.image.load("./assets/2.png").convert_alpha()
tile2_img = pygame.transform.scale(tile2_img, (rez, rez))
tile3_img = pygame.image.load("./assets/3.png").convert_alpha()
tile3_img = pygame.transform.scale(tile3_img, (rez, rez))


def main():
    tile0 = Tile(tile0_img)
    tile1 = Tile(tile1_img)
    tile2 = Tile(tile2_img)
    tile3 = Tile(tile3_img)
    options = [tile0, tile1, tile2, tile3]
    wave = Grid(width, height, rez, options)

    wave.initiate()
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        wave.draw(display)
        pygame.display.flip()

main()