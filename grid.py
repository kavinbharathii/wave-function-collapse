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
        for i in range(self.w):
            for j in range(self.h):
                self.grid[i][j].draw(win)

    def random_pick(self):
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key = lambda x:x.entrophy())

        for i in grid_copy:
            if i.entrophy() == 1:
                grid_copy.remove(i)
                
        filtered_grid = list(filter(lambda x:x.entrophy()==grid_copy[0].entrophy(), grid_copy))
        pick = random.choice(filtered_grid)
        return pick

    def collapse(self):
        pick = self.random_pick()
        self.grid[pick.x][pick.y].observe()

        next_grid = copy.copy(self.grid)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]

                else:
                    cell = self.grid[i][j]

                    # check above cell
                    try:
                        cell_above = self.grid[i - 1][j]
                        if cell_above.collapsed:
                            for option in cell.options:
                                if option not in cell_above.options[0].below:
                                    cell.options.remove(option)
                    except:
                        pass

                    # check right cell
                    try:
                        cell_right = self.grid[i][j + 1]
                        if cell_right.collapsed:
                            for option in cell.options:
                                if option not in cell_right.options[0].left:
                                    cell.options.remove(option)
                    except:
                        pass

                    # check down cell
                    try:
                        cell_down = self.grid[i][j + 1]
                        if cell_down.collapsed:
                            for option in cell.options:
                                if option not in cell_down.options[0].up:
                                    cell.options.remove(option)
                    except:
                        pass          

                    # check left cell
                    try:
                        cell_left = self.grid[i][j + 1]
                        if cell_left.collapsed:
                            for option in cell.options:
                                if option not in cell_left.options[0].right:
                                    cell.options.remove(option)
                    except:
                        pass 

                    if len(cell.options) == 1:
                        cell.collapsed = True

        self.grid = next_grid
