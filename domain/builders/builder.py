from domain.models import Model

class Builder:
    """Base class for builders"""
    def __init__(self):
        self._instance: Model = None

    def __call__(self) -> Model:
        """Returns builder's instance"""
        return self._instance

    
