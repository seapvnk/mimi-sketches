import pygame
from application import ClockManager

class Body:
    """Class to represent a body of an entity"""
    
    def __init__(self, speed: float, max_speed: float = -1):
        self.position: pygame.math.Vector2 = pygame.math.Vector2()
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        self.speed: float = speed
        self.max_speed: float = max_speed if max_speed > speed else speed * 2
        self.speed_increase: bool = False

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def update(self):
        """Update entity body"""
        speed = self.max_speed if self.speed_increase else self.speed
        dt = ClockManager.instance().dt
        self.position += self.direction * speed * dt
