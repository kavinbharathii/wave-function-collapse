from grid import Grid
from tile import Tile
import pygame
pygame.init()
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

width = 600
height = 600
rez = 60
display = pygame.display.set_mode((width, height))

def load_image(path, rez_):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (rez_, rez_))
    return img

def disp_msg(text, x, y):
    msg = font.render(str(text), 1, (255, 255, 255))
    display.blit(msg, (x, y))

def hover(mouse_pos, rez, grid):
    mx, my = mouse_pos
    x = mx // rez
    y = my // rez
    cell = grid.grid[y][x]
    cell_entropy = cell.entropy()
    cell_collpased = cell.collapsed
    cell_options = [opt.edges for opt in cell.options]
    pygame.draw.rect(display, (20, 20, 20), (mouse_pos[0], mouse_pos[1], 200, 100))
    disp_msg(f"entrophy  : {cell_entropy}", mx + 10, my + 10)
    disp_msg(f"collapsed : {cell_collpased}", mx + 10, my + 30)
    disp_msg(f"options   : {cell_options}", mx + 10, my + 50)


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

    # for row in wave.grid:
    #     for cell in row:
    #         print((cell.x, cell.y, cell.collapsed), end=" ")
    #     print()

    # game loop
    loop = True
    clock = pygame.time.Clock()
    while loop:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            

        wave.draw(display)
        wave.collapse()
        # mos_pos = pygame.mouse.get_pos()
        # hover(mos_pos, rez, wave)
        pygame.display.flip()


if __name__ == "__main__":
    main()
