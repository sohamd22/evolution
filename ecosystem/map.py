"""
The Map is a square area for the ecosystem to interact with each other.
"""

import numpy as np

class Map:
    def __init__(self, size = 256):
        self.size = size

        self.area = np.array([[None] * self.size for _ in range(self.size)])