import pygame

CLOCKS_TO_GAME_SECONDS: int = 5
CLOCKS_TO_GAME_PHYSICS_DT: int = 1000
FPS: int = 60

class ClockManager:
    """Controll application state"""
    _instance = None

    @classmethod
    def instance(_class):
        """Return an instance of ImageLoader if there is one,
           otherwise create an instance and returns it"""
        if _class._instance is None:
            _class._instance = _class()

        return _class._instance

    def __init__(self):
        self.clock: pygame.time.Clock = pygame.time.Clock()

    @property
    def fps(self):
        return self.clock.tick()

    @property
    def dt(self):
        return self.clock.tick(FPS) / CLOCKS_TO_GAME_PHYSICS_DT


