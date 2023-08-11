import pygame as pg
from config import setup
from common import SceneManager
from scenes import TitleScreenScene


pg.init()

if setup.is_fullscren:
    screen = pg.display.set_mode(
        setup.screen_size,
        pg.NOFRAME | 
        pg.FULLSCREEN
    )
else:
    screen = pg.display.set_mode(
        setup.screen_size, 
        pg.NOFRAME
    )
    
pg.display.set_caption(setup.name)

running = True
scene_manager = SceneManager(TitleScreenScene())

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(scene_manager.screen, (0, 0))
    pg.display.flip()

pg.quit()