
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

        # Test that the UnitTypePool contains the system types
        self.assertEqual(len(self.unit_type_pool), 8)

    def test_unit_type_pool_get(self):
        # Test that the UnitTypePool returns the correct UnitType
        self.SetUp()
        unit_type = self.unit_type_pool.get(UnitType.Ref(name="string"))
        self.assertEqual(unit_type, self.unit_type_pool.types[0])

    def test_unit_type_pool_add(self):
        # Test that the UnitTypePool adds a UnitType
        self.SetUp()
        unit_type = UnitType(aliases=[UnitType.Ref(name="test")], base_type=[UnitType.Ref(name="string")])
        self.unit_type_pool.add(unit_type)
        self.assertEqual(len(self.unit_type_pool), 9)

    def test_unit_type_pool_remove(self):
        # Test that the UnitTypePool removes a UnitType
        self.SetUp()
        unit_type = self.unit_type_pool.get(UnitType.Ref(name="string"))
        with self.assertRaises(Exception):
            self.unit_type_pool.remove(unit_type)
        self.assertEqual(len(self.unit_type_pool), 8)

    def test_unit_type_pool_contains(self):
        # Test that the UnitTypePool contains a UnitType
        self.SetUp()
        self.assertTrue(UnitType.Ref(name="string") in self.unit_type_pool)