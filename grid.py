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

    #checks if given point is within grid
    def is_inside(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_col:
            return True
        return False

    def is_empty(self, row, col):
        if(self.grid[row][col] == 0):
            return True
        return False
        



         