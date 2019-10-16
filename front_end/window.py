####

import pygame
import random

from front_end.infoground import infoground
from front_end.playground import playground


####


class Window(object):

    def __init__(self, height=600, fps=42):
        """
        Initialize pygame, window, background, font and etc.

        :param width:
        :param height:
        :param fps:
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.width      = 3 * height // 2
        self.height     = height
        self.screen     = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((200, 200, 200))

        self.info_ground = infoground.InfoGround(self.screen,
                                                 self.height // 2,
                                                 self.height, fps)

    def run(self):
        """
        The mainloop

        """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.info_ground.draw_tech_info()
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


def main():
    Window().run()


if __name__ == "__main__":
    main()
