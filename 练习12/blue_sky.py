import sys

import pygame
from settings import Settings
from ship import Ship


class BlueSky:
    """绘制蓝色天空"""

    def __init__(self):
        """初始化属性"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("蓝色天空")

        self.ship = Ship(self)

    def draw_sky(self):
        """绘制背景"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.draw_sky()
