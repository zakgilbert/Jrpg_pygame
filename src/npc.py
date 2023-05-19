import pygame
from pygame.locals import *
from constants import *
from globals import Globals
from animator import Animator


class Npc:
    def __init__(self, g: Globals, path, x, y, rows, cols, start_row, start_col, width, height):
        self.g = g
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.rows = rows
        self.cols = cols
        frame_w = self.rect.w // cols
        frame_h = self.rect.h // rows
        self.frame_rect = pygame.Rect(frame_w * start_col,
                                      frame_h * start_row,
                                      frame_w, frame_h)
        self.rect.x = self.g.x + self.pos_x
        self.rect.y = self.g.y + self.pos_y

        self.hero_at_bottom = False
        self.animator = Animator(0.09)

    def update(self):
        self.rect.x =  self.pos_x - self.g.x
        self.rect.y =  self.pos_y - self.g.y

    def draw(self, surface):
        frame_surface = self.image.subsurface(self.frame_rect)
        surface.blit(frame_surface, (self.rect.x, self.rect.y))
