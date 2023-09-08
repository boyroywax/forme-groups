import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit import UnitTypeRef, UnitTypeFunction, UnitType, UnitTypePool, Unit, UnitGenerator


class TestUnitTypeRef(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="test_alias")

    def test_create_unit_type_ref(self):
        self.assertIsInstance(self.unit_type_ref, UnitTypeRef)

    def test_unit_type_ref_has_alias(self):
        self.assertEqual(self.unit_type_ref.alias, "test_alias")

    def test_unit_type_ref_is_frozen(self):
        unit_type_ref = UnitTypeRef(alias="test_alias")
        with self.assertRaises(FrozenInstanceError):
            unit_type_ref.alias = "new_alias"


class TestUnitTypeFunction(unittest.TestCase):
    def setUp(self):
        self.unit_type_function = UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"])

    def test_create_unit_type_function(self):
        self.assertIsInstance(self.unit_type_function, UnitTypeFunction)

    def test_unit_type_function_has_object(self):
        self.assertIsNotNone(self.unit_type_function.object)

    def test_unit_type_function_has_args(self):
        self.assertEqual(self.unit_type_function.args, ["arg1", "arg2"])

    def test_unit_type_function_is_frozen(self):
        unit_type_function = UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"])
        with self.assertRaises(FrozenInstanceError):
            unit_type_function.object = MagicMock()

    def test_unit_type_function_call(self):
        unit_type_function = UnitTypeFunction(object=lambda x, y: x + y, args=[1, 2])
        self.assertEqual(unit_type_function.call(), 3)

    def test_unit_type_function_call_with_no_args(self):
        unit_type_function = UnitTypeFunction(object=lambda: 1, args=[])
        self.assertEqual(unit_type_function.call(), 1)

    def test_unit_type_function_call_with_builtin_function(self):
        unit_type_function = UnitTypeFunction(object=len, args=[[]])
        self.assertEqual(unit_type_function.call(), 0)

    def test_unit_type_function_args_is_frozen(self):
        unit_type_function = UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"])
        with self.assertRaises(FrozenInstanceError):
            unit_type_function.args = ["new_arg1", "new_arg2"]

    def test_unit_type_function_call_with_buildint_string_function(self):
        unit_type_function = UnitTypeFunction(object=str.upper)
        self.assertEqual(unit_type_function.call("test"), "TEST")


class TestUnitType(unittest.TestCase):
    def setUp(self):
        self.unit_type = UnitType(
            aliases=[UnitTypeRef(alias="alias1"), UnitTypeRef(alias="alias2")],
            super_type=[UnitTypeRef(alias="super_type")],
            prefix="prefix",
            suffix="suffix",
            separator="separator",
            sys_function=UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"]),
        )
        print(self.unit_type)

    def test_create_unit_type(self):
        self.assertIsInstance(self.unit_type, UnitType)

    def test_unit_type_has_aliases(self):
        self.assertEqual(len(self.unit_type.aliases), 2)

    def test_unit_type_has_super_type(self):
        self.assertEqual(len(self.unit_type.super_type), 1)

    def test_unit_type_has_prefix(self):
        self.assertEqual(self.unit_type.prefix, "prefix")

    def test_unit_type_has_suffix(self):
        self.assertEqual(self.unit_type.suffix, "suffix")

    def test_unit_type_has_seperator(self):
        self.assertEqual(self.unit_type.separator, "separator")

    def test_unit_type_has_sys_function(self):
        self.assertIsNotNone(self.unit_type.sys_function)

    def test_unit_type_is_frozen(self):
        unit_type = UnitType(aliases=[], super_type=[], prefix="prefix", suffix="suffix", separator="separator")
        with self.assertRaises(FrozenInstanceError):
            unit_type.prefix = "new_prefix"


