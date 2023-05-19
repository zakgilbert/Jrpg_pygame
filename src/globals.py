import pygame
from pygame.locals import *


class Globals:
    def __init__(self):
        self.keys = []
        self.movement_disabled = 0
        self.x = 0
        self.y = 0
        self.last_x = 0
        self.last_y = 0
        self.running = True
        self.clock = pygame.time.Clock()
        self.hero_col_bools = [False, False, False, False]

    def selected(self):
        return self.keys[K_j]

    def get_hero_bottom(self):
        return self.hero_col_bools[0]

    def get_hero_top(self):
        return self.hero_col_bools[1]

    def get_hero_left(self):
        return self.hero_col_bools[2]

    def get_hero_right(self):
        return self.hero_col_bools[3]

    def set_hero_bottom(self):
        self.set_hero_col_bool(0)

    def set_hero_top(self):
        self.set_hero_col_bool(1)

    def set_hero_left(self):
        self.set_hero_col_bool(2)

    def set_hero_right(self):
        self.set_hero_col_bool(3)

    def set_hero_col_bool_false(self):
        self.set_hero_col_bool(-1)

    def set_hero_col_bool(self, index):
        for i in range(len(self.hero_col_bools)):
            if i == index:
                self.hero_col_bools[i] = True
            else:
                self.hero_col_bools[i] = False
