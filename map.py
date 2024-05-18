"""
The Map is a square area for the ecosystem to interact with each other.
"""
import numpy as np
import random as rd
import pygame as pg
from collections import deque

from ecosystem.water import Water


class Map:
    def __init__(self, size = 256):
        self.size = size

        self.grid = np.zeros((self.size, self.size))

        self.initialize_water_chunks()
        
        print(list(self.grid.flatten()).count(1) / (self.size * self.size))
    
    def initialize_water_chunks(self):
        # initializes the chunks of water on the map

        # setting parameters for each water chunk
        MIN_CHUNK_SIZE = 4
        MAX_CHUNK_SIZE = 9

        # rough percent of map covered in water chunks
        WATER_CHUNK_PERCENTAGE = 0.6 / ((MIN_CHUNK_SIZE + MAX_CHUNK_SIZE) / 2)

        # randomly spreading water
        for i in range(self.size):
            for j in range(self.size):
                if(rd.random() < WATER_CHUNK_PERCENTAGE):
                    self.grid[i][j] = Water.ID
        
        # expanding the randomly spread water breadth first
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        for i in range(self.size):
            for j in range(self.size):
                if((i, j) in visited):
                    continue
                visited.add((i, j))

                if(self.grid[i][j] == Water.ID):
                    queue = deque([(i, j)])

                    chunk_size = rd.randint(MIN_CHUNK_SIZE, MAX_CHUNK_SIZE) - 1
                    current_chunk = set()
                    while chunk_size > 0 and queue:
                        wi, wj = queue.popleft()
                        
                        self.grid[wi][wj] = Water.ID
                        current_chunk.add((wi, wj))
                        chunk_size -= 1

                        visited.add((wi, wj))

                        rd.shuffle(DIRECTIONS)
                        for di, dj in DIRECTIONS:
                            if(min(wi + di, wj + dj) < 0 or max(wi + di, wj + dj) >= self.size or (wi + di, wj + dj) in current_chunk):
                                continue
                            queue.append((wi + di, wj + dj))

    def draw(self):
        pg.init()
        pass
