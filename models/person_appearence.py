import pygame
from infrastructure import ImageLoader
from application import SpriteSheet
from models.model import Model

class PersonAppearence(Model):
    """Represents person's appearence in the game and generate person image"""

    def __init__(self, uid: str):
        self._id = uid
        images = ImageLoader.instance()
        self._spritesheet = SpriteSheet(images.load('player_default1.png'))

    @property
    def image(self):
        return self._spritesheet.get(2, 1)


