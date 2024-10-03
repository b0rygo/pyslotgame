import sys
from setting import *
from machine import Machine
import pygame

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('SLOTGAME BY ERIC')
        self.clock = pygame.time.Clock()

        try:
            self.bg_image = pygame.image.load(BG_IMAGE_PATH)
        except pygame.error as e:
            print(f"Nie można załadować obrazu tła: {BG_IMAGE_PATH}")
            print(e)
            print("Ścieżka do obrazu tła:", BG_IMAGE_PATH)
        self.machine = Machine()
        self.delta_time = 0

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        #CZASY
        self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.start_time = pygame.time.get_ticks()

        pygame.display.update()
        self.screen.blit(self.bg_image, (0, 0))
        self.machine.update(self.delta_time)
        self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

