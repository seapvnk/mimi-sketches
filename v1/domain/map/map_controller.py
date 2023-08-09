import pygame
from config import COLLISION_LAYERS, SCREEN_SIZE
from infrastructure.map_loader import MapLoader

class MapController:
    """Setup, switch and render application maps"""

    def __init__(self, surface: pygame.surface.Surface, map_name: str):
        self._surface = surface
        self.map_loader = MapLoader.instance()
        self.map = self.map_loader.load(map_name)
        self._collision_mask: pygame.surface.Surface = None

    @property
    def last_layer(self) -> int:
        return len(self.map)

    @property
    def collision_mask(self) -> pygame.mask.Mask:
        if not self._collision_mask is None:
            return self._collision_mask

        collision_surface = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA, 32)
        for index in COLLISION_LAYERS:
            collision_surface.blit(self.map[index], (0, 0))

        self._collision_mask = pygame.mask.from_surface(collision_surface)
        return self._collision_mask

    def render(self, start: int, end: int = -1) -> None:
        """Render layers in given range"""
        end = end if end > 0 else start
        start = start if end != start else 0

        for layer in self.map[start:end]:
            self._surface.blit(layer, (0,0))

