import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for y in range(self.num_col)] for x in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def printGrid(self):
        for x in range(self.num_rows):
            for y in range(self.num_col):
                print(self.grid[x][y], end = " ")
            print()

    #used to fill colors array
    def draw(self, screen): 
        for row in range(self.num_rows):
            for col in range(self.num_col):
                cell_value = self.grid[row][col]
                #creates rectangle size and coordinate on window
                cell_rect = pygame.Rect(col*self.cell_size + 1, row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect) 



         