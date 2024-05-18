"""
The Map is a square area for the ecosystem to interact with each other.
"""
import numpy as np
import random as rd
from collections import deque

from ecosystem.water import Water
from ecosystem.grass import Grass


class Map:
    def __init__(self, size = 256):
        self.size = size

        self.grid = np.zeros((size, size))

        self.initialize_chunks(Water, 0.1, 4, 8)
        self.initialize_chunks(Grass, 0.2, 1, 3)

    
    def initialize_chunks(self, ChunkType, FREQUENCY, MIN_SIZE = 1, MAX_SIZE = 1):
        # initializes different chunk types on the map in the given frequency inclusive between the given sizes

        # randomly spreading chunk centers
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                if(rd.random() < FREQUENCY and not self.grid[i][j]):
                    self.grid[i][j] = ChunkType.ID
        
        # expanding the randomly spread water breadth first
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        for i in range(self.get_size()):
            for j in range(self.get_size()):
                if((i, j) in visited):
                    continue
                visited.add((i, j))

                if(self.grid[i][j] == ChunkType.ID):
                    queue = deque([(i, j)])

                    chunk_size = rd.randint(MIN_SIZE, MAX_SIZE) - 1
                    current_chunk = set()
                    while chunk_size > 0 and queue:
                        ci, cj = queue.popleft()
                        
                        self.grid[ci][cj] = ChunkType.ID
                        current_chunk.add((ci, cj))
                        chunk_size -= 1

                        visited.add((ci, cj))

                        rd.shuffle(DIRECTIONS)
                        for di, dj in DIRECTIONS:
                            if(min(ci + di, cj + dj) < 0 or max(ci + di, cj + dj) >= self.get_size() or (ci + di, cj + dj) in current_chunk):
                                continue
                            queue.append((ci + di, cj + dj))

    def get_size(self):
        return self.size
