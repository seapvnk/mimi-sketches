import pygame
from config import SCREEN_SIZE, WINDOW_TITLE
from application import ClockManager, EventHandler, Camera
from domain.map import MapController
from domain.player import Player, PlayerController
from domain.person import Person

class Application():
    """Root class to handle application logic"""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)

        self.event_handler: EventHandler = EventHandler()
        self.clock_manager: ClockManager = ClockManager.instance()
        
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
        player_person.body.position = pygame.math.Vector2(665.0, 233.0)
        player = Player('teste', player_person) 
        self.player_controller: PlayerController = PlayerController(self.screen, player)
        self.camera: Camera = Camera(
            self.screen, 
            self.player_controller.player
        )

    def main_loop(self) -> None:
        """Application main loop"""

        while True:
            self.event_handler.handle_events()
            dt = self.clock_manager.dt
            
            if pygame.MOUSEWHEEL in self.event_handler.events:
                self.camera.update(
                    self.event_handler.events[pygame.MOUSEWHEEL][0]
                )

            self.player_controller.update()
            self.player_controller.handle_player_input()
            self.render()

    def render(self) -> None:
        """Application rendering logic"""
        self.screen.fill((0, 0, 0))
        self.map_controller.render(6)
        self.player_controller.render()
        self.map_controller.render(6, self.map_controller.last_layer)
        self.camera.render()
        pygame.display.update()


