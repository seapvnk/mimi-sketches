import pygame

CLOCKS_TO_GAME_SECONDS: int = 5
CLOCKS_TO_GAME_PHYSICS_DT: int = 1000
FPS: int = 60

class ClockManager:
    """Controll application state"""

    def __init__(self):
        self.clock: pygame.time.Clock = pygame.time.Clock()

    @property
    def dt(self):
        return self.clock.tick(FPS) / CLOCKS_TO_GAME_PHYSICS_DT


