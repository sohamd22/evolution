import pygame
from settings import DT

class Organism(pygame.sprite.Sprite):
    mutation_chance = 0.01

    def __init__(self, pos, groups, lifespan, sense_range):
        super().__init__(groups)

        self.groups = groups

        self.lifespan = lifespan
        self.age = 0
        self.stage = "young"

        self.sense_range = sense_range

        self.image = pygame.image.load(f"../images/{self.name}-{self.stage}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.hitbox = pygame.Rect(0, 0, self.rect.width, self.rect.height)
        self.hitbox.center = self.rect.center
    
    def update_image(self):
        previous_stage = self.stage

        if self.age >= 0.8 * self.lifespan:
            self.stage = "old"
        elif self.age >= 0.2 * self.lifespan:
            self.stage = "adult"
        
        if self.stage == previous_stage:
            return
        
        self.image = pygame.image.load(f"../images/{self.name}-{self.stage}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.rect.x , self.rect.y))
    
    def update(self, occupied_tiles):
        self.age += DT

        self.update_image()

        self.reproduce(occupied_tiles)

        if self.age >= self.lifespan:
            self.kill()
            del self
            return
        
        