import pygame
from application import EventHandler
from domain.player.player import Player
from infrastructure import ConfigLoader 

class PlayerController:
    """Class to control the current player instance"""

    def __init__(self, surface: pygame.surface.Surface, player: Player):
        self.player: Player = player
        self.surface: pygame.surface.Surface = surface
        self.status: str = 'DOWN'
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        self.running: bool = False
        self._key_map: dict = ConfigLoader.instance().load('default_keymap')

    def update(self) -> None:
        """Update player's person"""
        self.player.person.update()
    
    def render(self) -> None:
        """Render player's person"""
        self.player.render()

    def _available_keys(self, pressed: list) -> list:
        """Returns only available pressed keys"""
        key_filter = lambda key: pressed[pygame.key.key_code(key)]
        available = filter(key_filter, self._key_map.keys())

        return list(map(lambda key: self._key_map[key], available))

    def _reflect_keyboard(self, obj: dict) -> None:
        """Set keyboard config attributes to instance"""
        for prop in obj: 
            self._reflect_keyboard_key(prop, obj[prop])

    def _reflect_keyboard_key(self, prop, val) -> None:
        """Set a keyboard key attributes to instance"""
        if type(val) is list and len(val) == 2: 
            val = pygame.math.Vector2(val)

        self.__dict__[prop] = val

    def handle_player_input(self) -> None:
        """Handle inputs from player to control player's person"""
        self.direction = pygame.math.Vector2()
        self.running, self.moving = False, False
        self.animation = f'PERSON_IDLE_{self.status}'
        
        keys = self._available_keys(pygame.key.get_pressed())
        for key in sorted(keys, key=lambda k: k['priority']):
            self._reflect_keyboard(key)

        self.player.person.body.direction = self.direction
        self.player.person.body.speed_increase = self.running
        self.player.person.action = self.animation

