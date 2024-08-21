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
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make the most recently draw screen visible.
            pygame.display.flip()
            self.clock.tick(60) #game loop 60 frames per second

            #redraw the screen during each pass through loop

            self.screen.fill(self.bg_color)
            self.ship.blitme()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()