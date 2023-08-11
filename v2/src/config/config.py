class Config:
    """
    Game configuration class
    """

    def __init__(self):
        self.screen_size: list = (1080, 720)
        self.is_fullscren: bool = True
        self.debug_mode: bool = False
        self.character_size: list = (32, 48)
    
    @property
    def name(self) -> str:
        sufix = ' [DEBUG]' if self.debug_mode else ''
        return 'ohr' + sufix