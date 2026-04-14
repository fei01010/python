import pygame
from pygame.sprite import Group
from star import Star
from settings import Settings

class ShineStar:
    """进行显示星星和管理其行为的类"""
    def __init__(self):
        """初始化 界面"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Shining Stars")
        self.star = Star(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.star._display_star()
            pygame.display.flip()

    def _display_stars(self):
        """显示一排排的星星"""
        stars = pygame.sprite.Group()


    


if __name__ == "__main__":
    sh = ShineStar()
    sh.run_game()
