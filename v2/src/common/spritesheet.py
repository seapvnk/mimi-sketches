import pygame as pg


class Spritesheet():
    """
    Handle spritesheets
    """

    def __init__(self, image: pg.Surface):
        self._sheet = image

    def get(
            self, x: int, y: int, width: int = 32, 
            height: int = 48, scale: pg.Vector2 = pg.Vector2(1, 1)) -> pg.Surface:
        """
        Cut a spritsheet image
        """
        image = pg.Surface((width, height))
        image.blit(
            self._sheet, 
            (0, 0), (x, y, width, height)
        )
        image = pg.transform.scale(image, (width * scale.x, height * scale.y))
        image.set_colorkey((0, 0, 0))

        return image
