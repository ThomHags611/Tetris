import pygame

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for y in range(self.num_col)] for x in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def printGrid(self):
        for x in range(self.num_rows):
            for y in range(self.num_col):
                print(self.grid[x][y], end = " ")
            print()

    #used to fill colors array
    def get_cell_colors(self):
        dark_grey = (26, 31, 40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen): 
        for row in range(self.num_rows):
            for col in range(self.num_col):
                cell_value = self.grid[row][col]
                #creates rectangle size and coordinate on window
                cell_rect = pygame.Rect(col*self.cell_size + 1, row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect) 



         