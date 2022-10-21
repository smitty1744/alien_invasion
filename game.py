from ships import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = (230, 230, 230)
        self.ships=Ship(self)
    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        self.ships.blitme()
        pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()







