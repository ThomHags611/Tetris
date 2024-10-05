import pygame, sys
from game import Game

pygame.init()  
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300,600)) #sets border size for window
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() #will account for refresh rate

game = Game()

while True:
    for event in pygame.event.get(): 
        #loops until we close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    
    clock.tick(60)
