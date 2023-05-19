import pygame
from pygame.locals import *
from constants import *
from globals import Globals
from animator import Animator

class Sprite:
    def __init__(self,g: Globals, path, topleft, rows, cols, start_row, start_col):
        self.g = g
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.rows = rows
        self.cols = cols
        frame_w = self.rect.w // cols
        frame_h = self.rect.h // rows
        self.frame_rect = pygame.Rect(frame_w * start_col,
                                      frame_h * start_row,
                                      frame_w, frame_h)
        self.animator = Animator(0.09)
    
    def draw(self, surface):
        frame_surface = self.image.subsurface(self.frame_rect)
        surface.blit(frame_surface, self.rect.topleft)
        if DEBUG:
            pygame.draw.rect(surface,
                             (0, 255, 0),
                             pygame.Rect(self.rect.x, self.rect.y,
                                         self.frame_rect.w, self.frame_rect.h),
                             1)

    def animate_down(self):
        self.animate_y(0)
        self.animate_x()

    def animate_up(self):
        self.animate_y(1)
        self.animate_x()

    def animate_left(self):
        self.animate_y(2)
        self.animate_x()

    def animate_right(self):
        self.animate_y(3)
        self.animate_x()

    def animate_x(self):
        if self.frame_rect.x == self.rect.w - self.frame_rect.w:
            self.frame_rect.x = 0
        else:
            self.frame_rect.x += self.frame_rect.w

    def animate_y(self, row):
        self.frame_rect.y = self.frame_rect.h * row