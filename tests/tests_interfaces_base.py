import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.unit_type import UnitTypeRef, UnitTypeFunction, UnitType
from src.groups.interfaces.base import BaseInterface


class TestBaseInterface(unittest.TestCase):
    def setUp(self) -> None:

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExample(BaseInterface):
            example: str = field(validator=validators.instance_of(str))

            def __str__(self) -> str:
                return super().__str__()

            def __repr__(self) -> str:
                return super().__repr__()

            def __iter__(self):
                return super().__iter__()

            def hash_256(self):
                return super().hash_sha256()

        self.unit_type_interface_example = InterfaceExample("test")

    def test_create_unit_type_interface(self):
        self.assertIsInstance(self.unit_type_interface_example, BaseInterface)

    def test_unit_type_interface_has_hash(self):
        self.assertIsNotNone(self.unit_type_interface_example.hash_sha256())

    def test_unit_type_interface_has_iter(self):
        self.assertEqual(list(self.unit_type_interface_example), ["test"])

    def test_unit_type_interface_slot_contains_list(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleTuple(BaseInterface):
            example: tuple = field(validator=validators.instance_of(tuple))

            def __str__(self) -> str:
                return super().__str__()

            def __repr__(self) -> str:
                return super().__repr__()

            def __iter__(self):
                return super().__iter__()

            def hash_sha256(self):
                return super().hash_sha256()

        unit_type_interface_example2 = InterfaceExampleTuple(("test", "test2",))
        self.assertEqual(list(unit_type_interface_example2.example), ["test", "test2"])

    def test_unit_type_interface_slot_contains_dict(self):

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExampleDict(BaseInterface):
                example: dict = field(validator=validators.instance_of(dict))

                def __str__(self) -> str:
                    return super().__str__()

                def __repr__(self) -> str:
                    return super().__repr__()

                def __iter__(self):
                    return super().__iter__()

                def hash_sha256(self):
                    return super().hash_sha256()

            unit_type_interface_example3 = InterfaceExampleDict({"testdict": {"test": "test", "test2": "test2"}, "testdict2": {"test3": "test3"}})
            print(unit_type_interface_example3)
            print(unit_type_interface_example3.example)
            self.assertEqual(list(unit_type_interface_example3), [{"testdict": {"test": "test", "test2": "test2"}, "testdict2": {"test3": "test3"}}])

            self.assertEqual(list(unit_type_interface_example3.example), ["testdict", "testdict2"])
            self.assertEqual(unit_type_interface_example3.example, {"testdict": {"test": "test", "test2": "test2"}, "testdict2": {"test3": "test3"}})

            self.assertNotEqual(unit_type_interface_example3.hash_sha256(), self.unit_type_interface_example.hash_sha256())
    