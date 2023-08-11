import pygame as pg
import os
from common import Singleton


class Image(Singleton):
    """
    Singleton to load images
    """

    def __init__(self):
        self._images = {}

    def get(self, img: str) -> pg.Surface:
        """
        Load image from memmory or from disc
        """
        path = os.path.abspath(f'./assets/images/{img}')
        if path in self._images:
            return self._images[path]
        
        return self._load(path)

    def _load(self, path: str) -> pg.Surface:
        """
        Load image from disc and save to ram
        """
        image = pg.image.load(path).convert_alpha()
        self._images[path] = image
        return image
