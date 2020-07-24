"""Just creating a cube and moving it"""

import pygame

MAX_X = 1080
MAX_Y = 700

GREEN = (0,250,0)     

pygame.init()

#Create screen 
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('PyGame!')

#Coordinate
x = 100
y = 100
#Size square
width = 15
height = 15

speed = 1


game_over = False
#Main cycle
while game_over == False:   
    screen.fill((0,0,0))
    #Quit the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True            

    #Move square
    keys = pygame.key.get_pressed()            
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed   
    if keys[pygame.K_s]:
        y += speed     



    #Create square
    pygame.draw.rect(screen,GREEN,[x, y, width, height])            
    pygame.display.update()



pygame.quit()
quit()                





