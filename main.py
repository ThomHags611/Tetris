import pygame, sys
from game import Game
from colors import Colors

pygame.init()  

#prints score and score box
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)

#prints next and next box
next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

game_over_surface = title_font.render("GAME OVER", True, Colors.white)



screen = pygame.display.set_mode((500,620)) #sets border size for window
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
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False: 
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()

        if event.type == GAME_UPDATE and game.game_over == False: #every 200 ms the block will move down
            game.move_down()
    
    #draws on the window
            
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(next_surface, (375, 180, 50, 50))
    
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    
    pygame.draw.rect(screen,Colors.light_blue,next_rect, 0, 10)

    if(game.game_over == True):
        screen.blit(game_over_surface, (320, 450, 50,50))

    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    game.draw(screen)
    
    pygame.display.update()
    
    clock.tick(60)
