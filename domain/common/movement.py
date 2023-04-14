import pygame
from application import ClockManager

class Movement:
    """Class to represent movement of an entity"""
    
    def __init__(
            self, 
            position: pygame.math.Vector2, direction: pygame.math.Vector2,
            speed: float):
        self.position: pygame.math.Vector2 = position
        self.direction: pygame.math.Vector2 = direction
        self.speed: float = speed

    def update(self):
        """Update entity movement"""
        dt = ClockManager.instance().dt
        self.position += self.direction * self.speed * dt
