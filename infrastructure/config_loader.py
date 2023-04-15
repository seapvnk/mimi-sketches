import os
import json

class ConfigLoader:
    """Singleton to load and store config references"""

    _instance = None

    @classmethod
    def instance(_class):
        """Return an instance of ConfigLoader if there is one,
           otherwise create an instance and returns it"""
        if _class._instance is None:
            _class._instance = _class()

        return _class._instance

    def __init__(self):
        self._references: dict = {}

    def load(self, json_file: str) -> dict:
        """Load config to memory"""
        config_path = os.path.abspath(f'./resources/configs/{json_file}.json')
        if config_path in self._references:
            return self._references[config_path]

        config_fp = open(config_path)
        config = json.load(config_fp)
        self._references[config_path] = config
        
        config_fp.close()
        return config

    def delete(self, config_path: str) -> None:
        """Unload config"""
        del self._references[config_path]


