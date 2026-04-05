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

        image_path = Path(__file__).parent / "images" / "star.bmp"
        self.image = pygame.image.load(str(image_path))
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width * 0.5
        self.rect.y = self.settings.screen_height * 0.5




