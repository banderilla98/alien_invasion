"""alien invasion game"""
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion project")

        #background screen color
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

            #redraw the screen during each pass through the loop.
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right
                    self.ship.rect.x += 1

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()