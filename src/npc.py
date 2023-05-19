import pygame
from pygame.locals import *
from constants import *
from globals import Globals
from zone_layer import ZoneLayer
from animator import Animator


class Npc(ZoneLayer):
    def __init__(self, g: Globals, path, x, y, width, height):
        super().__init__(g, path, width, height)
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.hero_at_bottom = False
        self.animator = Animator(0.09)

    def update(self):
        self.rect.x = self.g.x - self.pos_x
        self.rect.y = self.g.y - self.pos_y
    
    