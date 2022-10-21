import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Alien Invasion')

# set color in the game
bg_color=(0,0,255)

# draw the screen
screen.fill(bg_color)

pygame.display.flip()