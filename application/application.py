import pygame
from config import SCREEN_SIZE, WINDOW_TITLE
from application import ClockManager, EventHandler
from application.controllers import MapController
from models import Player, Person

class Application():
    """Root class to handle application logic"""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)

        self.event_handler: EventHandler = EventHandler()
        self.clock_manager: ClockManager = ClockManager()
        
        current_map: str = 'map1'
        self.map_controller: MapController = MapController(self.screen, current_map)

        player_person = Person(
            'id-teste',
            self.screen,
            'pedro',
            'sergio',
            '2002-9-1',
            1.99
        )
        player_person.set_position(665.0, 233.0)
        self.player = Player('teste', player_person) 

    def main_loop(self) -> None:
        """Application main loop"""

        while True:
            self.event_handler.handle_events()
            dt = self.clock_manager.dt
            self.render()
            pygame.display.update()

    def render(self) -> None:
        """Application rendering logic"""
        self.screen.fill((0, 0, 0))
        self.map_controller.render_layers(5)
        self.player.render()
        self.map_controller.render_layers()


