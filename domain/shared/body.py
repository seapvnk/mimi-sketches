import pygame
from application import ClockManager

class Body:
    """Class to represent a body of an entity"""
    
    def __init__(
            self, shape: pygame.mask.Mask,
            speed: float, max_speed: float = -1):
        self.position: pygame.math.Vector2 = pygame.math.Vector2()
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        self.shape: pygame.mask.Mask = shape
        self.speed: float = speed
        self.max_speed: float = max_speed if max_speed > speed else speed * 2
        self.speed_increase: bool = False

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def update(self, world: pygame.mask.Mask):
        """Update entity body"""
        speed = self.max_speed if self.speed_increase else self.speed
        dt = ClockManager.instance().dt
        n_position = self.position + self.direction * speed * dt
        overlap_area = world.overlap_area(self.shape, (n_position.x, n_position.y))
        tolerance = 410

        if overlap_area == 0:
            self.position = n_position
        elif overlap_area < tolerance:
            n_position.x = (self.position.x + n_position.x) / 2
            n_position.y = (self.position.y + n_position.y) / 2
        
            self.position = n_position
            

