import pygame
import sys

class EventHandler():
    """Application event loop handler"""
    def __init__(self):
        pass

    def handle_events(self) -> None:
        """Event loop"""
        for event in pygame.event.get():
            self.handle(event)
    
    def handle(self, event: pygame.event.Event) -> None:
        """Handle a single event"""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


