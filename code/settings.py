from random import random, shuffle, randint
from collections import deque

SIZE = 832
TILE_SIZE = 16
FPS = 30

DT = 0.01

_MAP_SIZE = SIZE // TILE_SIZE
MAP = [([""] * _MAP_SIZE) for _ in range(_MAP_SIZE)]

def _randomize(type, chance, min_cluster_size = 1, max_cluster_size = 1):
    # initial distribution
    for i in range(_MAP_SIZE):
        for j in range(_MAP_SIZE):
            if MAP[i][j]:
                continue
            
            if(random() < chance):
                MAP[i][j] = type
    
    # adding the clusters
    if max_cluster_size == 1:
        return

    visited = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(_MAP_SIZE):
        for j in range(_MAP_SIZE):
            if((i, j) in visited):
                continue
            visited.add((i, j))

            if(MAP[i][j] == type):
                to_visit = deque([(i, j)])
                
                cluster_size = randint(min_cluster_size, max_cluster_size) - 1
                
                while cluster_size > 0 and to_visit:
                    vi, vj = to_visit.popleft()

                    shuffle(directions)
                    for di, dj in directions:
                        vi, vj = vi + di, vj + dj
                        if(min(vi, vj) < 0 or max(vi, vj) >= _MAP_SIZE or MAP[vi][vj]):
                            vi, vj = vi - di, vj - dj
                            continue

                        MAP[vi][vj] = type
                        cluster_size -= 1
                        visited.add((vi, vj))

                        if random() < 0.75:
                            # will explore the given path only 75% of the time to prevent centralized cluster forms
                            to_visit.append((vi, vj))
                        vi, vj = vi - di, vj - dj

_randomize("w", 0.005, 50, 100)
_randomize("g", 0.05)