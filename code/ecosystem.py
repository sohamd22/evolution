import pygame
from settings import *

from water import Water
from plant import Plant

class Ecosystem:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.water_sprites = pygame.sprite.Group()
        self.plant_sprites = pygame.sprite.Group()

        # sprite setup
        self.initialize_map()
    
    def initialize_map(self):
        for r, row in enumerate(MAP):
            for c, col in enumerate(row):
                x = c * TILE_SIZE
                y = r * TILE_SIZE

                if col == 'w':
                    Water((x, y), [self.visible_sprites, self.collision_sprites, self.water_sprites])
                elif col == 'g':
                    Plant((x, y), [self.visible_sprites, self.plant_sprites], self.plant_sprites)
        
        for plant in self.plant_sprites:
            plant.initialize_properties(self.water_sprites)
    
    def run(self):
        occupied_tiles = set()
        for sprite in self.visible_sprites:
            occupied_tiles.add((sprite.hitbox.x, sprite.hitbox.y))

        # update and draw
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(occupied_tiles)