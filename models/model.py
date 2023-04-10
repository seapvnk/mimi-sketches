from typing import Any
from models.exceptions import UndefinedAttributeException

class Model:
    """Base class for application models"""
    
    @property
    def id(self):
        return self._id


