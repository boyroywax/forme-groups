import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType, ReferenceInterface


class TestReferenceInterface(unittest.TestCase):
    def setUp(self) -> None:

        class InterfaceExample(ReferenceInterface):
            pass

        self.unit_type_interface_example = InterfaceExample()


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

    def test_unit_type_ref_slots(self):
        self.assertEqual(self.unit_type_ref.__slots__, ("alias",))

    def test_unit_type_ref_hash(self):
        self.assertEqual(self.unit_type_ref.hash_256(), "8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702")

    


class TestUnitTypeFunction(unittest.TestCase):
    def setUp(self):
        self.unit_type_function = UnitTypeFunction(function_object=MagicMock(), args=["arg1", "arg2"])

    def test_create_unit_type_function(self):
        self.assertIsInstance(self.unit_type_function, UnitTypeFunction)

    def test_unit_type_function_has_object(self):
        self.assertIsNotNone(self.unit_type_function.function_object)

    def test_unit_type_function_has_args(self):
        self.assertEqual(self.unit_type_function.args, ["arg1", "arg2"])

    def test_unit_type_function_is_frozen(self):
        unit_type_function = UnitTypeFunction(function_object=MagicMock(), args=["arg1", "arg2"])
        with self.assertRaises(FrozenInstanceError):
            unit_type_function.function_object = MagicMock()

    def test_unit_type_function_call(self):
        unit_type_function = UnitTypeFunction(function_object=lambda x, y: x + y, args=[1, 2])
        self.assertEqual(unit_type_function.call(), 3)

    def test_unit_type_function_call_with_no_args(self):
        unit_type_function = UnitTypeFunction(function_object=lambda: 1, args=[])
        self.assertEqual(unit_type_function.call(), 1)

    def test_unit_type_function_call_with_builtin_function(self):
        unit_type_function = UnitTypeFunction(function_object=len, args=[[]])
        self.assertEqual(unit_type_function.call(), 0)

    def test_unit_type_function_args_is_frozen(self):
        unit_type_function = UnitTypeFunction(function_object=MagicMock(), args=["arg1", "arg2"])
        with self.assertRaises(FrozenInstanceError):
            unit_type_function.args = ["new_arg1", "new_arg2"]

    def test_unit_type_function_call_with_buildint_string_function(self):
        unit_type_function = UnitTypeFunction(function_object=str.upper)
        self.assertEqual(unit_type_function.call("test"), "TEST")

    def test_unit_type_function_call_with_buildint_string_function_and_args(self):
        unit_type_function = UnitTypeFunction(function_object=dict.get, args=["test_key"])
        self.assertEqual(unit_type_function.call({"test_key": "test_value"}), "test_value")

    def test_unit_type_function_call_with_dict_and_value(self):
        unit_type_function = UnitTypeFunction(function_object=dict)
        self.assertEqual(unit_type_function.call({"test": "test"}), {"test": "test"})

    def test_unit_type_function_call_with_list_and_value(self):
        unit_type_function = UnitTypeFunction(function_object=list)
        self.assertEqual(unit_type_function.call(["test"]), ["test"])



    def test_unit_type_function_repr(self):
        unit_type_function = UnitTypeFunction(function_object=dict(), args=[])
        self.assertEqual(repr(unit_type_function), "UnitTypeFunction(function_object=<class 'dict'>, args=[])")


class TestUnitType(unittest.TestCase):
    def setUp(self):
        self.unit_type = UnitType(
            aliases=[UnitTypeRef(alias="alias1"), UnitTypeRef(alias="alias2")],
            super_type=[UnitTypeRef(alias="super_type")],
            prefix="prefix",
            suffix="suffix",
            separator="separator",
            sys_function=UnitTypeFunction(function_object="str.upper", args=[]),
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

    def test_unit_type_slots(self):
        self.assertEqual(self.unit_type.__slots__, ("aliases", "super_type", "prefix", "suffix", "separator", "sys_function",))

    def test_unit_type_hash(self):
        self.assertEqual(self.unit_type.hash_256(), "09cc56132215e2c8d3805879e3fd5ece1242d3eaf5681643c03bfce6f75615f6")

    def test_unit_type_hash_tree(self):
        self.assertEqual(self.unit_type.hash_tree().root(), "7f6cce3f1a1f604510cdb35d0c3cf533033cd7ab3333c2d3f71b16144df5601f")

