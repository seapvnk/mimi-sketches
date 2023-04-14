import pygame
from config import SCREEN_SIZE
from application import SpriteSheet
from domain.models import Player

MAX_ZOOM = 100
MIN_ZOOM = 38

class Camera:
    """Camera to follow player's person"""

    def __init__(self, surface: pygame.surface.Surface, player: Player):
        self._player: Player = player
        self._surface: pygame.surface.Surface = surface
        self._zoom: float = 4

    def update(self, controls: pygame.event.Event) -> None:
        """Update camera using mouse scroll"""
        to_update = 2 * (controls.y / 10)
        updated_value = self._zoom + to_update

        int_zoom = int(updated_value * 10)
        if int_zoom <= MIN_ZOOM or int_zoom >= MAX_ZOOM:
            return

        self._zoom = updated_value

    def render(self) -> None:
        """Render camera image in surface"""
        w, h = SCREEN_SIZE
        zoom = self._zoom

        rectx = self._player.person.rect.centerx
        recty = self._player.person.rect.centery

        offset_x = w // zoom
        offset_y = h // zoom

        sheet = SpriteSheet(self._surface)
        camera = sheet.get(
            rectx - offset_x,
            recty - offset_y,
            offset_x * 2,
            offset_y * 2
        )
        

        camera = pygame.transform.scale(camera, SCREEN_SIZE)
        self._surface.fill((0, 0, 0))
        self._surface.blit(camera, (0, 0, w, h))

