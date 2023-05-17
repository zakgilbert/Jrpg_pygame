import pygame
from pygame.locals import *
from input import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, position, rows, cols, start_row, start_col, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.start_row = start_row
        self.start_col = start_col
        self.rows = rows
        self.cols = cols
        self.facing = {"down": True, "up": False,
                       "left": False, "right": False}
        self.frame_width = self.rect.width / cols
        self.frame_height = self.rect.height / rows
        self.portion_rect = pygame.Rect(self.frame_width * self.start_col,
                                        self.frame_height * self.start_row, self.frame_width, self.frame_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, keys, map, time, animation_speed, animation_timer, current_frame):
        frame_update_needed, curr_frame, ani_timer = self.time_to_animate(
            time, animation_speed, animation_timer, current_frame)
        self.move(keys, map, frame_update_needed)
        return curr_frame, ani_timer

    def draw(self, surface):
        portion_surface = self.image.subsurface(self.portion_rect)
        surface.blit(portion_surface, self.rect.topleft)

    def move(self, keys, map,frame_update_needed):
        speed = 1
        if hero_down(keys):
            if not map.map_moving_y:
                self.rect.y += speed
            if frame_update_needed or not self.is_facing("down"):
                self.toggle_facing("down")
                self.animate_down()
        elif hero_up(keys):
            if not map.map_moving_y:
                self.rect.y -= speed
            if frame_update_needed or not self.is_facing("up"):
                self.toggle_facing("up")
                self.animate_up()
        elif hero_left(keys):
            if not map.map_moving_x:
                self.rect.x -= speed
            if frame_update_needed or not self.is_facing("left"):
                self.toggle_facing("left")
                self.animate_left()
        elif hero_right(keys):
            if not map.map_moving_x:
                self.rect.x += speed
            if frame_update_needed or not self.is_facing("right"):
                self.toggle_facing("right")
                self.animate_right()
        else:
            self.stand()
        self.rect.x = max(min(self.rect.x, self.screen_width - self.portion_rect.width), 0)
        self.rect.y = max(min(self.rect.y, self.screen_height - self.portion_rect.height), 0)

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
        if self.portion_rect.x == self.rect.width - self.portion_rect.width:
            self.portion_rect.x = 0
        else:
            self.portion_rect.x += self.portion_rect.width

    def animate_y(self, row):
        self.portion_rect.y = self.portion_rect.height * row

    def stand(self):
        self.portion_rect.x = self.portion_rect.width * self.start_col

    def time_to_animate(self, time, animation_speed, animation_timer, current_frame):
        animation_timer += time / 1000.0
        if animation_timer >= animation_speed:
            current_frame = (current_frame + 1) % self.cols
            animation_timer = 0.0
            return True, current_frame, animation_timer
        else:
            return False, current_frame, animation_timer

    def is_facing(self, direction):
        return self.facing.get(direction)

    def toggle_facing(self, direction):
        self.facing = {key: False for key in self.facing}
        self.facing[direction] = True
    
    def collision_rect(self):
        return pygame.Rect(self.rect.x, self.rect.y, self.frame_width, self.frame_height)