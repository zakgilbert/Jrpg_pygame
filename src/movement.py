import pygame
from pygame.locals import *
from constants import *
from globals import Globals
from zone import Zone


def movement(g: Globals, zone: Zone):
    result = False
    if change_position(g):
        bounds(g, zone)
        result = True
    return result


def change_position(g: Globals):
    is_moving = False
    if not g.movement_disabled:
        if up(g) and not g.get_hero_bottom():
            g.last_y = g.y
            g.y -= SCROLL_SPEED
            is_moving = True
        elif down(g) and not g.get_hero_top():
            g.last_y = g.y
            g.y += SCROLL_SPEED
            is_moving = True
        elif left(g) and not g.get_hero_right():
            g.last_x = g.x
            g.x -= SCROLL_SPEED
            is_moving = True
        elif right(g) and not g.get_hero_left():
            g.last_x = g.x
            g.x += SCROLL_SPEED
            is_moving = True
    return is_moving


def bounds(g: Globals, zone: Zone):
    g.x = max(min(g.x, zone.w - WIDTH), 0)
    g.y = max(min(g.y, zone.h - HEIGHT), 0)


def down(g: Globals):
    return g.keys[DOWN]


def up(g: Globals):
    return g.keys[UP]


def left(g: Globals):
    return g.keys[LEFT]


def right(g: Globals):
    return g.keys[RIGHT]
