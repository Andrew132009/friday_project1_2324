import sys
import pygame as pg


def check_events():
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pg.display.flip()