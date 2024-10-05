import pygame, sys
from game import Game

pygame.init()  
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300,600)) #sets border size for window
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() #will account for refresh rate

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200) #will trigger game_update event every 200 milliseconds
while True:
    for event in pygame.event.get(): 
        #loops until we close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #runs if arrow keys are hit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()

        if event.type == GAME_UPDATE: #every 200 ms the block will move down
            game.move_down()
    
    #draws on the window
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    
    clock.tick(60)
