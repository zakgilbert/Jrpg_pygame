import pygame
from pygame.locals import *
from input import *

class ScrollingMap:
    def __init__(self,screen, map_image_path, map_width, map_height, view_width, view_height, scroll_speed):
        self.map_image = pygame.image.load(map_image_path)
        self.map_rect = self.map_image.get_rect()
        self.map_width = map_width
        self.map_height = map_height
        self.view_width = view_width
        self.view_height = view_height
        self.scroll_speed = scroll_speed
        self.view_rect = pygame.Rect(0, 0, view_width, view_height)
        self.view_rect.center = screen.get_rect().center
        self.map_moving_x = False
        self.map_moving_y = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    def update(self, keys):
        if keys[K_LEFT] or keys[K_a]:
            self.view_rect.x -= self.scroll_speed
        if keys[K_RIGHT] or keys[K_d]:
            self.view_rect.x += self.scroll_speed
        if keys[K_UP] or keys[K_w]:
            self.view_rect.y -= self.scroll_speed
        if keys[K_DOWN] or keys[K_s]:
            self.view_rect.y += self.scroll_speed

        view_rect_x = max(min(self.view_rect.x, self.map_width - self.view_width), 0)
        view_rect_y = max(min(self.view_rect.y, self.map_height - self.view_height), 0)
        self.map_moving_x = (view_rect_x == self.view_rect.x)
        self.map_moving_y = (view_rect_y == self.view_rect.y)
        self.view_rect.x = view_rect_x
        self.view_rect.y = view_rect_y

    def draw(self, screen):

        # Calculate the position to blit the map image
        map_x = (screen.get_width() - self.view_rect.width) // 2
        map_y = (screen.get_height() - self.view_rect.height) // 2

        # Calculate the position to crop the map image
        crop_x = self.view_rect.x
        crop_y = self.view_rect.y

        # Blit the cropped portion of the map image at the calculated position
        screen.blit(self.map_image, (map_x, map_y), pygame.Rect(crop_x, crop_y, self.view_rect.width, self.view_rect.height))
