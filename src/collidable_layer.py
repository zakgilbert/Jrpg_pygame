from globals import Globals
from constants import *
from zone_layer import ZoneLayer

class Collidable_Layer(ZoneLayer):
    def __init__(self, g: Globals, path, x, y, width, height):
        super().__init__(g, path, width, height)
        self.pos_x = x
        self.pos_y = y
        self.hero_at_bottom = False

    def update(self):
        self.rect.x = self.g.x - self.pos_x
        self.rect.y = self.g.y - self.pos_y


    def draw(self, surface):
        surface.blit(self.image, (0, 0), pygame.Rect(
            self.rect.x, self.rect.y, WIDTH, HEIGHT))

    def get_collision_rect(self):
        return pygame.Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())
