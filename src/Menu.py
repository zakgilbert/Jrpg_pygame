import pygame
from pygame.locals import *
from input import *

BLUE = (30, 53, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Menu:
    def __init__(self, options):
        self.options = options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 32)
    
    def draw(self, screen):
        screen.fill(BLUE)
        pygame.draw.rect(screen, WHITE, (0, 0, screen.get_width(), screen.get_height()), 8, 10, 10, 10, 10, 10)
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() // 2, 200 + i * 50))
            screen.blit(text, text_rect)

            if i == self.selected_option:
                pygame.draw.rect(screen, WHITE, text_rect, 2)

    def handle_events(self, keys):
        if hero_down(keys):
            self.selected_option = (self.selected_option + 1) % len(self.options)
        elif hero_up(keys):
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif input_okay(keys):
            print("Selected option:", self.options[self.selected_option])


