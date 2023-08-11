import unittest
import pygame as pg
from common import SceneManager
from scenes import TitleScreenScene


class SceneManagerTest(unittest.TestCase):
    def test_update(self):
        """
        Test that it can call update method
        """
        scene_manager = SceneManager(TitleScreenScene())
        scene_manager.update()

    def test_change_scene(self):
        """
        Test that it can change scene and internally switches between scenes
        """
        first_scene = TitleScreenScene()
        second_scene = TitleScreenScene()

        scene_manager = SceneManager(first_scene)
        scene_manager.next(second_scene)

        self.assertEqual(scene_manager._scene, second_scene)

    def test_has_screen(self):
        """
        Test that it can show up screen
        """
        scene_manager = SceneManager(TitleScreenScene())
        self.assertIsInstance(scene_manager.screen, pg.Surface)
