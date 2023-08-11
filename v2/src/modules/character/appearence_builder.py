from __future__ import annotations
from common import Image, Spritesheet
from modules.character import *
import pygame as pg


class AppearenceBuilder:
    """
    Initializate appearence instance
    """

    def __init__(self, uid: int):
        self._appearence = Appearence(uid)

    @property
    def build(self) -> Appearence:
        """
        Return the appearence instance
        """
        return self._appearence
    
    def body_scale(self, body_scale: list) -> AppearenceBuilder:
        """
        Set appearence body scale
        """
        self._appearence.body_scale = pg.Vector2(body_scale)
        return self

    def body(self, image_path: str) -> AppearenceBuilder:
        """
        Set appearence body
        """
        self._appearence.body = Spritesheet(Image.get(image_path))
        return self
    
    def outfit(self, image_path: str) -> AppearenceBuilder:
        """
        Set appearence outfit
        """
        self._appearence.outfit = Spritesheet(Image.get(image_path))
        return self
    
    def hairstyle(self, image_path: str) -> AppearenceBuilder:
        """
        Set appearence hairstyle
        """
        self._appearence.hairstyle = Spritesheet(Image.get(image_path))
        return self
    
    def accessory(self, image_path: str) -> AppearenceBuilder:
        """
        Set appearence accessory
        """
        self._appearence.accessory = Spritesheet(Image.get(image_path))
        return self