import unittest
from common import Singleton


class SingletonTest(unittest.TestCase):
    def test_has_unique_instance(self):
        """
        Test that it always return the same instance
        """

        singleton_1 = Singleton.instance()
        singleton_2 = Singleton.instance()

        self.assertEqual(singleton_1, singleton_2)