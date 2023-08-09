import websocket

class Socket:
    """Read and write in socket"""
    
    def __init__(self):
        self._ws = websocket.WebSocket()
        self._ws.connect('ws://127.0.0.1:9723/ws')

    def read(self) -> str:
        """Read server message"""
        return self._ws.recv()

    def send(self, message: str) -> None:
        """Send a message to server"""
        self._ws.send(message)
    
    def close(self):
        """Close connection"""
        self._ws.close()
    
