import pygame as pg
import sys

from map import Map

def input(events):
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)

def main():
    world = Map(32)

    SCREEN_SIZE = 768

    SCALING_FACTOR = SCREEN_SIZE / world.get_size()

    pg.init()
    pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    screen = pg.display.get_surface()

    for i in range(world.get_size()):
        for j in range(world.get_size()):
            square = pg.Rect(j * SCALING_FACTOR, i * SCALING_FACTOR, SCALING_FACTOR, SCALING_FACTOR)
            color = (81, 179, 54)
            match world.grid[i][j]:
                case 1:
                    color = (33, 139, 219)
                case 2:
                    color = (41, 128, 17)
            pg.draw.rect(screen, color, square)
            

    while True:
        input(pg.event.get())

        pg.display.update()

if __name__ == "__main__":
    main()