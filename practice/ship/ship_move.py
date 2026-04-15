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
            self.settings.screen_width, self.settings.screen_height)
        self.ship = Ship()
        self.status = False

    def run_game(self):
        """进行游戏的进程"""

        self.update_screen()

    def _check_event(self):
        """对键盘和鼠标进行响应"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_eevnt(event)

    def _check_keydown_event(self, event):
        """响应键盘按下"""
        if event.key == pygame.K_RIGHT:
            if self.status and 

        

    def update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)