import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.interfaces.container import ContainerInterface


class TestContainerInterface(unittest.TestCase):
    def test_container_interface(self):
        container_interface = ContainerInterface()
        self.assertIsInstance(container_interface, ContainerInterface)

    def test_container_interface_slots(self):
        container_interface = ContainerInterface()
        self.assertEqual(container_interface.__slots__, ("_items",))

    