import pygame
from Constants import *
from Player import *

class Main():
    def __init__(self, screen):
        """
        Init function
        :param screen:
        """
        self.screen = screen
        self.background = pygame.image.load('images/background.jpg')
        self.player = Player("Sergiy")
        self.running = True
        self.main_loop()

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

            # Moving player
            elif e.type == pygame.KEYDOWN: # On key down
                if e.key == pygame.K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if e.key == pygame.K_DOWN:
                    self.player.direction = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if e.key == pygame.K_LEFT:
                    self.player.direction = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if e.key == pygame.K_UP:
                    self.player.direction = UP
                    self.player.moving = [0, 0, 0, 1]

            elif e.type == pygame.KEYUP: # On key up
                if e.key == pygame.K_UP:
                    self.player.moving[UP] = 0
                if e.key == pygame.K_DOWN:
                    self.player.moving[DOWN] = 0
                if e.key == pygame.K_LEFT:
                    self.player.moving[LEFT] = 0
                if e.key == pygame.K_RIGHT:
                    self.player.moving[RIGHT] = 0


    def render(self):
        """
        Rendering everything
        """
        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        pygame.display.flip()

    def main_loop(self):
        """
        The main loop
        """
        while self.running == True:
            self.player.move()
            self.render()
            self.handle_events()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
