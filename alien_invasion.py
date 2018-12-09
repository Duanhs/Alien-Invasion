import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():

    pygame.init()
    """创建设置实例"""
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.screen_color
    #创建飞船实例
    ship = Ship(screen)

    while True:
        for envet in pygame.event.get():
            if envet == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()