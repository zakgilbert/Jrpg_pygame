
import pygame
from pygame.locals import *
from enum import Enum

WIDTH = 800
HEIGHT = 600
KEYS = []
MOVEMENT_DISABLED = 0
X = 0
Y = 0
LAST_X = 0
LAST_Y = 0
RUNNING = True
CURRENT_FRAME = 0
ANIMATION_TIMER = 0.0
ANIMATION_SPEED = 0.09  # Lower values mean faster animation