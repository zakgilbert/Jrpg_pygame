from typing import List, Callable

class Zone:
    def __init__(self, updates: List[Callable], 
                 draws: List[Callable], 
                 collision,
                 width, height):
        self.updates = updates
        self.draws = draws
        self.collision = collision
        self.w = width
        self.h = height
    
    def update(self):
        for update in self.updates:
            update()
        self.collision.update()

    def draw(self, surface):
        for draw in self.draws:
            draw(surface)
