import datetime
import pygame as pg
from modules.character import Appearence
from modules.character import BattleStatus


class Character:
    """
    Character entity
    """

    def __init__(self, uid: int):
        self.id: int = uid
        self.birthday: datetime = datetime()
        self.battle_status: BattleStatus = BattleStatus()
        self.appearence: Appearence = Appearence()
        self.position: pg.Vector2 = pg.Vector2(0, 0)
