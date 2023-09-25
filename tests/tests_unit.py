import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base_class = Base()

    def test_base_class(self):
        self.assertIsInstance(self.base_class, Base)

