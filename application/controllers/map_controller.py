import pytmx
import pygame

class MapController:
    """Class to controll map rendering and switching"""

    def __init__(self, surface: pygame.surface.Surface, map_name: str):
        self.current_map = map_name
        self._surface: pygame.surface.Surface = surface
        self.load_map(map_name)

    def load_map(self, map_name: str) -> None:
        """Load a map to memmory and reset state"""
        map_path = f'{map_name}.tmx'
        self.current_layer = 0
        self.tiled_map = pytmx.load_pygame(map_path)

    def render_layers(self, n: int = 100) -> None:
        """Render many layers"""
        while not self.render_layer() and self.current_layer + 1 != n: pass

    def render_layer(self) -> bool:
        """Render a layer, 
           return true if reaches the last layer, otherwise false"""
        layer = self.tiled_map.layers[self.current_layer]
        for x, y, gid in layer:
           self.render_tile(x, y, gid)

        return self.next_layer()

    def render_tile(self, x: int, y: int, gid: int) -> None:
        """Render a single tile in the surface"""
        tile_size = 32
        if self.tiled_map.get_tile_image_by_gid(gid):
            image = self.tiled_map.get_tile_image(x, y, self.current_layer)
            self._surface.blit(image, (x * tile_size, y * tile_size))

    def next_layer(self) -> bool:
        """Move to next layer, 
           return True if reaches the last layer, otherwise false"""
        if self.current_layer + 1 == len(self.tiled_map.layers):
            self.current_layer = 0
            return True

        self.current_layer += 1
        return False


