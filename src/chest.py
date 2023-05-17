import pygame
from pygame.locals import *
from input import *

class TreasureChest:
    def __init__(self, x, y, scroll_speed):
        self.x = x
        self.y = y
        self.image_close = pygame.image.load('../assets/chestClose.png')  # Replace 'treasure_chest.png' with the actual image file name
        self.image_open = pygame.image.load('../assets/chestOpen.png')  # Replace 'treasure_chest.png' with the actual image file name
        self.rect_close = self.image_close.get_rect()
        self.rect_open = self.image_open.get_rect()
        self.is_looted = False
        self.scroll_speed = scroll_speed

    def draw(self, surface):
        if self.is_looted:
            surface.blit(self.image_open, (self.x, self.y))
        else:
            surface.blit(self.image_close, (self.x, self.y))
    
    def check_collision(self, surface, sprite):
        rect_color = (255, 0,0)
        green = (0, 255, 0)
        rect = self.collision_rect()
        other_rect = sprite.collision_rect()
        pygame.draw.rect(surface,rect_color,rect,1)
        pygame.draw.rect(surface,green, other_rect,1 )
        collide_rect = rect.colliderect(other_rect)
        if collide_rect:
            if sprite.rect.x < self.x:
                sprite.rect.x = self.x - sprite.frame_width
            elif sprite.rect.x > self.x:
                sprite.rect.x = self.x + self.image_close.get_width()
            elif sprite.rect.y < self.y:
                sprite.rect.y = self.y - sprite.frame_height
            elif sprite.rect.y > self.y:
                sprite.rect.y = self.y + self.image_close.get_height()
        return collide_rect
    
    def update(self, keys, map):
        if hero_down(keys):
            if map.map_moving_y:
                self.y -= self.scroll_speed
        if hero_up(keys):
            if map.map_moving_y:
                self.y += self.scroll_speed
        if hero_left(keys):
            if map.map_moving_x:
                self.x += self.scroll_speed
        if hero_right(keys):
            if map.map_moving_x:
                self.x -= self.scroll_speed
    
    def collision_rect(self):
        return pygame.Rect(self.x, self.y, self.image_close.get_width(), self.image_close.get_height())
