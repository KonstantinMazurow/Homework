import pygame
import sys
from bullet import Bullet
from ufo import Ufo
import time

def events(screen, player, bullets):
    # обработка событий
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # вправо
                if event.key == pygame.K_RIGHT:
                    player.mright = True
                # влево
                elif event.key == pygame.K_LEFT:
                    player.mleft = True
                # стрельба
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, player)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                # вправо
                if event.key == pygame.K_RIGHT:
                    player.mright = False
                # влево
                elif event.key == pygame.K_LEFT:
                    player.mleft = False

def update(bg_color,screen, stats, scrs, player, ufos, bullets):
    # обновление экрана
    screen.fill(bg_color)
    scrs.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.output()
    ufos.draw(screen)  
    pygame.display.flip()

def update_bullets(screen, stats, scrs, ufos, bullets):
    # Обновление позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions:
        for ufos in collisions.values():
            stats.score += 10 * len(ufos)
        scrs.image_score()
        check_high_score(stats, scrs)
        scrs.image_player()
    if len(ufos) == 0:
        bullets.empty()
        create_army(screen, ufos)

def player_kill(stats, screen, scrs, player, ufos, bullets):
    # столконовение пушки и пришельцев
    if stats.player_left > 0:
        stats.player_left -= 1
        scrs.image_player()
        ufos.empty()
        bullets.empty()
        create_army(screen, ufos)
        player.create_player()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_ufos(stats, screen, scrs, player, ufos, bullets):
    # обновляет позицию пришельцев
    ufos.update()
    if pygame.sprite.spritecollideany(player, ufos):
        player_kill(stats, screen, scrs, player, ufos, bullets)
    ufos_check(stats, screen, scrs, player, ufos, bullets)

def ufos_check(stats, screen, scrs, player, ufos, bullets):
    # добрались ли пришельцы до каря экрана
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            player_kill(stats, screen, scrs, player, ufos, bullets)
            break

def create_army(screen, ufos):
    # создание множество прищельцев
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    number_ufo_x = int ((700 - 2 * ufo_width) / ufo_width)
    ufo_height = ufo.rect.height
    number_ufo_y = int((800 - 500 - 2 * ufo_height) / ufo_height)

    for row_number in range(number_ufo_y):
        for ufo_number in range (number_ufo_x):
            ufo = Ufo(screen)
            ufo.x = ufo_width + (ufo_width * ufo_number)
            ufo.y = ufo_height + (ufo_height * row_number)
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.rect.height + (2 * ufo.rect.height * row_number)
            ufos.add(ufo)

def check_high_score(stats, scrs):
    # ПРоврерка на рекорд
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scrs.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

        