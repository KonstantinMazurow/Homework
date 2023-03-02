import pygame

class Bullet(pygame.sprite.Sprite):
    # Создаем пулю в позиции пушки
    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 5
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Рисуем пулю
        pygame.draw.rect(self.screen, self.color, self.rect)
