import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((100, 50))
pygame.display.set_caption('Key Press Identifier')
font = pygame.font.SysFont('arial', 24)

while (True):
    for a in pygame.event.get():
        if (a.type == QUIT):
           pygame.quit()
           exit()
           
    if (pygame.key.get_focused()):
       press = pygame.key.get_pressed()
       
    for b in range(0, len(press)):
        if press[b] == 1:
            screen.fill((0, 0, 0))
            keyName = pygame.key.name(b)
            keyName1 = font.render(keyName, True, (255, 255, 255))
            screen.blit(keyName1, (0, 0))

    pygame.display.update()
