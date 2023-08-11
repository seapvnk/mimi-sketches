import pygame as pg


class BattleStatus:
    """
    Character status entity
    """

    def __init__(self, uid: int):
        self.id: int = uid
        self.hp: int = 0
        self.max_hp: int = 0
        self.max_mana: int = 0
        self.mana: int = 0
        self.max_stamina: int = 0
        self.stamina: int = 0
        self.accuracy: int = 0
        self.strenght: float = 0
        self.magic: float = 0
        self.speed: float = 0
        self.solid: bool = True
