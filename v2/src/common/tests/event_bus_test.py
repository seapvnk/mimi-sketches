import unittest
from common import EventBus


class EventBusTest(unittest.TestCase):
    def test_write(self):
        """
        Test that it can write an event in event bus buffer
        """
        event_bus = EventBus()
        event_bus.write('event.test', {})

        self.assertEqual(len(event_bus._events), 1)
    
    def test_read(self):
        """
        Test that it can read an event in event bus buffer
        """
        expected = { 'label': 'event.test' }

        event_bus = EventBus()
        event_bus.write('event.test', {})

        self.assertEqual(event_bus.read(), expected)

    def test_read_should_remove_first_event(self):
        """
        Test that it remove the first event when read
        """
        event_bus = EventBus()
        event_bus.write('event.test', {})
        event_bus.read()

        self.assertEqual(len(event_bus._events), 0)