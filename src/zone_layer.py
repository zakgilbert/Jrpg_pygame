import pygame
from pygame.locals import *
from globals import Globals
from constants import *


class ZoneLayer:
    def __init__(self, g: Globals, path, width, height):
        self.image = pygame.image.load(path)
        self.rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.w = width #todo doesn't need
        self.h = height #todo doesn't need
        self.g = g

    def update(self):
        self.rect.x = self.g.x
        self.rect.y = self.g.y

    def draw(self, surface):
        surface.blit(self.image, (0, 0), pygame.Rect(
            self.rect.x, self.rect.y, WIDTH, HEIGHT))
