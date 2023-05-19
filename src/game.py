import pygame
from constants import *
from globals import Globals
from input import handle_input
from zone_layer import ZoneLayer
from hero import Hero
from zone import Zone
from movement import movement
from loot import Loot
from collision import Collision
from npc import Npc

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Engine")

g = Globals()
forest_ground = ZoneLayer(g, "../assets/map.png", 2048, 1792)
forest_trees = ZoneLayer(g, "../assets/forest.png", 2048, 1792)
chest_1 = Loot(g, "../assets/chestOpen.png", "../assets/chestClose.png", 500, 500, 16, 16)
chest_2 = Loot(g, "../assets/chestOpen.png", "../assets/chestClose.png", 550, 550, 16, 16)
npc = Npc(g, "../assets/yeti.png", 600, 600, 2, 5, 0, 0, 160, 64)
hero = Hero(g, "../assets/lockf.png", (WIDTH // 2, HEIGHT // 2), 4, 3, 0, 1)
zone = Zone([forest_ground.update, chest_1.update, chest_2.update, npc.update, hero.update, forest_trees.update],
            [forest_ground.draw, chest_1.draw, chest_2.draw, npc.draw, hero.draw, forest_trees.draw],
            Collision(g, hero, [chest_1, chest_2, npc]),
            2048, 1792)
render_and_update = True

# Game loop

while g.running:
    # Handle events
    g.running, g.keys = handle_input()
    # Update game logic
    movement(g, zone)
    zone.update()

    screen.fill((0, 0, 0))  # Fill the screen with black

    zone.draw(screen)

    # Flip the display
    pygame.display.flip()
    g.clock.tick(60)

# Quit the game
pygame.quit()