class TestUnitTypePool(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="test_alias")
        self.unit_type_function = UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"])
        self.unit_type = UnitType(
            aliases=[self.unit_type_ref],
            super_type=[self.unit_type_ref],
            prefix="prefix",
            suffix="suffix",
            separator="separator",
            sys_function=self.unit_type_function,
        )
        self.unit_type_pool = UnitTypePool()

    def test_create_unit_type_pool(self):
        self.assertIsInstance(self.unit_type_pool, UnitTypePool)

    def test_unit_type_pool_has_unit_types(self):
        self.assertEqual(len(self.unit_type_pool.unit_types), 0)

    def test_unit_type_pool_contains_alias(self):
        self.assertFalse(self.unit_type_pool.contains_alias("test_alias"))

    def test_unit_type_pool_add_unit_type(self):
        self.unit_type_pool.add_unit_type(self.unit_type)
        self.assertEqual(len(self.unit_type_pool.unit_types), 1)

    def test_unit_type_pool_add_unit_type_with_existing_alias(self):
        self.unit_type_pool.add_unit_type(self.unit_type)
        with self.assertRaises(ValueError):
            self.unit_type_pool.add_unit_type(self.unit_type)

    def test_unit_type_pool_freeze_pool(self):
        self.unit_type_pool.freeze_pool()
        self.assertEqual(self.unit_type_pool.frozen, True)
        with self.assertRaises(Exception):
            self.unit_type_pool.add_unit_type(self.unit_type)

    def test_set_system_types(self):
        unit_type_pool = UnitTypePool()
        unit_type_pool.set_system_types_from_json()
        self.assertGreater(len(unit_type_pool.unit_types), 0)


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(value="test_value", type_ref="test_type_ref")

    def test_create_unit(self):
        self.assertIsInstance(self.unit, Unit)

    def test_unit_has_value(self):
        self.assertEqual(self.unit.value, "test_value")

    def test_unit_has_type_ref(self):
        self.assertEqual(self.unit.type_ref, "test_type_ref")


class TestUnitGenerator(unittest.TestCase):
    def setUp(self):
        self.unit_type_ref = UnitTypeRef(alias="test_alias")
        self.unit_type_function = UnitTypeFunction(object=MagicMock(), args=["arg1", "arg2"])
        self.unit_type = UnitType(
            aliases=[self.unit_type_ref],
            super_type=[self.unit_type_ref],
            prefix="prefix",
            suffix="suffix",
            separator="separator",
            sys_function=self.unit_type_function,
        )
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.add_unit_type(self.unit_type)
        self.unit_generator = UnitGenerator(unit_type_pool=self.unit_type_pool)
        self.unit_generator.unit_type_pool.freeze_pool()

    def test_create_unit(self):
        self.unit_type_pool.freeze_pool()
        unit = self.unit_generator.create_unit("test_alias")
        self.assertIsInstance(unit, Unit)

    def test_create_unit_with_invalid_alias(self):
        self.unit_type_pool.freeze_pool()
        with self.assertRaises(ValueError):
            self.unit_generator.create_unit("invalid_alias")

    def test_create_unit_with_multiple_aliases(self):
        unit_type_ref2 = UnitTypeRef(alias="test_alias2")
        unit_type2 = UnitType(
            aliases=[unit_type_ref2],
            super_type=[self.unit_type_ref],
            prefix="prefix",
            suffix="suffix",
            separator="separator",
            sys_function=self.unit_type_function,
        )
        self.unit_type_pool.add_unit_type(unit_type2)
        self.assertEqual(self.unit_type_pool.get_type_from_alias("test_alias2"), unit_type2)

    def test_create_unit_with_value(self):
        # self.unit_generator.unit_type_pool.set_system_types_from_json()
        self.unit_generator.unit_type_pool.freeze_pool()
        pre_pool = self.unit_generator.unit_type_pool
        print(pre_pool)
        unit = self.unit_generator.create_unit(alias="str", value="test_value_")
        print(hash(unit))
        print(self.unit_generator.unit_type_pool)
        self.assertEqual(self.unit_generator.unit_type_pool, pre_pool)

    def test_create_units_and_check_if_same_hash(self):
        self.unit_type_pool.set_system_types_from_json()
        self.unit_type_pool.freeze_pool()
        unit1 = self.unit_generator.create_unit("str", value="test_value")
        unit2 = self.unit_generator.create_unit("str", value="test_value")
        self.assertEqual(unit1, unit2)

    def test_create_unit_with_no_value(self):
        self.unit_type_pool.set_system_types_from_json()
        self.unit_type_pool.freeze_pool()
        unit = self.unit_generator.create_unit(alias="str")
        self.assertEqual(unit.value, "")

    def test_create_units_from_all_system_types(self):
        self.unit_type_pool.set_system_types_from_json()
        self.unit_type_pool.freeze_pool()
        for unit_type in self.unit_type_pool.unit_types:
            unit = self.unit_generator.create_unit(unit_type.aliases[0].alias)
            print(unit)
            self.assertIsInstance(unit, Unit)
