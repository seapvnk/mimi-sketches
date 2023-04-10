import pygame
from models.model import Model
from models.person import Person
from datetime import date

class Player(Model):
    """Class to represents the player in the application"""

    def __init__(self, uid: str, person: Person):
        self._id: str = uid
        self._person: Person = person
        
    def render(self):
        self._person.render()
