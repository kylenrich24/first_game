import pygame
import sys

# first thing to do is to initialize pygame
pygame.init()

#just variables
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)   #tupple
player_pos = [400, 300]     #list
player_size = 50


# making a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game loop, loop that runs while game is not over
game_over = False

while not game_over:        #going to keep running while not game_over

    for event in pygame.event.get():        #getting the events

        if event.type == pygame.QUIT:       #system exit/cancel
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]           #original position of rectangle
            y = player_pos[1]


            if event.key == pygame.K_LEFT:      #pressing left key
                x -= player_size
            elif event.key == pygame.K_RIGHT:       #pressing right key
                x += player_size

            player_pos = [x, y]     #new position of rectangle

    screen.fill((0, 0, 0))      #to move rectangle and stop drawing
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))     #drawing a rectangle




    pygame.display.update()     #need to update screen every iteration