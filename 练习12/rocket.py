import sys

import pygame
from settings import Settings
from ship import Ship

class Rocket:
    """在屏幕底部中央显示一个火箭，使火箭可以上下左右移动，确保不会移动到屏幕外部。"""
    def __init__(self):
        """管理游戏资源和行为"""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("火箭")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """更新屏幕上的图像并切换到新屏幕"""
        self.screen.fill((230,230,230))
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    r = Rocket()
    r.run_game()