import pygame
from settings import TILE_SIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(f"../images/{self.name}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.hitbox = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)
        self.hitbox.center = self.rect.center