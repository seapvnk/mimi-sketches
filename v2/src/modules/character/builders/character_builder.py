from __future__ import annotations
from modules.character import *
import pygame as pg
from datetime import datetime


class CharacterBuilder:
    """
    Initializate character instance
    """

    def __init__(self, uid: int):
        self._character = Character(uid)

    @property
    def build(self) -> Character:
        """
        Return the character instance
        """
        return self._character

    def position(self, position: list) -> CharacterBuilder:
        """
        Set character position
        """
        self._character.position = pg.Vector2(position)
        return self
    
    def birthday(self, birthday: str) -> CharacterBuilder:
        """
        Set character birthday
        """
        year, month, day = birthday.split('-')
        self._character.birthday = datetime(year, month, day)
        return self
    
    def appearence(self, appearence: Appearence) -> CharacterBuilder:
        """
        Set character appearence
        """
        self._character.appearence = appearence
        return self
 
    def battle_status(self, battle_status: BattleStatus) -> CharacterBuilder:
        """
        Set character battle status
        """
        self._character.battle_status = battle_status
        return self
