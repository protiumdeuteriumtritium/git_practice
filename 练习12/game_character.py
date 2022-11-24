import pygame

import sys
from settings import Settings
from ship import Ship

class GameRole:
    """创建游戏角色，并将游戏角色绘制到屏幕中央"""

    def __init__(self):
        """初始化游戏属性和资源"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = pygame.display.set_caption("游戏角色")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        self.screen.fill((230,230,230))
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    gr = GameRole()
    gr.run_game()