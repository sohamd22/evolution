"""
Rabbits are herbivores and therefore may eat:
- Grass

They have genetic traits:
- LIFESPAN (years): how old they can get.
- MAX_SPEED (meters / second): how fast they can get.
- MAX_ENDURANCE: how long they can perform activities without getting hungry / thirsty.
- MAX_VISION (meters): how far they can see in a 360 degree radius.

They have variable traits that may reach the corresponding maximums based on environmental factors 
(vicinity of Food and Water):

- age (years): measure of growth; can reproduce at 20% of lifespan given that it is greater than 1 year; naturally
               increases with time.
- speed (meters / second): measure of fastness; determines how fast it may move; higher speed generally means
                           lower endurance; increases with age.
- endurance: measure of stamina; determines how long before it gets hungry and thirsty; higher endurance generally
             means lower speed; increases with age.
- vision (meters): measure of sight; determines how far it can see; increases with age.
- hunger: determines level of hunger; if high enough, may negatively impact speed or vision and lead to death;
          increases naturally at a rate determined by the endurance and increases quicker when moving at faster
           speeds; may be reduced by consuming Food.
- thirst: determines level of thirst; if high enough, may negatively impact speed or vision and lead to death;
          increases naturally at a rate determined by the endurance and increases quicker when moving at faster
           speeds; may be reduced by consuming Water.
                           
If found very hungry or thirsty for an extended duration, it is removed from the ecosystem.
"""


class Rabbit:
    def __init__(self, pos_x, pos_y,
                 LIFESPAN = 6, MAX_SPEED = 1, MAX_ENDURANCE = 1, MAX_VISION = 1, 
                 age = 0, speed = 0, endurance = 0, vision = 0):
        # position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # genetic traits
        self.MAX_SPEED = MAX_SPEED
        self.MAX_ENDURANCE = MAX_ENDURANCE
        self.MAX_VISION = MAX_VISION
        self.LIFESPAN = LIFESPAN

        # variable traits
        self.age = age
        self.speed = speed
        self.endurance = endurance
        self.vision = vision
        self.hunger = 0
        self.thirst = 0
