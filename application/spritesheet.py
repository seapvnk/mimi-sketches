import pygame

class SpriteSheet():
    """Handle spritesheets"""

    def __init__(self, image: pygame.surface.Surface):
        self.sheet = image

    def get(
            self, col: int, row: int, width: int = 32, 
            height: int = 64, scale: float = 1.0) -> pygame.surface.Surface:
        """Cut a spritsheet image"""
        image = pygame.Surface((width, height))
        image.blit(
            self.sheet, 
            (0, 0), ((row * width), (col * height), width, height)
        )
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))

        return image


