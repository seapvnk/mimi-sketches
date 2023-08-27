from __future__ import annotations
from modules.character import *


class BattleStatusBuilder:
    """
    Initializate battle status instance
    """

    def __init__(self, uid: int):
        self._battle_status = BattleStatus(uid)

    @property
    def build(self) -> BattleStatus:
        """
        Return the battle status instance
        """
        return self._battle_status
    
    def hp(self, hp: int, max_hp: int) -> BattleStatusBuilder:
        """
        Set battle status hp and max hp
        """
        self._battle_status.hp = hp
        self._battle_status.max_hp = max_hp
        return self

    def attack(self, strenght: float, magic: float) -> BattleStatusBuilder:
        """
        Set battle status strenght and magic props
        """
        self._battle_status.strenght = strenght
        self._battle_status.magic = magic
        return self
    
    def mana(self, mana: int, max_mana: int) -> BattleStatusBuilder:
        """
        Set battle status mana and max mana
        """
        self.mana = mana
        self._battle_status.max_mana = max_mana
        return self

    def stamina(self, stamina: int, max_stamina: int) -> BattleStatusBuilder:
        """
        Set battle status stamina and max stamina
        """
        self._battle_status.stamina = stamina
        self._battle_status.max_stamina = max_stamina
        return self

    def accuracy(self, accuracy: int) -> BattleStatusBuilder:
        """
        Set battle status accuracy
        """
        self._battle_status.accuracy  = accuracy
        return self
    
    def speed(self, speed: float) -> BattleStatusBuilder:
        """
        Set battle status speed
        """
        self._battle_status.speed = speed
        return self
    
