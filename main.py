import pygame
from random import uniform, randint
import os, sys

from ecosystem import Map, Water, Grass, all_elements

def input(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

def main():
    # to display on second monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-1400},{50}"

    pygame.init()
    clock = pygame.time.Clock()
    fps = 30

    tile_size = 28
    world = Map(size = 32, tile_size = tile_size)

    screen_size = world.get_size() * tile_size

    pygame.display.set_mode((screen_size, screen_size))
    screen = pygame.display.get_surface()

    ground_image = pygame.transform.scale(pygame.image.load('images/ground.png'), (tile_size, tile_size))
    

    while True:
        input(pygame.event.get())

        for i in range(world.get_size()):
            for j in range(world.get_size()):
                element = world.map[i, j]
                if element is None:
                    screen.blit(ground_image, (j * tile_size, i * tile_size))
                    continue
                screen.blit(element.image.convert(), (element.rect.x, element.rect.y))

        for grass in list(Grass.elements.values()):
            child, death = grass.update(tile_size, world.get_size())
            if child:
                world.map[int(child.rect.y / tile_size), int(child.rect.x / tile_size)] = child
            elif death:
                world.map[int(grass.rect.y / tile_size), int(grass.rect.x / tile_size)] = None

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()