import pygame
from Constants import *

class Player():
    def __init__(self):
        self.state = ALIVE
        self.position = [START_X, START_Y, RIGHT]
        self.name = "Sergiy"
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ["sprites/player.png"]
        self.images = []

        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(24, 102, 75, 75))
            i.append(temp.subsurface(105, 102, 75, 75))
            i.append(temp.subsurface(186, 102, 75, 75))
            i.append(temp.subsurface(264, 101, 75, 75))
            self.images.append(i)

        self.moving[0, 0, 0, 0]

    def move(self):
        pass

    def render(self, screen):
        screen.blit(self.images[self.position[0]][self.state], (self.position[X], self.position[Y]))

    def render_ui(self, screen):
        pass