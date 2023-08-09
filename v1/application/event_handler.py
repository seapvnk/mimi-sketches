import pygame
import sys

class EventHandler():
    """Application event loop handler"""
    def __init__(self):
        pygame.event.set_allowed([pygame.QUIT])
        self.events: dict = {}

    def handle_events(self) -> None:
        """Event loop"""
        self.events = {}
        for event in pygame.event.get():
            self.add_event(event)
            self.handle(event)

    def add_event(self, event: pygame.event.Event) -> None:
        """Add an event to handle outside"""
        if not event.type in self.events:
            self.events[event.type] = []

        self.events[event.type].append(event)
    
    def handle(self, event: pygame.event.Event) -> None:
        """Handle a single event"""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


