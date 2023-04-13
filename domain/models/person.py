import pygame
from application import ClockManager
from domain.models.model import Model
from domain.models.person_appearence import PersonAppearence
from datetime import date

class Person(Model, pygame.sprite.Sprite):
    """Class to represents a person in the application"""

    def __init__(
            self, uid: str, surface: pygame.surface.Surface, name: str, 
            last_name: str, birthday: str, money: float, 
            is_player: bool = False):
        self._id: str = uid
        self._name: str = name
        self._last_name: str = last_name
        self._money: float = money
        self._pos: pygame.math.Vector2 = pygame.math.Vector2()
        self._dir: pygame.math.Vector2 = pygame.math.Vector2()
        
        self._is_player: bool = is_player
        
        year_birthday, month_birthday, day_birthday = list(map(int, birthday.split('-')))
        self._birthday: date = date(year_birthday, month_birthday, day_birthday)
        self._person_appearence = PersonAppearence('aa')

        self._surface: pygame.surface.Surface = surface
        self._action: str = 'PERSON_RUN_DOWN'
        self._speed: int = 200

    def update(self) -> None:
        """Update person"""
        if not self._is_player:
            pass

        self._pos += self._dir * self._speed * ClockManager.instance().dt

    def set_dir(self, direction: pygame.math.Vector2):
        """Set person's direction"""
        self._dir = direction
    
    def set_action(self, action: str) -> None:
        """Set person's action"""
        self._action = action

    def set_position(self, position: pygame.math.Vector2) -> None:
        """Set person position"""
        self._pos = position
    
    def render(self) -> None:
        """Render person appearence in the surface"""
        image = self._person_appearence.image(self._action)
        rect = pygame.Rect(self._pos.x, self._pos.y, 32, 32)

        self._surface.blit(image, rect)


