class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self._reset_stats()
        # 最高分在整个游戏周期内保留，不随每局重置
        self.high_score = 0

    def _reset_stats(self):
        """初始化在游戏运行期间的统计信息"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
