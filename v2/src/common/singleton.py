class Singleton:
    _instance = None

    @classmethod
    def instance(_class):
        """Return the single instance"""
        if _class._instance is None:
            _class._instance = _class()

        return _class._instance