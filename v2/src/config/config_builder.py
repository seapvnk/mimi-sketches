from __future__ import annotations
from config import Config


class ConfigBuilder:
    """
    Initializate config class
    """

    def __init__(self):
        self._config = Config()

    @property
    def build(self) -> Config:
        """
        Return the config instance
        """
        return self._config

    def screen_size_is(self, size: list) -> ConfigBuilder:
        """
        Set screen size
        """
        self._config.screen_size = size
        return self

    @property
    def using_debug_mode(self) -> ConfigBuilder:
        """
        Set debug mode to True
        """
        self._config.debug_mode = True
        return self

    @property
    def is_fullscreen(self) -> ConfigBuilder:
        """
        Set is fullscreen property to true
        """
        self._config.is_fullscren = True
        return self

    @property
    def is_not_fullscreen(self) -> ConfigBuilder:
        """
        Set is fullscreen property to true
        """
        self._config.is_fullscren = False
        return self
