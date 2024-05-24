import pygame as pg
import random as rd
import sys, os

from map import Map

from ecosystem.water import Water
from ecosystem.grass import Grass

types = [Water, Grass]
id_to_type = {type.ID: type for type in types}
id_to_type[0] = None

tiles = pg.sprite.Group()

def input(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)

def main():
    world = Map()

    # to display on second monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-1400},{50}"

    pg.init()

    SCREEN_SIZE = 896
    pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    screen = pg.display.get_surface()

    clock = pg.time.Clock()

    scaling_factor = SCREEN_SIZE / world.get_size()

    for i in range(world.get_size()):
        for j in range(world.get_size()):
            tile_type = id_to_type[int(world.get_map()[i][j])]
            tile = pg.Rect(j * scaling_factor, i * scaling_factor, scaling_factor, scaling_factor)
            
            if(tile_type == Water):
                tiles.add(Water(tile))
            elif(tile_type == Grass):
                tiles.add(Grass(tile, rd.randint(5, 7), rd.uniform(0.5 * scaling_factor, 1 * scaling_factor)))

    while True:
        screen.fill((81, 179, 54))

        input(pg.event.get())

        for tile in tiles:
            tile.update(screen)

        pg.display.update()

        clock.tick(60)

if __name__ == "__main__":
    main()