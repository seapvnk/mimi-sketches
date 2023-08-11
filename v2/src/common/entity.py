from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Application entity
    """

    @abstractmethod
    def update(self) -> dict:
        """
        Update and returns update dict
        """
        pass