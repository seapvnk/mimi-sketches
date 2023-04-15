import pygame
from application import ClockManager
from domain.models.model import Model
from domain.models.person_appearence import PersonAppearence
from datetime import date

class Person(Model):
    """Class to represents a person in the application"""

    def __init__(
            self, uid: str, surface: pygame.surface.Surface, name: str, 
            last_name: str, birthday: str, money: float, 
            is_player: bool = False):
        self.id: str = uid
        self.name: str = name
        self.last_name: str = last_name
        self.money: float = money

        self.running: bool = False

        self.position: pygame.math.Vector2 = pygame.math.Vector2()
        self.direction: pygame.math.Vector2 = pygame.math.Vector2()
        
        self._is_player: bool = is_player
        
        year_birthday, month_birthday, day_birthday = list(map(int, birthday.split('-')))
        self.birthday: date = date(year_birthday, month_birthday, day_birthday)
        self.appearence = PersonAppearence('aa')

        self._surface: pygame.surface.Surface = surface
        self.action: str = 'PERSON_RUN_DOWN'
        self.speed: int = 200

        image = self.appearence.image(self.action)
        self.rect = image.get_rect(center=self.position)

    def update(self) -> None:
        """Update person"""
        if not self._is_player:
            pass

        dt = ClockManager.instance().dt
        speed = self.speed if not self.running else self.speed * 2
        self.position += self.direction * speed * dt 
        self.rect.centery = round(self.position.y)
        self.rect.centerx = round(self.position.x)

    def render(self) -> None:
        """Render person appearence in the surface"""
        image = self.appearence.image(self.action)
        self._surface.blit(image, self.rect)


