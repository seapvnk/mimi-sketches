import pygame as pg
from common.spritesheet import Spritesheet


class Map:
    """
    Map entity
    """

    def __init__(self, uid: int):
        self.id: int = uid
        self.name: str = ""
