import pygame as pg
from config import ConfigBuilder, env

pg.init()

config_debug = ConfigBuilder()\
    .is_not_fullscreen\
    .using_debug_mode\
    .build

config_prod = ConfigBuilder()\
    .screen_size_is((pg.display.Info().current_w, pg.display.Info().current_h))\
    .build

factories = {
    'debug': config_debug,
    'prod': config_prod
}

setup = factories[env['CONFIG_SETUP']]

pg.quit()


