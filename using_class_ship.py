import pygame
import time
from settings import Settings
from ship import Ship
pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")

ship=Ship(screen)


screen.fill(ai_settings.bg_color)

ship.blitme()
# Draw the ship at the location
ship.blitme()
# screen.blit(image, rect)


# make the most recent drawm screen visible
pygame.display.flip()

time.sleep(5)
sys.exit()