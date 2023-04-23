import pygame
from application import ClockManager
from domain.shared import Model, Body
from domain.person.appearence import Appearence
from datetime import date

class Person(Model):
    """Class to represents a person in the application"""

    def __init__(
            self, uid: str, surface: pygame.surface.Surface, name: str, 
            last_name: str, birthday: str, money: float):
        self.id: str = uid
        self.name: str = name
        self.last_name: str = last_name
        self.money: float = money

        self.body = Body(200, 700)
        
        year_birthday, month_birthday, day_birthday = list(map(int, birthday.split('-')))
        self.birthday: date = date(year_birthday, month_birthday, day_birthday)
        self.appearence = Appearence('aa')

        self._surface: pygame.surface.Surface = surface
        self.action: str = 'PERSON_RUN_DOWN'
        self.speed: int = 200

        image = self.appearence.image(self.action)
        self.rect = image.get_rect(center=self.body.position)

    def update(self) -> None:
        """Update person"""
        self.body.update()
        self.rect.centery = round(self.body.position.y)
        self.rect.centerx = round(self.body.position.x)

    def render(self) -> None:
        """Render person appearence in the surface"""
        image = self.appearence.image(self.action)
        self._surface.blit(image, self.rect)


