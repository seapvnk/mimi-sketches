import pygame
import os

class ImageLoader:
    """Singleton to load and store image references"""

    _instance = None

    @classmethod
    def instance(_class):
        """Return an instance of ImageLoader if there is one,
           otherwise create an instance and returns it"""
        if _class._instance is None:
            _class._instance = _class()

        return _class._instance

    def __init__(self):
        self._references: dict = {}

    def load(self, img: str) -> pygame.surface.Surface:
        """Load image to memory"""
        image_path = os.path.abspath(f'./resources/assets/images/{img}')
        if image_path in self._references:
            return self._references[image_path]

        image = pygame.image.load(image_path).convert_alpha()
        self._references[image_path] = image

        return image

    def delete(self, img_path: str) -> None:
        """Unload image"""
        del self._references[img_path]

