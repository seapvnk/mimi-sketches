import pygame as pg
from common.spritesheet import Spritesheet


class Appearence:
    """
    Character appearence entity
    """

    def __init__(self, uid: int):
        self.id: int = uid
        self.body: Spritesheet = None
        self.outfit: Spritesheet = None
        self.hairstyle: Spritesheet = None
        self.accessory: Spritesheet = None
        self.body_scale: pg.Vector2 = None

