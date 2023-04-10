import pygame
from application import EventHandler
from models import Player

class PlayerController:
    """Class to control the current player instance"""

    def __init__(
            self, player: Player, event_handler: EventHandler, 
            surface: pygame.surface.Surface):
        self._player: Player = player
        self._event_handler: EventHandler = event_handler
        self._surface: pygame.surface.Surface = surface
    
    def render(self) -> None:
        """Render player's person"""
        self._player.render()

