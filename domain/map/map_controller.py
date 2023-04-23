import pygame
from infrastructure.map_loader import MapLoader

class MapController:
    """Setup, switch and render application maps"""

    def __init__(self, surface: pygame.surface.Surface, map_name: str):
        self._surface = surface
        self.map_loader = MapLoader.instance()
        self.map = self.map_loader.load(map_name)

    @property
    def last_layer(self):
        return len(self.map)

    def render(self, start: int, end: int = -1):
        """Render layers in given range"""
        end = end if end > 0 else start
        start = start if end != start else 0

        for layer in self.map[start:end]:
            self._surface.blit(layer, (0,0))

