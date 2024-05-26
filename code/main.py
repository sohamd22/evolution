import pygame, os, sys
from settings import *

from ecosystem import Ecosystem

# to display on second monitor
# os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-1400},{30}"

class Simulation:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((SIZE, SIZE))
        pygame.display.set_caption('Ecosystem')
        self.clock = pygame.time.Clock()

        self.ecosystem = Ecosystem()
    
    def run(self):
        ground_color = (196,244,108)

        while True:
            # event management
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(ground_color)
            self.ecosystem.run()

            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()