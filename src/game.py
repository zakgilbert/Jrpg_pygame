import pygame
from pygame.locals import *
from constants import *
from globals import *
from input import *
from zone_layer import *
from hero import *
from zone import *
from movement import *
from collidable_layer import *
from loot import *
from collision import *
#from npc import Npc

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Engine")
globals = Globals()
forest_ground = ZoneLayer(globals, "assets/map.png", 2048, 1792)
forest_trees = ZoneLayer(globals, "assets/forest.png", 2048, 1792)
# town = Collidable_Layer(globals, "assets/town.png", 500, 500, 512, 512)
chest_1 = Loot(globals, "assets/chestOpen.png",
             "assets/chestClose.png", 500, 500, 16, 16)
chest_2 = Loot(globals, "assets/chestOpen.png",
             "assets/chestClose.png", 550, 550, 16, 16)
#npc = Npc(globals, "assets/yeti.png",(600,600), 2, 5, 0, 0 )
hero = Hero(globals,"assets/lockf.png", (WIDTH // 2, HEIGHT // 2), 4, 3, 0, 1)
zone = Zone([forest_ground.update,  chest_1.update, chest_2.update, hero.update, forest_trees.update],
            [forest_ground.draw,  chest_1.draw, chest_2.draw,hero.draw, forest_trees.draw],
            Collision(globals, hero, [chest_1, chest_2]),
            2048, 1792)
render_and_update = True


# Game loop

while globals.running:
    # Handle events
    globals.running, globals.keys = handle_input()
    # Update game logic
    movement(globals, zone)
    zone.update()

    screen.fill((0, 0, 0))  # Fill the screen with black

    zone.draw(screen)

    # Flip the display
    pygame.display.flip()
    globals.clock.tick(60)

# Quit the game
pygame.quit()
