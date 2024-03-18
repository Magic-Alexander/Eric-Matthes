import sys # импорт модуль sys
import pygame # импорт модуль pygame
from settings import Settings # импорт class Settings from setting module
from ship import Ship # import class Ship from ship module

class AlienInvasion: # create main class for Game

    def __init__(self):  # initializing attributes 

        pygame.init() # initial pygame quees settings
        self.settings = Settings() #" create an instance of the Settings class

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #" set the display window size and title
        pygame.display.set_caption("Alien Invasion") # set the title

        self.ship = Ship(self) #create an instance of the Ship class
    

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()






