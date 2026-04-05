import pygame
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

    def _display_star(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.star.image, self.star.rect)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self._display_star()
            pygame.display.flip()


if __name__ == "__main__":
    sh = ShineStar()
    sh.run_game()
