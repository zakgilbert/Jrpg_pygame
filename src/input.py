import pygame
from pygame.locals import *


def handle_input():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            return False, keys
    return True, keys
