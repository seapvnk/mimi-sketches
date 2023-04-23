import pygame
from config import PERSON_ANIMATIONS
from infrastructure import ImageLoader
from application import SpriteSheet, Animation
from domain.shared.model import Model

class Appearence(Model):
    """Represents person's appearence in the game and generate person image"""

    def __init__(self, uid: str):
        self._id = uid
        images = ImageLoader.instance()
        self._spritesheet = SpriteSheet(images.load('player_default1.png'))
        self._animation = Animation(self._spritesheet)
        
        for animation_name, animation, time in PERSON_ANIMATIONS:
            start, end = animation
            start = pygame.math.Vector2(start)
            self._animation.add(animation_name, start, end, time)

    def image(self, action: str) -> pygame.surface.Surface:
        return self._animation.play(action)


