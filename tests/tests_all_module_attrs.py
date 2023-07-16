import unittest

from src.groups.attr_all import UnitTypeRef, UnitValue, Unit, FrozenUnit, FrozenUnitValue, FrozenUnitTypeRef


class TestAllAttrs(unittest.TestCase):
    def test_unit_type_ref(self):
        type_ref = "int"
        unit_type_ref = UnitTypeRef(type_ref)

        self.assertEqual(unit_type_ref.type_ref, type_ref)

    def test_bad_unit_type_ref(self):
        with self.assertRaises(Exception):
            UnitTypeRef(1)

    def test_frozen_unit_type_ref(self):
        type_ref = "int"
        unit_type_ref = FrozenUnitTypeRef(type_ref)

        self.assertEqual(unit_type_ref.type_ref, type_ref)

    def test_bad_frozen_unit_type_ref(self):
        with self.assertRaises(Exception):
            FrozenUnitTypeRef(1)

    def test_unit_value(self):
        value = 1
        unit_value = UnitValue("int", value)

        self.assertEqual(unit_value.value, value)

    def test_bad_unit_value(self):
        with self.assertRaises(Exception):
            UnitValue(1, 1)

    def test_frozen_unit_value(self):
        value = 1
        unit_value = FrozenUnitValue("int", value)

        self.assertEqual(unit_value.value, value)

    # def test_unit_type_ref_freeze(self):
    #     type_ref = "int"
    #     unit_type_ref = UnitTypeRef(type_ref)

    #     frozen_unit_type_ref = unit_type_ref.freeze()
    #     # unit_type_ref.freeze()

    #     self.assertIsInstance(frozen_unit_type_ref, FrozenUnitTypeRef)
    #     with self.assertRaises(Exception):
    #         frozen_unit_type_ref.type_ref = "float"

    #     self.assertEqual(frozen_unit_type_ref.type_ref, type_ref)

    def test_unit(self):
        value = 1
        unit = Unit("int", value)

        self.assertEqual(unit.value, value)

        unit.value = 2

    
