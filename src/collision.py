import pygame
from pygame.locals import *
from constants import *
from hero import Hero
from loot import Loot
from globals import Globals
from typing import List


class Collision:
    def __init__(self, g: Globals, hero: Hero, layers: List[Loot]):
        self.g = g
        self.hero = hero
        self.layers = layers
    
    def update(self):
        hero_rect = self.hero.get_collision_rect()
        for layer in self.layers:
            collide_rect = layer.get_collision_rect().colliderect(hero_rect)
            if collide_rect:
                result = self.check_collision(hero_rect, layer.get_collision_rect())
                if result == "bottom":
                    layer.hero_at_bottom = True
                    self.g.set_hero_bottom()
                elif result == "top":
                    self.g.set_hero_top()
                elif result == "left":
                    self.g.set_hero_left()
                elif result == "right":
                    self.g.set_hero_right()
                else:
                    self.g.set_hero_col_bool_false()
                break
            else:
                layer.hero_at_bottom = False
                self.g.set_hero_col_bool_false()

    def check_collision(self, rect1, rect2):
        # Calculate the center points of the rectangles
        rect1_center = rect1.center
        rect2_center = rect2.center

        # Calculate the distances between the centers of the rectangles
        dx = rect1_center[0] - rect2_center[0]
        dy = rect1_center[1] - rect2_center[1]

        # Calculate the minimum distance between the centers along the x and y axes
        min_distance_x = (rect1.width + rect2.width) / 2
        min_distance_y = (rect1.height + rect2.height) / 2

        # Check for collision on each side
        if abs(dx) <= min_distance_x and abs(dy) <= min_distance_y:
            overlap_x = min_distance_x - abs(dx)
            overlap_y = min_distance_y - abs(dy)

            if overlap_x >= overlap_y:
                # Colliding on top or bottom side
                if dy > 0:
                    return "bottom"
                else:
                    return "top"
            else:
                # Colliding on left or right side
                if dx > 0:
                    return "right"
                else:
                    return "left"

        # No collision
        return None
