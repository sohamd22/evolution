"""
Grass is at the bottom of the food chain.

They have genetic traits:
- LIFESPAN (years): how old they can get.
- MAX_HEIGHT (meters): how tall they may grow.

They have variable traits:
- age (years): measure of growth; can reproduce at 20% of lifespan given that it is greater than 1 year;
               may reach upto the LIFESPAN based on environmental factors (vicinity of Water).
- height (meters): measure of height; can absorb Water from further away as the height grows; increases
                   with age and may grow upto the MAX_HEIGHT based on environmental factors (vicinity of Water).

If found without Water for an extended duration, it is removed from the ecosystem.
"""

class Grass:
    def __init__(self, pos_x, pos_y,
                 LIFESPAN = 6, MAX_HEIGHT = 1, age = 0, height = 0):
        # position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # genetic traits
        self.MAX_HEIGHT = MAX_HEIGHT
        self.LIFESPAN = LIFESPAN

        # variable traits
        self.age = age
        self.height = height
        