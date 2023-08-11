import pygame as pg
from scenes.scene import Scene


class SceneManager:
    """
    Manage application scenes
    """

    def __init__(self, scene: Scene):
        self._scene = scene
        self._scene.on_create()

    def update(self) -> None:
        """
        Update scene
        """
        self._scene.update()

    def next(self, scene: Scene) -> None:
        """
        Switch to another scene
        """
        self._scene.on_destroy()
        
        scene.on_create()
        self._scene = scene

    @property
    def screen(self) -> pg.Surface:
        return self._scene.render()
