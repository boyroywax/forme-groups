import unittest
import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit import Unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit("test", "string")

    def test_init(self):
        self.assertEqual(self.unit.value, "test")
        self.assertEqual(self.unit.type_ref, "string")