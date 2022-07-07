
# --------------------------------------------------------------------------------- #

# libraries requird
import pygame
pygame.init()
from grid import Grid
from tile import Tile

# initializong the font object
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

# --------------------------------------------------------------------------------- #

# global variables
width = 600
height = 600
rez = 50
display = pygame.display.set_mode((width, height))

# --------------------------------------------------------------------------------- #
# function for loading images with given resolution/size
def load_image(path, rez_, padding):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (rez_ - padding, rez_ - padding))
    return img

# --------------------------------------------------------------------------------- #

# function for displayong a given message
def disp_msg(text, x, y):
    msg = font.render(str(text), 1, (255, 255, 255))
    display.blit(msg, (x, y))

# --------------------------------------------------------------------------------- #

# debug tool 
# when mouse is hovered over a cell, if displays the 
#       [ ] cell entropy
#       [ ] cell collapsed boolean
#       [ ] cell options / tiles
def hover(mouse_pos, rez, grid):
    mx, my = mouse_pos
    x = mx // rez
    y = my // rez
    cell = grid.grid[y][x]

    # cell information
    cell_entropy = cell.entropy()
    cell_collpased = cell.collapsed
    cell_options = [opt.edges for opt in cell.options]

    # hover box
    pygame.draw.rect(display, (20, 20, 20), (mouse_pos[0], mouse_pos[1], 200, 100))

    # hover text/info
    disp_msg(f"entrophy  : {cell_entropy}", mx + 10, my + 10)
    disp_msg(f"collapsed : {cell_collpased}", mx + 10, my + 30)
    disp_msg(f"options   : {cell_options}", mx + 10, my + 50)

# --------------------------------------------------------------------------------- #

# main game function
def main():
    # loading tile images
    options = []
    for i in range(5):
        # load tetris tile
        img = load_image(f"./assets/{i}.png", rez, 5)
        
        # load corner tile
        # img = load_image(f"./assets/{i}.png", rez)
        options.append(Tile(img))

    # edge conditions for tetris tiles
    options[0].edges = [0, 0, 0, 0]
    options[1].edges = [1, 1, 0, 1]
    options[2].edges = [1, 1, 1, 0]
    options[3].edges = [0, 1, 1, 1]
    options[4].edges = [1, 0, 1, 1]

    # edge conditions for corner tiles
    # options[0].edges = [0, 0, 0, 0]
    # options[1].edges = [1, 1, 0, 0]
    # options[2].edges = [0, 1, 1, 0]
    # options[3].edges = [0, 0, 1, 1]
    # options[4].edges = [1, 0, 0, 1]

    # update tile rules for each tile
    for i, tile in enumerate(options):
        tile.index = i 
        tile.set_rules(options)

    # wave grid
    wave = Grid(width, height, rez, options)
    wave.initiate()

    # toggle for displaying debug information
    hover_toggle = False

    # game loop
    loop = True
    while loop:

        display.fill((0, 0, 0))
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hover_toggle = not hover_toggle
            
        # grid draw function
        wave.draw(display)
        # grid collapse method to run the alogorithm
        wave.collapse()

        # mouse position and hover debug
        if hover_toggle:
            mos_pos = pygame.mouse.get_pos()
            hover(mos_pos, rez, wave)

        # update the display
        pygame.display.flip()

# --------------------------------------------------------------------------------- #

# calling the main function
if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------- #
