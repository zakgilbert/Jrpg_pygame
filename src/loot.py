import pygame
from globals import Globals
from constants import *
from collidablelayer import CollidableLayer


class Loot:
    def __init__(self, g: Globals, path_looted, path_loot, x, y, width, height):
        self.looted_layer = CollidableLayer(
            g, path_looted, x, y, width, height)
        self.loot_layer = CollidableLayer(g, path_loot, x, y, width, height)
        self.looted = False
        self.hero_at_bottom = False
        self.g = g

    def update(self):
        self.looted_layer.update()
        self.loot_layer.update()
        if self.g.selected() and self.hero_at_bottom:
            self.looted = True

    def draw(self, surface):
        if self.looted:
            self.looted_layer.draw(surface)
            if DEBUG:
                pygame.draw.rect(surface,
                                 (255, 0, 0),
                                 pygame.Rect(self.looted_layer.rect.x * (-1),
                                             self.looted_layer.rect.y * (-1),
                                             self.looted_layer.image.get_width(),
                                             self.looted_layer.image.get_height()),
                                 1)
        else:
            self.loot_layer.draw(surface)
            if DEBUG:
                pygame.draw.rect(surface,
                                 (255, 0, 0),
                                 pygame.Rect(self.loot_layer.rect.x * (-1),
                                             self.loot_layer.rect.y * (-1),
                                             self.loot_layer.image.get_width(),
                                             self.loot_layer.image.get_height()),
                                 1)

    def get_collision_rect(self):
        return pygame.Rect(self.loot_layer.rect.x * (-1),
                           self.loot_layer.rect.y * (-1),
                           self.loot_layer.image.get_width(),
                           self.loot_layer.image.get_height())
