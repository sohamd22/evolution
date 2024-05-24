"""
Grass is at the bottom of the food chain.

They have genetic traits:
- LIFESPAN (years): how old they can get.
- MAX_HEIGHT (meters): how tall they may grow.

They have variable traits:
- age (years): measure of growth; can reproduce at 20% of lifespan given that it is greater than 1 year;
               may reach upto the LIFESPAN based on environmental factors (vicinity of Water).
- height (meters): measure of height; can absorb Water from further away as the height grows; increases
                   with age and may grow upto the MAX_HEIGHT based on environmental factors (vicinity of Water).

If found without Water for an extended duration, it is removed from the ecosystem.
"""

import pygame as pg
import random as rd
import math

class Grass(pg.sprite.Sprite):
    ID = 2
    COLOR = (41, 128, 17) # dark green

    instances = pg.sprite.Group()

    def __init__(self, rect,
                 LIFESPAN = 6, MAX_HEIGHT = 1, age = 0, height = 0):
        super().__init__()
        self.rect = rect

        # genetic traits
        self.MAX_HEIGHT = MAX_HEIGHT
        self.LIFESPAN = LIFESPAN

        # variable traits
        self.age = age
        self.height = height

        Grass.instances.add(self)
    
    def can_reproduce(self, tile_size, waters):
        pass

    def update(self, screen):
        self.age += 0.005
        if self.rect.height < self.MAX_HEIGHT:
            self.height += 0.025
                
        self.rect.height = self.height
        pg.draw.rect(screen, self.COLOR, self.rect)
