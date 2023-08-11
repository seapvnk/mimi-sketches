import pygame as pg
from scenes import Scene
from config import setup


class TitleScreenScene(Scene):
    """Application scene stub"""
    def __init__(self):
        self.ctx: dict = {}
        self.surface = pg.Surface(setup.screen_size)

    def on_create(self, ctx: dict = {}):
        """Scene setup"""
        self.ctx = ctx

    def update(self):
        """Update scene"""
        pass

    def on_destroy(self):
        """Destroy scene"""
        pass

    def render(self) -> pg.Surface:
        self.surface.fill((100, 100, 100))
        pg.draw.circle(self.surface, (0, 0, 255), (250, 250), 75)
        
        return self.surface