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
            self._display_screen()
            self._display_stars()
            pygame.display.flip()

    def _display_stars(self):
        """显示一排排的星星"""
        self.stars = pygame.sprite.Group()
        current_x, current_y = self.settings.screen_width_restrict, self.settings.current_y
        while current_y < (self.settings.screen_height - self.settings.screen_height_restrict):
            while current_x < (self.settings.screen_width - self.settings.screen_width_restrict):
                current_x += self.settings.gap
                new_star = Star(self)
                new_star.rect.x = current_x
                new_star.rect.y = current_y
                self.stars.add(new_star)
            
            current_x = self.settings.screen_width_restrict
            current_y += 30

        self.stars.draw(self.screen)

    def _display_screen(self):
        self.screen.fill(self.settings.bg_color)



    


if __name__ == "__main__":
    sh = ShineStar()
    sh.run_game()
