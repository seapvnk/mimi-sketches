import pygame
from application import EventHandler
from domain.models import Player

class PlayerController:
    """Class to control the current player instance"""

    def __init__(self, surface: pygame.surface.Surface, player: Player):
        self._player: Player = player
        self._surface: pygame.surface.Surface = surface
        self._status: str = 'DOWN'
        self._direction: pygame.math.Vector2 = pygame.math.Vector2()
        self._running: bool = False

    def update(self) -> None:
        """Update player's person"""
        self._player.person.update()
    
    def render(self) -> None:
        """Render player's person"""
        self._player.render()

    def handle_player_input(self) -> None:
        """Handle inputs from player to control player's person"""
        keys = pygame.key.get_pressed()
        self._direction = pygame.math.Vector2()

        if keys[pygame.K_d]:
            self._running = True
            self._direction.x = 1
            self._status = 'RIGHT'
        elif keys[pygame.K_a]:
            self._running = True
            self._direction.x = -1
            self._status = 'LEFT'
        elif keys[pygame.K_s]:
            self._running = True
            self._direction.y = 1
            self._status = 'DOWN'
        elif keys[pygame.K_w]:
            self._running = True
            self._direction.y = -1
            self._status = 'UP'
        else:
            self._running = False

        animation = f'PERSON_IDLE_{self._status}'
        if self._running:
            animation = f'PERSON_RUN_{self._status}'
        
        self._player.person.set_dir(self._direction)
        self._player.person.set_action(animation)

