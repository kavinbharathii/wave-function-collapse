import copy
import random
from cell import Cell

class Grid:
    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.w = self.width // self.rez
        self.h = self.height // self.rez
        self.grid = []
        self.options = options

    def initiate(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.rez, self.options)
                self.grid[i].append(cell)

    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    def random_pick(self):
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key = lambda x:x.entropy())

        for i in grid_copy:
            if i.entropy() == 1:
                grid_copy.remove(i)
                

        filtered_grid = list(filter(lambda x:not x.collapsed, grid_copy))
        if filtered_grid != []:
            filtered_grid = list(filter(lambda x:x.entropy()==filtered_grid[0].entropy(), filtered_grid))                
            pick = random.choice(filtered_grid)
            return pick
        else:
            return None


    def collapse(self):
        pick = self.random_pick()
    
        if pick:
            self.grid[pick.x][pick.y].observe()
        else:
            return

        next_grid = copy.copy(self.grid)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]

                else:
                    cumulative_valid_options = self.options
                    # check above cell
                    if i > 1:
                        cell_above = self.grid[i - 1][j]
                        valid_options = []
                        for option in cell_above.options:
                            valid_options.extend(option.down)
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check right cell
                    if j < self.h - 1:
                        cell_right = self.grid[i][j + 1]
                        valid_options = []
                        for option in cell_right.options:
                            valid_options.extend(option.left)
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check down cell
                    if i < self.w - 1:
                        cell_down = self.grid[i + 1][j]
                        valid_options = []
                        for option in cell_down.options:
                            valid_options.extend(option.up)
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check left cell
                    if j > 1:
                        cell_left = self.grid[i][j - 1]
                        valid_options = []
                        for option in cell_left.options:
                            valid_options.extend(option.right)
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # print()
                    # print([opt.index for opt in cumulative_valid_options])
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()

        self.grid = copy.copy(next_grid)
