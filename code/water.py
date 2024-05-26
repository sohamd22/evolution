import pygame

from tile import Tile

class Water(Tile):
    name = "water"
    
    def __init__(self, pos, groups):
        super().__init__(pos, groups)
    