import pygame
from player import Player
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Inviders")
    bg_color = (0, 0, 0)
    player = Player(screen)
    bullets = Group()
    ufos = Group()
    controls.create_army(screen, ufos)
    stats = Stats()
    scrs = Scores(screen, stats)

    while True:
        
        controls.events(screen, player, bullets)
        if stats.run_game:
            player.update_player()
            controls.update(bg_color, screen, stats, scrs, player, ufos, bullets)
            controls.update_bullets(screen, stats, scrs, ufos, bullets)
            controls.update_ufos(stats, screen, scrs, player, ufos, bullets)
    
run()