import unittest

from src.groups.manager.defaults import Defaults
from src.groups.units import UnitType, UnitValue


class TestDefaults(unittest.TestCase):
    def setUp(self):
        self.defaults = Defaults()
