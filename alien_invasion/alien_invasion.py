import sys
from time import sleep
import pygame
from button import Button
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import ScoreBoard
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # 如果你喜欢全屏模式
        """
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        anyway,仅仅记录，后续有需求再相应更改
        """
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 创建一个用于存储游戏统计信息的实例, 并创建一个记分牌
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.play_button = Button(self, "Play")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # 让游戏一开始处于非活跃状态
        self.game_active = False
        
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(self.mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家点击play时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 还原游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置统计信息
            self.stats._reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            #清空列表
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.centre_ship()

            # 隐藏光标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key ==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        """
        print(len(self.bullets))
        """ 
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人的碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果是， 就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        """这里的True表示发生碰撞时删除对应的子弹和外星人
        """
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # 删除现有的子弹并创建新的外星舰队
            self.bullets.empty()
            self._create_fleet() 
            self.settings.increase_speed()   
            self.stats.level += 1
            self.sb.prep_level()     

    def _ship_hit(self):
        """响应飞船与外星人的碰撞"""
        # ship_left -1
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # 清空外星人编组和子弹编组
            self.bullets.empty()
            self.aliens.empty()

            # 创建新的外星舰队， 并将飞船置于屏幕底部中央
            self._create_fleet()
            self.ship.centre_ship()

            # 暂停
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """检测是否有外星人到达了屏幕的底部边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 操作与飞船与外星人碰撞相同
                self._ship_hit()
                break


    def _update_aliens(self):
        """更新外形舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人与飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外形人到达屏幕的下边缘
        self._check_aliens_bottom()

    def _create_fleet(self):
        """创建一个外形舰队"""
        # 创建一个外星人, 再不断添加, 直到没有空间添加外星人为止
        # 外星人的间距为外星人的宽度和高度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        
        while(current_y < (self.settings.screen_height - 3 * alien_height)):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # 放置完每行外星人后重置currentx，y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并将其加入外星舰队"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x, new_alien.rect.y = x_position, y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """"将整个外形舰队向下移动，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()