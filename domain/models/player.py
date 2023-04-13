import pygame
from domain.models.model import Model
from domain.models.person import Person
from datetime import date

class Player(Model):
    """Class to represents the player in the application"""

    def __init__(self, uid: str, person: Person):
        self._id: str = uid
        self._person: Person = person

    @property
    def person(self) -> Person:
        return self._person
        
    def render(self):
        self._person.render()

