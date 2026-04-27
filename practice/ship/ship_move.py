import sys
import pygame

from settings import Settings
from ship import Ship

class ShipMove:
    """管理飞船移动的类"""
    def __init__(self):
        """初始化该程序的一些些"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Moving your ship!")
        self.ship = Ship(self)

    def run_game(self):
        """进行游戏的进程"""
        while True:
            self._check_event()
            self.update_screen()
            self.clock.tick(self.settings.fps)

    def _check_event(self):
        """对键盘和鼠标进行响应"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            

    def update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship._update_ship()
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    """创建游戏实例并开始游戏"""
    sm_game = ShipMove()
    sm_game.run_game()
