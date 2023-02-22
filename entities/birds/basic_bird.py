import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class BasicBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.name = self.BASIC_BIRD
        self.image = pygame.image.load("basic_bird.png")
    
    def ability(self):
        self.vel = self.vel * 2
        self.acc = 0
        self.used_ability = True