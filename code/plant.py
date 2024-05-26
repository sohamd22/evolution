import pygame
from random import random, randint, shuffle
from settings import TILE_SIZE

from organism import Organism

class Plant(Organism):
    name = "plant"

    max_reproduction_factor = 5e-2

    spread = 2

    def __init__(self, pos, groups, plant_sprites, lifespan = 0):
        super().__init__(pos, groups, lifespan or randint(5, 7), 3)

        self.plant_sprites = plant_sprites

        self.reproduction_factor = self.max_reproduction_factor

        self.crowd_importance = (self.sense_range) * 3e-1
        self.water_importance = (self.sense_range) * 5e-1

        self.water_nutrition_level = 1e-2

    def initialize_properties(self, water_sprites):
        for water in water_sprites:
            dist_tiles = pygame.math.Vector2(self.hitbox.centerx, self.hitbox.centery).distance_to((water.hitbox.centerx, water.hitbox.centery)) / TILE_SIZE

            if dist_tiles <= self.sense_range:
                self.water_nutrition_level += self.sense_range - dist_tiles + 1
    
    def calculate_reproduction_chance(self):
        crowd_factor = 1
        for plant in self.plant_sprites:
            if plant == self:
                continue

            dist_tiles = pygame.math.Vector2(self.hitbox.centerx, self.hitbox.centery).distance_to((plant.hitbox.centerx, plant.hitbox.centery)) / TILE_SIZE
            
            if dist_tiles <= self.sense_range:
                crowd_factor += (1 - plant.age / plant.lifespan) * (self.sense_range - dist_tiles + 1)

        return (self.reproduction_factor * self.water_importance * self.water_nutrition_level) / (self.crowd_importance * crowd_factor)

    def reproduce(self, occupied_tiles):
        if self.reproduction_factor < self.max_reproduction_factor:
            self.reproduction_factor += 0.1 * self.max_reproduction_factor
            return
        if self.stage != "adult":
            return
        
        reproduction_chance = self.calculate_reproduction_chance()

        if random() < reproduction_chance:
            directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
            shuffle(directions)

            for dx, dy in directions:
                x = self.hitbox.left + TILE_SIZE * dx * randint(1, self.spread)
                y = self.hitbox.top + TILE_SIZE * dy * randint(1, self.spread)

                possible = True

                if (x, y) in occupied_tiles:
                    possible = False
                    break
                
                if not possible:
                    continue

                lifespan_mutation = 0
                if random() < self.mutation_chance:
                    lifespan_mutation = randint(-5, 5) / 10

                self.reproduction_factor = 0
                Plant((x, y), self.groups, self.plant_sprites, self.lifespan + lifespan_mutation)                
                break
                    