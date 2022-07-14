
# --------------------------------------------------------------------------------- #
# required libraries
import copy
import random
from cell import Cell

# --------------------------------------------------------------------------------- #

# Grid class
class Grid:
    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.w = self.width // self.rez
        self.h = self.height // self.rez
        self.grid = []
        self.options = options

    # initiate each spot in the grid with a cell object
    def initiate(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.rez, self.options)
                self.grid[i].append(cell)

    # draw each cell in the grid
    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    # randomly pick a cell using [entropy heuristic]
    def heuristic_pick(self):

        # shallow copy of a grid
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key = lambda x:x.entropy())

        # remove collapsed cells
        for i in grid_copy:
            if i.entropy() == 1:
                grid_copy.remove(i)
        

        filtered_grid = list(filter(lambda x:not x.collapsed, grid_copy))
        
        # return a pick if filtered copy os not empty
        if filtered_grid != []:
            filtered_grid = list(filter(lambda x:x.entropy()==filtered_grid[0].entropy(), filtered_grid))                
            pick = random.choice(filtered_grid)
            return pick
        else:
            return None

    # [WAVE FUNCTION COLLAPSE] algorithm
    def collapse(self):

        # pick a random cell using entropy heuristic
        pick = self.heuristic_pick()
        if pick:
            self.grid[pick.x][pick.y].observe()
        else:
            return

        # shallow copy of the gris
        next_grid = copy.copy(self.grid)

        # update the entropy values and superpositions of each cell in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]

                else:
                    # cumulative_valid_options will hold the options that will satisfy the "down", "right", "up", "left" 
                    # conditions of each cell in the grid. The cumulative_valid_options is computed by,

                    cumulative_valid_options = self.options
                    # check above cell
                    cell_above = self.grid[(i - 1) % self.w][j]
                    valid_options = []                          # holds the valid options for the current cell to fit with the above cell
                    for option in cell_above.options:
                        valid_options.extend(option.down)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check right cell
                    cell_right = self.grid[i][(j + 1) % self.h]
                    valid_options = []                          # holds the valid options for the current cell to fit with the right cell
                    for option in cell_right.options:
                        valid_options.extend(option.left)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check down cell
                    cell_down = self.grid[(i + 1) % self.w][j]
                    valid_options = []                          # holds the valid options for the current cell to fit with the down cell
                    for option in cell_down.options:
                        valid_options.extend(option.up)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check left cell
                    cell_left = self.grid[i][(j - 1) % self.h]
                    valid_options = []                          # holds the valid options for the current cell to fit with the left cell
                    for option in cell_left.options:
                        valid_options.extend(option.right)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # finally assign the cumulative_valid_options options to be the current cells valid options
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()

        # re-assign the grid value after cell evaluation
        self.grid = copy.copy(next_grid)
