import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.interfaces.base import BaseInterface
from src.groups.converters import _convert_list_to_tuple


class TestBaseInterface(unittest.TestCase):
    def setUp(self) -> None:

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExample(BaseInterface):
            example: str = field(validator=validators.instance_of(str))

        self.unit_type_interface_example = InterfaceExample("test")

    def test_create_unit_type_interface(self):
        self.assertIsInstance(self.unit_type_interface_example, BaseInterface)

    def test_unit_type_interface_has_hash(self):
        self.assertIsNotNone(self.unit_type_interface_example.hash_sha256())

    def test_unit_type_interface_has_iter(self):
        self.assertEqual(list(self.unit_type_interface_example), ["test"])

    def test_unit_type_interface_slot_contains_tuple(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleTuple(BaseInterface):
            example: tuple = field(validator=validators.instance_of(tuple))

        unit_type_interface_example2 = InterfaceExampleTuple(("test", "test2",))
        self.assertEqual(list(unit_type_interface_example2.example), ["test", "test2"])

    def test_unit_type_interface_slot_contains_dict(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleDict(BaseInterface):
            example: dict = field(validator=validators.instance_of(dict))

        unit_type_interface_example3 = InterfaceExampleDict({"test": "test2"})
        self.assertEqual(unit_type_interface_example3.example, {"test": "test2"})
        self.assertEqual(list(unit_type_interface_example3.example), ["test"])

    def test_unit_type_interface_slot_contains_list(self):

        @define(frozen=True, slots=True)
        class InterfaceExampleList(BaseInterface):
            example: tuple = field(validator=validators.instance_of(list | tuple), converter=_convert_list_to_tuple)

        unit_type_interface_example4 = InterfaceExampleList(["test", "test2"])
        self.assertEqual(unit_type_interface_example4.example, ("test", "test2"))
        self.assertEqual(list(unit_type_interface_example4.example), ["test", "test2"])

        with self.assertRaises(ValueError):
            unit_type_interface_example5 = InterfaceExampleList({"test": "test2"})

        with self.assertRaises(FrozenInstanceError):
            unit_type_interface_example4.example = tuple("test3",)

        self.assertEqual(unit_type_interface_example4.example, ("test", "test2"))

    def test_unit_type_interface_slot_contains_int(self):

            @define(frozen=True, slots=True)
            class InterfaceExampleInt(BaseInterface):
                example: int = field(validator=validators.instance_of(int))

            unit_type_interface_example6 = InterfaceExampleInt(1)
            self.assertEqual(unit_type_interface_example6.example, 1)

            with self.assertRaises(TypeError):
                unit_type_interface_example7 = InterfaceExampleInt("test")

            with self.assertRaises(FrozenInstanceError):
                unit_type_interface_example6.example = 2

            self.assertEqual(unit_type_interface_example6.example, 1)

    def test_unit_type_interface_slot_contains_float(self):

            @define(frozen=True, slots=True)
            class InterfaceExampleFloat(BaseInterface):
                example: float = field(validator=validators.instance_of(float))

            unit_type_interface_example8 = InterfaceExampleFloat(1.0)
            self.assertEqual(unit_type_interface_example8.example, 1.0)

            with self.assertRaises(TypeError):
                unit_type_interface_example9 = InterfaceExampleFloat("test")

            with self.assertRaises(FrozenInstanceError):
                unit_type_interface_example8.example = 2.0

            self.assertEqual(unit_type_interface_example8.example, 1.0)
            self.assertEqual(str(unit_type_interface_example8), "1.0")
            self.assertEqual(repr(unit_type_interface_example8), "InterfaceExampleFloat(example=1.0)")

    def test_base_interface_is_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            self.unit_type_interface_example.example = "test"

    def test_base_interface_str(self):
        self.assertEqual(str(self.unit_type_interface_example), "test")


