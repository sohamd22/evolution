"""
Rabbits are herbivores and therefore may eat:
- Grass
"""

from animal import Animal
class Rabbit(Animal):
    def __init__(self, pos_x, pos_y,
                 LIFESPAN = 6, MAX_SPEED = 1, MAX_ENDURANCE = 1, MAX_VISION = 1, 
                 age = 0, speed = 0, endurance = 0, vision = 0):
        self.super(pos_x, pos_y, LIFESPAN, MAX_SPEED, MAX_ENDURANCE, MAX_VISION, age, speed, endurance, vision)
