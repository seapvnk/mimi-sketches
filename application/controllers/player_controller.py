import pygame
from application import EventHandler
from domain.models import Player

class PlayerController:
    """Class to control the current player instance"""

    def __init__(self, surface: pygame.surface.Surface, player: Player):
        self.player: Player = player
        self.surface: pygame.surface.Surface = surface
        self.status: str = 'DOWN'
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        self.running: bool = False

    def update(self) -> None:
        """Update player's person"""
        self.player.person.update()
    
    def render(self) -> None:
        """Render player's person"""
        self.player.render()

    def handle_player_input(self) -> None:
        """Handle inputs from player to control player's person"""
        keys = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2()

        if keys[pygame.K_d]:
            self.running = True
            self.direction.x = 1
            self.status = 'RIGHT'
        elif keys[pygame.K_a]:
            self.running = True
            self.direction.x = -1
            self.status = 'LEFT'
        elif keys[pygame.K_s]:
            self.running = True
            self.direction.y = 1
            self.status = 'DOWN'
        elif keys[pygame.K_w]:
            self.running = True
            self.direction.y = -1
            self.status = 'UP'
        else:
            self.running = False

        animation = f'PERSON_IDLE_{self.status}'
        if self.running:
            animation = f'PERSON_RUN_{self.status}'
        
        self.player.person.direction = self.direction
        self.player.person.action = animation

