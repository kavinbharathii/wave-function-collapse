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
            filtered_grid = list(filter(lambda x:x.entropy()==filtered_grid[0].entropy(), grid_copy))                
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
                    cell = self.grid[i][j]

                    if cell.entropy() == 1:
                        cell.update()
                        break

                    # check above cell
                    try:
                        cell_above = self.grid[i - 1][j]
                        if cell_above.collapsed:
                            valid_options = cell_above.below
                            cell.options = [option for option in cell.options if option in valid_options]
                    except:
                        pass

                    # check right cell
                    try:
                        cell_right = self.grid[i][j + 1]
                        if cell_right.collapsed:
                            valid_options = cell_above.left
                            cell.options = [option for option in cell.options if option in valid_options]
                    except:
                        pass

                    # check down cell
                    try:
                        cell_down = self.grid[i + 1][j]
                        if cell_down.collapsed:
                            valid_options = cell_above.up
                            cell.options = [option for option in cell.options if option in valid_options]
                    except:
                        pass          

                    # check left cell
                    try:
                        cell_left = self.grid[i][j - 1]
                        if cell_left.collapsed:
                            valid_options = cell_above.right
                            cell.options = [option for option in cell.options if option in valid_options]
                    except:
                        pass 

                    # print(cell.x, cell.y, cell.collapsed, [i.edges for i in cell.options])

        self.grid = copy.copy(next_grid)
