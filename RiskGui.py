import pygame
import time
from Input import *
from Risk import *
from sys import exit
def draw():
    pygame.init()
    screen = pygame.display.set_mode((800,530))
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 8) 
    img = pygame.image.load('map2.jpg')
    radius = 15
    
    while True:        
        event = pygame.event.poll()
        
        for event in pygame.event.get():
            #Exit
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit(0)

            #Back_Ground_Image
            screen.blit(img,(0,0))
            territories = claim_random_terr()
            draw_terr(screen,terrtories,radius,font)
        
            for p in players: 
                territories = random_reinforce(p,terrtories)     
                draw_terr(screen,terrtories,radius,font)
            pygame.time.wait(200)

            attack_all(p)
            draw_terr(screen,terrtories,radius,font)

            exit(0)

def draw_terr(screen,territories,radius,font):
     for t in territories:
                
                x = t.get_xcord()
                y = t.get_ycord() 
                id = t.get_id()
                c = t.get_color()
                
                #Circles
                pygame.draw.circle(screen,c,[x,y],radius, 0)
                
                #Texts        
                text = font.render(str(t.get_num_of_units()),True,black,c)
                textrect = text.get_rect()
                textrect.center =(x,y)
                screen.blit(text, textrect)
                pygame.display.update()
                pygame.time.wait(200)
draw()