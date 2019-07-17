import pygame
import random
import sys


# first thing to do is to initialize pygame
pygame.init()

#just variables
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)   #tupple
BACKGROUND_COLOR = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (170, 100, 160)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]     #list

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]       #setting enemy in random position in x axis (from 0 to 800-enemy size
enemy_list = [enemy_pos]

speed = 10

# making a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game loop, loop that runs while game is not over
game_over = False

score = 0

clock = pygame.time.Clock()     #making an instance clock

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, speed):
    if score < 20:
        speed = 5
    elif score < 40:
        speed = 8
    elif score < 60:
        speed = 15
    else:
        speed = 25
    return speed

def drop_enemies(enemy_list):   #pass enemy_list to this function, a function that generates multiple positions for enemies
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:    #if there are less than 10 enemies
        x_pos = random.randint(0, WIDTH - enemy_size)    #random position in x axis
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):   #need an enemy list argument, a function that draws enemies
    for enemy_pos in enemy_list:   #goes through the enemy_list
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))  # drawing an enemy/ another rectangle

def update_enemy_positions(enemy_list, score):     #a function that makes the enemies fall
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:        #if enemy starts at top of y axis
            enemy_pos[1] += speed              #make the original position go down the y axis

        else:           #if outside the range of y axis
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
        return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if e_x >= p_x and e_x < (p_x + player_size) or (p_x >= e_x and p_x < (e_x + enemy_size)):       #x overlap based on x position and x size
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)): # y overlap based on y position and y size
            return True
    return False

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

    screen.fill(BACKGROUND_COLOR)      #to move rectangle and stop drawing

    #UPDATING THE POSITION OF ENEMY

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    speed = set_level(score, speed)

    text = "Score: " + str(score)

    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))     #drawing a rectangle

    clock.tick(30)      #making a delay on the while loop


    pygame.display.update()     #need to update screen every iteration