import pygame
from pygame.locals import *
from states import get_current, get_last, STATE_ZONE, STATE_MAP, STATE_MENU, set_current, set_last
from enum import Enum


def handle_input():
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            return False, keys
    handle_state(keys)
    return True, keys


def hero_down(KEYS):
    return KEYS[K_DOWN] or KEYS[K_s]


def hero_up(KEYS):
    return KEYS[K_UP] or KEYS[K_w]


def hero_left(KEYS):
    return KEYS[K_LEFT] or KEYS[K_a]


def hero_right(KEYS):
    return KEYS[K_RIGHT] or KEYS[K_d]

def input_semi_colon(KEYS):
    return KEYS[K_SEMICOLON]

def input_okay(KEYS):
    return KEYS[K_j]

def input_cancel(KEYS):
    return KEYS[K_l]

def handle_state(KEYS):
    last = get_last()
    current = get_current()
    if current == STATE_ZONE or current == STATE_MAP:
        if input_semi_colon(KEYS):
            set_last(current)
            set_current(STATE_MENU)
    elif current == STATE_MENU:
        if input_cancel(KEYS):
            set_last(current)
            set_current(last)




