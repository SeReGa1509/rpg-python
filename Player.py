import pygame
from Constants import *

class Player():
    def __init__(self, name):
        """
        Initializing
        :param name:
        :rtype: object
        """
        self.state = ALIVE
        self.direction = RIGHT
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ["sprites/player.png", "sprites/player.png", "sprites/player.png", "sprites/player.png"]
        self.images = []

        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(24, 102, 75, 75))
            i.append(temp.subsurface(105, 102, 75, 75))
            i.append(temp.subsurface(186, 102, 75, 75))
            i.append(temp.subsurface(264, 101, 75, 75))
            self.images.append(i)

        self.moving = [0, 0, 0, 0]

    def move(self):
        # Handle moving
        if self.moving[RIGHT] == 1:
            self.x += PLAYER_SPEED
        if self.moving[DOWN] == 1:
            self.y += PLAYER_SPEED
        if self.moving[LEFT] == 1:
            self.x -= PLAYER_SPEED
        if self.moving[UP] == 1:
            self.y -= PLAYER_SPEED

        # Check out where player is
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.x >= SCREEN_WIDTH - PLAYER_WIDTH:
            self.x = SCREEN_WIDTH - PLAYER_WIDTH
        if self.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.y = SCREEN_HEIGHT - PLAYER_HEIGHT

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        pass