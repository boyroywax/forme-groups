import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.interfaces.base import BaseInterface
from src.groups.converters import _convert_list_to_tuple
from src.groups.merkle_tree import MerkleTree


class TestBaseInterface(unittest.TestCase):
    def setUp(self) -> None:

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExample(BaseInterface):
            example: str = field(validator=validators.instance_of(str))

        self.base_interface_example = InterfaceExample("test")

    def test_create_base_interface(self):
        self.assertIsInstance(self.base_interface_example, BaseInterface)

    def test_base_interface_has_hash(self):
        self.assertIsNotNone(self.base_interface_example.hash_sha256())

    def test_base_interface_has_iter(self):
        self.assertEqual(list(self.base_interface_example), ["test"])

    def test_base_interface_has_slots(self):
        self.assertEqual(self.base_interface_example.__slots__, ("example",))

    def test_base_interface_slot_contains_tuple(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleTuple(BaseInterface):
            example: tuple = field(validator=validators.instance_of(tuple))

        base_interface_example2 = InterfaceExampleTuple(("test", "test2",))
        self.assertEqual(list(base_interface_example2.example), ["test", "test2"])

    def test_base_interface_slot_contains_dict(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleDict(BaseInterface):
            example: dict = field(validator=validators.instance_of(dict))

        base_interface_example3 = InterfaceExampleDict({"test": "test2"})
        self.assertEqual(base_interface_example3.example, {"test": "test2"})
        self.assertEqual(list(base_interface_example3.example), ["test"])

    def test_base_interface_slot_contains_list(self):

        @define(frozen=True, slots=True)
        class InterfaceExampleList(BaseInterface):
            example: tuple = field(validator=validators.instance_of(list | tuple), converter=_convert_list_to_tuple)

        base_interface_example4 = InterfaceExampleList(["test", "test2"])
        self.assertEqual(base_interface_example4.example, ("test", "test2"))
        self.assertEqual(list(base_interface_example4.example), ["test", "test2"])

        with self.assertRaises(ValueError):
            base_interface_example5 = InterfaceExampleList({"test": "test2"})

        with self.assertRaises(FrozenInstanceError):
            base_interface_example4.example = tuple("test3",)

        self.assertEqual(base_interface_example4.example, ("test", "test2"))

    def test_base_interface_slot_contains_int(self):

            @define(frozen=True, slots=True)
            class InterfaceExampleInt(BaseInterface):
                example: int = field(validator=validators.instance_of(int))

            base_interface_example6 = InterfaceExampleInt(1)
            self.assertEqual(base_interface_example6.example, 1)

            with self.assertRaises(TypeError):
                base_interface_example7 = InterfaceExampleInt("test")

            with self.assertRaises(FrozenInstanceError):
                base_interface_example6.example = 2

            self.assertEqual(base_interface_example6.example, 1)

    def test_base_interface_slot_contains_float(self):

            @define(frozen=True, slots=True)
            class InterfaceExampleFloat(BaseInterface):
                example: float = field(validator=validators.instance_of(float))

            base_interface_example8 = InterfaceExampleFloat(1.0)
            self.assertEqual(base_interface_example8.example, 1.0)

            with self.assertRaises(TypeError):
                base_interface_example9 = InterfaceExampleFloat("test")

            with self.assertRaises(FrozenInstanceError):
                base_interface_example8.example = 2.0

            self.assertEqual(base_interface_example8.example, 1.0)
            self.assertEqual(str(base_interface_example8), "1.0")
            self.assertEqual(repr(base_interface_example8), "InterfaceExampleFloat(example=1.0)")

    def test_base_interface_is_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            self.base_interface_example.example = "test"

    def test_base_interface_str(self):
        self.assertEqual(str(self.base_interface_example), "test")

    def test_base_interface_repr(self):
        self.assertEqual(repr(self.base_interface_example), "InterfaceExample(example='test')")

    def test_base_interface_hash(self):
        self.assertEqual(self.base_interface_example.hash_sha256(), "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f")

    def test_base_interface_iter(self):
        self.assertEqual(list(self.base_interface_example), ["test"])

    def test_base_interface_multiple_args(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleMultipleArgs(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: str = field(validator=validators.instance_of(str))

        base_interface_example10 = InterfaceExampleMultipleArgs("test", "test2")
        self.assertEqual(base_interface_example10.example, "test")
        self.assertEqual(base_interface_example10.example2, "test2")

        self.assertEqual(str(base_interface_example10), "test, test2")
        self.assertEqual(repr(base_interface_example10), "InterfaceExampleMultipleArgs(example='test', example2='test2')")

    def test_base_interface_multiple_args_with_list(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleMultipleArgsWithList(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: list = field(validator=validators.instance_of(list))

        base_interface_example11 = InterfaceExampleMultipleArgsWithList("test", ["test2", "test3"])
        self.assertEqual(base_interface_example11.example, "test")
        self.assertEqual(base_interface_example11.example2, ["test2", "test3"])

        self.assertEqual(str(base_interface_example11), "test, ['test2', 'test3']")
        self.assertEqual(repr(base_interface_example11), "InterfaceExampleMultipleArgsWithList(example='test', example2=['test2', 'test3'])")

    def test_base_interface_multiple_args_with_dict(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleMultipleArgsWithDict(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: dict = field(validator=validators.instance_of(dict))

        base_interface_example12 = InterfaceExampleMultipleArgsWithDict("test", {"test2": "test3"})
        self.assertEqual(base_interface_example12.example, "test")
        self.assertEqual(base_interface_example12.example2, {"test2": "test3"})

        self.assertEqual(str(base_interface_example12), "test, {'test2': 'test3'}")
        self.assertEqual(repr(base_interface_example12), "InterfaceExampleMultipleArgsWithDict(example='test', example2={'test2': 'test3'})")

    def test_base_interface_hash_with_multiple_args(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleMultipleArgsWithHash(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: str = field(validator=validators.instance_of(str))

        base_interface_example13 = InterfaceExampleMultipleArgsWithHash("test", "test2")
        self.assertEqual(base_interface_example13.hash_sha256(), "dbcebaa3668e942d85d0263fd43063e45395a3c659ccebfe7d182dcf5879df51")

    def test_base_interface_hash_with_multiple_args_with_list(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleMultipleArgsWithListAndHash(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: list = field(validator=validators.instance_of(list))

        base_interface_example14 = InterfaceExampleMultipleArgsWithListAndHash("test", ["test2", "test3"])
        self.assertEqual(base_interface_example14.hash_sha256(), "d2238b8b227b4a2c798b5b0fb0581fb622787df0d1bd8f2a3d24b4573d031773")

    def test_base_interface_contains_item_verify(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleHashVerify(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: str = field(validator=validators.instance_of(str))

        base_interface_example15 = InterfaceExampleHashVerify("test", "test2")
        self.assertTrue(base_interface_example15.contains_item("test2"))

    def test_base_interface_item_verify_with_list(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleHashVerifyWithList(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: list = field(validator=validators.instance_of(list))

        base_interface_example16 = InterfaceExampleHashVerifyWithList("test", ["test2", "test3"])
        print([item for item in base_interface_example16.__iter__()])
        self.assertTrue(base_interface_example16.contains_item("test2"))

    def test_base_interface_item_verify_with_dict(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleHashVerifyWithDict(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: dict = field(validator=validators.instance_of(dict))

        base_interface_example17 = InterfaceExampleHashVerifyWithDict("test", {"test2": "test3"})
        print([item for item in base_interface_example17.__iter__()])
        self.assertTrue(base_interface_example17.contains_item("test2"))
        self.assertTrue(base_interface_example17.contains_item("test3"))
        self.assertTrue(base_interface_example17.contains_item({"test2": "test3"}))