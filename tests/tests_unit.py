
import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')


import unittest
from src.groups.unit import Unit, UnitType, UnitTypePool


class TestUnit(unittest.TestCase):
    def SetUp(self):
        self.unit_type_pool = UnitTypePool()

    def test_init(self):
        # Test that the UnitTypePool is initialized
        self.SetUp()
        self.assertIsInstance(self.unit_type_pool, UnitTypePool)

        #test that the UnitTypePool contains the system types
        self.assertEqual(len(self.unit_type_pool), 8)