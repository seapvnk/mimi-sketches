import pygame
from time import time
from application import SpriteSheet, ClockManager

class Animation:
    """Define animations for spritesheets"""

    def __init__(
            self, spritesheet: SpriteSheet, 
            width: int = 32, height: int = 48):
        self._spritesheet: SpriteSheet = spritesheet
        self._animations: dict = {} 
        self._index: int = 0
        self._current: str = ''
        self._width: int = width
        self._height: int = height
        self._last_played: str = ''
        self._start_animation: float = 0
        self._current_animation_time: float = 0

    def add(
            self, name: str, 
            start: pygame.math.Vector2, 
            end: int, time: float) -> None:
        """Register animation"""
        self._animations[name] = (start, end, time)

    def skip_frame(self):
        """Skip frame when clock tick get 60 2 times"""
        if time() - self._start_animation > self._current_animation_time:
            self._index += 1
            self._start_animation = time()

    def play(self, name: str) -> pygame.surface.Surface:
        """Play current animation frame"""
        start, end, animation_time = self._animations[name]
        if name != self._last_played:
            self._last_played = name
            self._index = 0
            self._start_animation = animation_time
            self._current_animation_time = animation_time

        image = self._spritesheet.get(
            start.x + (self._index * self._width),
            start.y, 
            self._width, 
            self._height
        )
        
        self.skip_frame()
        
        if self._index > end:
            self._index = 0
        
        return image


