class Stats():
    # статистика текущей игры
    def __init__(self):
        # иницмализация статистики
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        # статистика, которая изменяетсяво время игры
        self.player_left = 3
        self.score = 0