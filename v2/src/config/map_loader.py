import pytmx
import pygame
from config import SCREEN_SIZE

class MapLoader:
    """Singleton to load and store map references and images"""

    _instance = None

    @classmethod
    def instance(_class):
        """Return an instance of MapLoader if there is one,
           otherwise create an instance and returns it"""
        if _class._instance is None:
            _class._instance = _class()

        return _class._instance

    def __init__(self):
        self._references: dict = {}
    
    def load(self, map_name: str) -> list:
        """Load map"""
        if not map_name in self._references:
            self.load_map(map_name)

        return self._references[map_name]

    def load_map(self, map_name: str) -> None:
        """Load a map to memmory"""
        map_path = f'{map_name}.tmx'
        self.tiled_map = pytmx.load_pygame(map_path)
        layers = []
        for current_layer, layer in enumerate(self.tiled_map.layers):
            self.current_layer = current_layer
            layers.append(self.load_layer(layer))
        
        self._references[map_name] = layers

    def load_layer(self, layer) -> pygame.surface.Surface:
        """Render a layer, 
           return true if reaches the last layer, otherwise false"""
        surface = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA, 32)
        for x, y, gid in layer:
            self.render_tile(surface, x, y, gid)

        return surface.convert_alpha()

    def render_tile(
            self, surface: pygame.surface.Surface, 
            x: int, y: int, gid: int) -> None:
        """Render a single tile in the surface"""
        tile_size = 32
        if self.tiled_map.get_tile_image_by_gid(gid):
            image = self.tiled_map.get_tile_image(x, y, self.current_layer)
            surface.blit(image, (x * tile_size, y * tile_size))

