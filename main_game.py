import pygame
import time
from settings import Settings

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
screen.fill(ai_settings.bg_color)

# make the most recent drawm screen visible
pygame.display.flip()
