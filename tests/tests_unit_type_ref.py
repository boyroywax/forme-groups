import unittest
import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit_type_ref import UnitTypeRef


class TestUnitTypeRef(unittest.TestCase):
    def test_unit_type_ref(self):
        unit_type_ref = UnitTypeRef('test')
        self.assertEqual(unit_type_ref._type_ref, 'test')

    def test_unit_type_ref_overwrite(self):
        unit_type_ref = UnitTypeRef('test')
        with self.assertRaises(Exception):
            unit_type_ref._type_ref = 'test2'

    def test_unit_type_ref_eq(self):
        unit_type_ref = UnitTypeRef('test')
        unit_type_ref2 = UnitTypeRef('test')
        self.assertEqual(unit_type_ref, unit_type_ref2)

    def test_unit_type_ref_neq(self):
        unit_type_ref = UnitTypeRef('test')
        unit_type_ref2 = UnitTypeRef('test2')
        self.assertNotEqual(unit_type_ref, unit_type_ref2)