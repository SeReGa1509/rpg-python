import pygame
from Constants import *

class Main():
    def __init__(self, screen):
        """
        Init function
        :param screen:
        """
        self.screen = screen
        self.background = pygame.image.load('images/background.jpg')
        self.running = True
        self.main_loop()

    def handle_events(self):
        pass

    def render(self):
        """
        Rendering everything
        """
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def main_loop(self):
        """
        The main loop
        """
        while self.running == True:
            self.render()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
