"""
Water is a static element of variable size and its only purpose is to be used by organisms in the ecosystem to 
sustain themselves.
"""

class Water:
    ID = 1

    def __init__(self, pos_x, pos_y,
                SIZE = 5):
        self.pos_x = pos_x
        self.pos_y = pos_y