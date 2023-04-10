import pygame
from models.model import Model
from models.person_appearence import PersonAppearence
from datetime import date

class Person(Model, pygame.sprite.Sprite):
    """Class to represents a person in the application"""

    def __init__(
            self, uid: str, surface: pygame.surface.Surface, name: str, 
            last_name: str, birthday: str, money: float):
        self._id: str = uid
        self._name: str = name
        self._last_name: str = last_name
        self._money: float = money
        self._pos: pygame.math.Vector2 = pygame.math.Vector2()
        
        year_birthday, month_birthday, day_birthday = list(map(int, birthday.split('-')))
        self._birthday: date = date(year_birthday, month_birthday, day_birthday)
        self._person_appearence = PersonAppearence('aa')

        self._surface: pygame.surface.Surface = surface

    def set_position(self, x: float, y: float) -> None:
        """Set person position"""
        self._pos = pygame.math.Vector2(x ,y)
    
    def render(self) -> None:
        """Render person appearence in the surface"""
        image = self._person_appearence.image
        rect = pygame.Rect(self._pos.x, self._pos.y, 32, 32)

        self._surface.blit(image, rect)


