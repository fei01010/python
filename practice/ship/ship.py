import pygame

class Ship:
    """管理飞船相关的类"""
    def __init__(self, sm_game):
        """初始化飞船相关的设置"""
        self.screen = sm_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sm_game.settings
        self.moving_right = False
        self.moving_left = False 
        self.moving_up = False
        self.moving_down = False

        # 加载飞船并获取其外接矩形
        self.image = pygame.image.load('image_ship/ship.bmp')
        self.rect = self.image.get_rect()

        #将飞船放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _update_ship(self):
        """更新飞船的位置"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """将飞船绘制在屏幕上指定位置"""
        self.screen.blit(self.image, self.rect)