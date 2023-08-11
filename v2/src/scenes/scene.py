from abc import ABC, abstractmethod
import pygame as pg


class Scene(ABC):
    """
    Application scene stub
    """
    
    @abstractmethod
    def on_create(self):
        """
        Scene setup
        """
        pass

    @abstractmethod
    def update(self):
        """
        Update scene
        """
        pass

    @abstractmethod
    def on_destroy(self):
        """
        Destroy scene
        """
        pass

    @abstractmethod
    def render(self) -> pg.Surface:
        """
        Render scene
        """
        pass