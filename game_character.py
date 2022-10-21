import pygame
import time
from settings import Settings

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")


image = pygame.image.load('images/ship.bmp')
rect = image.get_rect()
screen_rect = screen.get_rect()

# Start each new ship at the center of the screen.
rect.centerx = screen_rect.centerx
rect.bottom = screen_rect.centery
screen.fill(ai_settings.bg_color)
# Draw the ship at the location
screen.blit(image, rect)


# make the most recent drawm screen visible
pygame.display.flip()