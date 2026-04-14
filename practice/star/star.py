import pygame
from pathlib import Path
from pygame.sprite import Sprite

class Star(Sprite):
    """管理星星的类"""
    def __init__(self, sh):
        """初始化星星并设置其位置"""
        super().__init__()
        self.screen = sh.screen
        self.settings = sh.settings

        self.image = pygame.image.load("star/images_2/star.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width * 0.5
        self.rect.y = self.settings.screen_height * 0.5

    def _display_star(self):
        """绘出一个星星的图像"""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.image, self.rect)
