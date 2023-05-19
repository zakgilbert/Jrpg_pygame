import pygame
from pygame.locals import *
from constants import *
from globals import Globals
from animator import *
from movement import *
from sprite import Sprite


class Hero(Sprite):
    def __init__(self, g: Globals, path, topleft, rows, cols, start_row, start_col):
        super().__init__(g, path, topleft, rows, cols, start_row, start_col)
                            
    def get_collision_rect(self):
        return pygame.Rect(self.rect.x, self.rect.y, self.frame_rect.w, self.frame_rect.h)

    def update(self):
        if not self.animator.time_to_animate(self.g.clock.get_time(), self.cols):
            return
        if down(self.g):
            self.animate_down()
        elif up(self.g):
            self.animate_up()
        elif left(self.g):
            self.animate_left()
        elif right(self.g):
            self.animate_right()

