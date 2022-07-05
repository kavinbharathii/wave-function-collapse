from grid import Grid
from tile import Tile
import pygame

width = 600
height = 600
rez = 300
display = pygame.display.set_mode((width, height))

def load_image(path, rez_):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (rez_, rez_))
    return img


def main():
    # loading tile images
    options = []
    for i in range(5):
        img = load_image(f"./assets/{i}.png", rez)
        options.append(Tile(img))

    # rule set
    options[0].edges = [0, 0, 0, 0]
    options[1].edges = [1, 1, 0, 1]
    options[2].edges = [1, 1, 1, 0]
    options[3].edges = [0, 1, 1, 1]
    options[4].edges = [1, 0, 1, 1]

    for tile in options:
        tile.set_rules(options)

    # wave grid
    wave = Grid(width, height, rez, options)
    wave.initiate()
    wave.collapse()

    # game loop
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        wave.draw(display)
        pygame.display.flip()


if __name__ == "__main__":
    main()
