import numpy as np
from random import random, shuffle, randint
import math
import pygame

from collections import deque

all_elements = {}

class Water:
    chance = 0.05

    min_cluster_size = 4
    max_cluster_size = 8

    images = ['images/water.png']
    elements = {}

    def __init__(self, tile_size, position):
        self.image = pygame.transform.scale(pygame.image.load(self.images[0]), (tile_size, tile_size))
        self.rect = self.image.get_rect(x = position[0] * tile_size, y = position[1] * tile_size)

        self.elements[(self.rect.x, self.rect.y)] = self
        all_elements[(self.rect.x, self.rect.y)] = self
    
    def __str__(self):
        return "W"

class Grass:
    max_reproduction_factor = 0.8

    mutation_chance = 0.01

    chance = 0.1

    images = ['images/grass-young.png', 'images/grass.png', 'images/grass-old.png', 'images/grass-dying.png']
    elements = {}

    def __init__(self, tile_size, position, lifespan = None):
        self.lifespan = lifespan or randint(50, 70) / 10
        self.age = 0

        self.reproduction_factor = Grass.max_reproduction_factor

        x, y = position[0] * tile_size, position[1] * tile_size

        directions = [(0, tile_size), (tile_size, 0), (0, -tile_size), (-tile_size, 0)]
        visited = set([(x, y)])

        to_visit = deque([(x + dx, y + dy) for dx, dy in directions])
        while to_visit:
            vx, vy = to_visit.popleft()
            visited.add((vx, vy))

            if (vx, vy) in Water.elements:
                self.vicinity_to_water = math.dist((x, y), (vx, vy)) / tile_size
                break
            
            for dx, dy in directions:
                vx, vy = vx + dx, vy + dy
                if(min(vx, vy) < 0 or (vx, vy) in visited):
                    vx, vy = vx - dx, vy - dy
                    continue
                to_visit.append((vx, vy))
                vx, vy = vx - dx, vy - dy

        self.image = pygame.transform.scale(pygame.image.load(self.images[0]), (tile_size, tile_size))
        self.rect = self.image.get_rect(x = x, y = y)

        self.elements[(self.rect.x, self.rect.y)] = self
        all_elements[(self.rect.x, self.rect.y)] = self
    
    def reproduce(self, tile_size, map_size):
        if(self.age < 0.2 * self.lifespan or self.age >= 0.8 * self.lifespan):
            return

        reproduction_chance = self.get_reproduction_chance(tile_size, map_size)
        
        if random() < reproduction_chance:
            directions = [(0, tile_size), (tile_size, 0), (0, -tile_size), (-tile_size, 0), (tile_size, tile_size), (tile_size, -tile_size), (-tile_size, -tile_size), (-tile_size, tile_size)]

            shuffle(directions)
            possibilities = [(self.rect.x + dx, self.rect.y + dy) for dx, dy in directions]

            for px, py in possibilities:
                if min(px, py) < 0 or max(px, py) >= (map_size * tile_size) or (px, py) in all_elements:
                    continue
                lifespan_mutation = (randint(-5, 5) / 10) if random() < Grass.mutation_chance else 0
                child = Grass(tile_size, (px / tile_size, py / tile_size), round(self.lifespan + lifespan_mutation, 1))
                self.reproduction_factor = 0
                return child

    def get_reproduction_chance(self, tile_size, map_size):
        water_importance = 3

        surrounding_grass_factor = 1
        affected_range = 2

        directions = [(0, tile_size), (tile_size, 0), (0, -tile_size), (-tile_size, 0)]
        visited = set([(self.rect.x, self.rect.y)])

        to_visit = deque([(self.rect.x + dx, self.rect.y + dy) for dx, dy in directions])
        
        for i in range(affected_range):
            current_length = len(to_visit)

            for _ in range(current_length):
                vx, vy = to_visit.popleft()
                visited.add((vx, vy))

                if (vx, vy) in Grass.elements:
                    surrounding_grass_factor += (affected_range - i)
                
                for dx, dy in directions:
                    vx, vy = vx + dx, vy + dy
                    if(min(vx, vy) < 0 or (vx, vy) in visited):
                        vx, vy = vx - dx, vy - dy
                        continue
                    to_visit.append((vx, vy))
                    vx, vy = vx - dx, vy - dy

        reproduction_chance = self.reproduction_factor / (water_importance * self.vicinity_to_water * surrounding_grass_factor)

    def update(self, tile_size, map_size):
        self.age += 0.1

        if self.reproduction_factor < Grass.max_reproduction_factor:
            self.reproduction_factor += Grass.max_reproduction_factor / 4

        if self.age >= self.lifespan:
            Grass.elements.pop((self.rect.x, self.rect.y))
            all_elements.pop((self.rect.x, self.rect.y))
            del self
            return (None, True)
        if self.age >= 0.8 * self.lifespan:
            self.image = pygame.transform.scale(pygame.image.load(self.images[3]), (tile_size, tile_size))
        elif self.age >= 0.5 * self.lifespan:
            self.image = pygame.transform.scale(pygame.image.load(self.images[2]), (tile_size, tile_size))
        elif self.age >= 0.2 * self.lifespan:
            self.image = pygame.transform.scale(pygame.image.load(self.images[1]), (tile_size, tile_size))

        child = self.reproduce(tile_size, map_size)

        return (child, False)

    def __str__(self):
        return "G"

class Rabbit:
    def __init__(self, position, lifespan, speed):
        pass

class Map:
    def __init__(self, size = 64, tile_size = 8):
        self.size = size

        self.map = np.array([[None] * self.size for _ in range(self.size)])

        self.randomize(Water, tile_size, Water.min_cluster_size, Water.max_cluster_size)
        self.randomize(Grass, tile_size)

    def randomize(self, Type, tile_size, min_cluster_size = 1, max_cluster_size = 1):
        # initial distribution
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i, j]:
                    continue
                
                if(random() < Type.chance):
                    self.map[i, j] = Type(tile_size, (j, i))
        
        # adding the clusters
        if max_cluster_size == 1:
            return

        visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(self.size):
            for j in range(self.size):
                if((i, j) in visited):
                    continue
                visited.add((i, j))

                if(isinstance(self.map[i, j], Type)):
                    to_visit = deque([(i, j)])
                    
                    cluster_size = randint(min_cluster_size, max_cluster_size) - 1
                    current_cluster = set()
                    
                    while cluster_size > 0 and to_visit:
                        vi, vj = to_visit.popleft()
                        
                        self.map[vi, vj] = Type(tile_size, (vj, vi))
                        current_cluster.add((vi, vj))
                        cluster_size -= 1

                        visited.add((vi, vj))

                        shuffle(directions)
                        for di, dj in directions:
                            vi, vj = vi + di, vj + dj
                            if(min(vi, vj) < 0 or max(vi, vj) >= self.size or (vi, vj) in current_cluster or self.map[vi, vj]):
                                vi, vj = vi - di, vj - dj
                                continue
                            to_visit.append((vi, vj))
                            vi, vj = vi - di, vj - dj

    def get_size(self):
        return self.size
    
    def get_map(self):
        return self.map.copy()
