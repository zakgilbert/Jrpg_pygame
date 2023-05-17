import pygame
from pygame.locals import *
from sprite import *
from input import *
from states import *
from Menu import *
from map import *
from chest import *
from globals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Engine")


menu_options = ["Start Game", "Options", "Quit"]
menu = Menu(menu_options)
# Replace "map.png" with the path to your map image
scrolling_map = ScrollingMap( screen, "../assets/map.png", 2048, 1792, WIDTH, HEIGHT, 2)
forest = ScrollingMap( screen, "../assets/forest.png", 2048, 1792, WIDTH, HEIGHT, 2)
chest = TreasureChest(500, 500, 2)
sprite = Sprite("../assets/lockf.png", (WIDTH // 2, HEIGHT // 2), 4, 3, 0, 1, WIDTH, HEIGHT)
# Game loop
clock = pygame.time.Clock()

while RUNNING:
    # Handle events
    RUNNING, KEYS = handle_input()
    # Update game logic

    screen.fill((0, 0, 0))  # Fill the screen with black


    # Render
    if get_current() == STATE_ZONE:
        scrolling_map.update(KEYS)
        forest.update(KEYS)
        chest.update(KEYS, scrolling_map)
        CURRENT_FRAME, ANIMATION_TIMER = sprite.update(
            KEYS, scrolling_map, clock.get_time(), ANIMATION_SPEED, ANIMATION_TIMER, CURRENT_FRAME)
        scrolling_map.draw(screen)
        chest.draw(screen)
        chest.check_collision(screen, sprite)
        sprite.draw(screen)
        forest.draw(screen)

    if get_current() == STATE_MENU:
        menu.handle_events(KEYS)
        menu.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
