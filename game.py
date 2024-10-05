from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
    #will choose random block and delete it from list, ensuring we use all blocks before repeating cycle
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    
    #checks and makes sure block is in boreder true = in border, false = out of border
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col) :
                return False
        return True
    
    #rotates object
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False: 
            self.undo_rotation()

    #will be called if invalid rotation is done near border
    def undo_rotation(self):
        self.current_block.rotation_state -= 1

        if(self.current_block.rotation_state < 0):
            self.current_block.rotation_state = len(self.current_block.cell - 1)
    
    #locks block when it hits bottom of the screen
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id #updates board array with id of object
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

    #returns false if block collides with another block
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tiles in tiles:
            if self.grid.is_empty(tiles.row, tiles.col) == False:
                return False
        return True




                

        