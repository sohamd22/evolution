"""
Water is a static element of variable size and its only purpose is to be used by organisms in the ecosystem to 
sustain themselves.
"""

import pygame as pg

class Water(pg.sprite.Sprite):
    ID = 1
    COLOR = (33, 139, 219) # blue

    instances = pg.sprite.Group()

    def __init__(self, rect):
        super().__init__()
        self.rect = rect

        Water.instances.add(self)
    
    def update(self, screen):
        pg.draw.rect(screen, self.COLOR, self.rect)