import pygame
from config import PERSON_ANIMATIONS
from infrastructure import ImageLoader
from application import SpriteSheet, Animation
from domain.shared.model import Model

class Appearence(Model):
    """Represents person's appearence in the game and generate person image"""

    def __init__(
            self, uid: str, body: str, eyes: str, 
            hairstyle: str, outfit: str, 
            accessory: str = '', is_kid: bool = False):
        self._id = uid
        self.image_loader = ImageLoader.instance()
        
        self.body = body
        self.eyes = eyes
        self.hairstyle = hairstyle
        self.outfit = outfit
        self.is_kid = is_kid
        self.accessory = accessory if not self.is_kid else ''

        self.create_spritesheet()
        self._animation = Animation(self._spritesheet)
        
        for animation_name, animation, time in PERSON_ANIMATIONS:
            start, end = animation
            start = pygame.math.Vector2(start)
            self._animation.add(animation_name, start, end, time)

    def create_spritesheet(self) -> None:
        """Generate spritesheet for person appearence"""
        steps = [
            self.load_image('Bodies', self.body),
            self.load_image('Eyes', self.eyes),
            self.load_image('Outfits', self.outfit),
            self.load_image('Hairstyles', self.hairstyle)
        ]

        if not self.is_kid and self.accessory != '':
            steps.append(self.load_image('Accessories', self.accessory))

        rect = steps[0].get_rect()
        sprite_img = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA, 32)
        for step in steps:
            sprite_img.blit(step, (0, 0))
        
        self._spritesheet = SpriteSheet(sprite_img.convert_alpha())

    def load_image(self, folder: str, item: str) -> pygame.surface.Surface:
        """Load spritesheet image"""
        sufix = '_kids/32x32/' if self.is_kid else '/32x32/'
        return self.image_loader.load(folder + sufix + item)
        

    def image(self, action: str) -> pygame.surface.Surface:
        """Return the current image of person appearence animation"""
        return self._animation.play(action)


