import pygame as pg


class Player:
    """
    Player entity
    """

    def __init__(self, uid: int):
        self.id: int = uid
        self.char_id: int = 0
        self.joystick = None
        
        self._init_joystick()
        
    @property
    def controller(self):
        return self.switch_controllers(self)
    
    def _init_joystick(self):
        """
        Initialize joystick
        """

        pg.joystick.init()
        joysticks = [pg.Joystick(x) for x in range(pg.joystick.get_count())]
        if len(joysticks) > 0:
            self.joystick = joysticks[0]