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
    fps = 1 # each frame represents 1/10th of a year

    tile_size = 60
    world = Map(size = 16, tile_size = tile_size)

    screen_size = world.get_size() * tile_size

    pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption('Evolution')
    screen = pygame.display.get_surface()

    font = pygame.font.Font('freesansbold.ttf', tile_size // 2)

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
                if isinstance(element, Grass):
                    text = font.render(str(element.lifespan), True, (255, 255, 255))
                    text.set_alpha(200)
                    text_rect = text.get_rect(center = (element.rect.x + tile_size // 2, element.rect.y + tile_size // 2))
                    
                    screen.blit(text, text_rect)

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