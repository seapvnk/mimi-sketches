from common import Singleton


class EventBus(Singleton):
    """
    Singleton to read and write events
    """

    def __init__(self):
        self._events = []

    def read(self) -> dict:
        """
        Read event
        """
        if len(self._events) < 1:
            return {}
            
        event = self._events[0]
        self._events = self._events[1:]
        return event

    def write(self, label: str, event: dict) -> None:
        """
        Write event
        """
        event['label'] = label
        self._events.append(event)
