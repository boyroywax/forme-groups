import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.interfaces.base import BaseInterface
from src.groups.utils.converters import _convert_list_to_tuple
from src.groups.utils.merkle_tree import MerkleTree


class TestBaseInterface(unittest.TestCase):
    def setUp(self) -> None:

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExample(BaseInterface):
            example: str = field(validator=validators.instance_of(str))

        self.base_interface_example = InterfaceExample("test")

    def test_base_interface_create_instance(self):
        self.assertIsInstance(self.base_interface_example, BaseInterface)

    def test_base_interface_has_iter(self):
        self.assertEqual(list(self.base_interface_example), ["test"])

    def test_base_interface_has_slots(self):
        self.assertEqual(self.base_interface_example.__slots__, ("example",))

    def test_base_interface_has_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            self.base_interface_example.example = "test2"

    def test_base_interface_has_weakref_slot_false(self):
        self.assertFalse(self.base_interface_example.__weakref__)

    def test_base_interface_has_str(self):
        self.assertEqual(str(self.base_interface_example), "test")

    def test_base_interface_has_repr(self):
        self.assertEqual(repr(self.base_interface_example), "InterfaceExample(example='test')")

    def test_base_interface_has_hash(self):
        self.assertIsNotNone(self.base_interface_example.hash_sha256())

    def test_base_interface_hash_equal_hashes(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleHash(BaseInterface):
            example: str = field(validator=validators.instance_of(str))

        base_interface_example2 = InterfaceExampleHash("test")
        self.assertEqual(base_interface_example2.hash_sha256(), self.base_interface_example.hash_sha256())

    def test_base_interface_has_hash(self):
        self.assertIsNotNone(self.base_interface_example.hash_sha256())

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
        self.assertEqual(base_interface_example14.hash_sha256(), "cd9bad01f840a718739bfeec0d41c00e8af7f490b0b30f344e78e346e8d3dd92")

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

        base_interface_example16 = InterfaceExampleHashVerifyWithList("test", ["test2", "test3", "test4", "test5"])
        print([item for item in base_interface_example16.__iter__()])
        self.assertTrue(base_interface_example16.contains_item("test"))
        self.assertTrue(base_interface_example16.contains_item(["test2", "test3", "test4", "test5"]))

    def test_base_interface_item_verify_with_dict(self):

        @define(slots=True, frozen=True, weakref_slot=False)
        class InterfaceExampleHashVerifyWithDict(BaseInterface):
            example: str = field(validator=validators.instance_of(str))
            example2: dict = field(validator=validators.instance_of(dict))

        base_interface_example17 = InterfaceExampleHashVerifyWithDict("test", {"test2": "test3"})
        print([item for item in base_interface_example17.__iter__()])
        self.assertTrue(base_interface_example17.contains_item("test"))
        self.assertTrue(base_interface_example17.contains_item({"test2": "test3"}))

    # def test_base_interface_item_verify_with_list_of_dicts(self):
            
    #     @define(slots=True, frozen=True, weakref_slot=False)
    #     class InterfaceExampleHashVerifyWithDictAndList(BaseInterface):
    #         example: str = field(validator=validators.instance_of(str))
    #         example2: list = field(validator=validators.instance_of(list))

    #     base_interface_example18 = InterfaceExampleHashVerifyWithDictAndList("test", [{"test2": "test3"}, {"test4": "test5"}])
    #     print([item for item in base_interface_example18.__iter__()])
    #     self.assertTrue(base_interface_example18.contains_item({"test2": "test3"}))
    #     self.assertTrue(base_interface_example18.contains_item({"test4": "test5"}))

    # def test_base_interface_item_verify_with_list_of_dicts_and_lists(self):

    #     @define(slots=True, frozen=True, weakref_slot=False)
    #     class InterfaceExampleHashVerifyWithDictAndList(BaseInterface):
    #         example: str = field(validator=validators.instance_of(str))
    #         example2: list = field(validator=validators.instance_of(list))

    #     base_interface_example19 = InterfaceExampleHashVerifyWithDictAndList("test", [{"test2": "test3"}, ["test4", "test5"]])
    #     print([item for item in base_interface_example19.__iter__()])
    #     self.assertTrue(base_interface_example19.contains_item({"test2": "test3"}))
    #     self.assertTrue(base_interface_example19.contains_item(["test4", "test5"]))

    # def test_base_interface_iterate_subunits(self):

    #     @define(slots=True, frozen=True, weakref_slot=False)
    #     class InterfaceExampleHashVerifyWithDictAndList(BaseInterface):
    #         example: str = field(validator=validators.instance_of(str))
    #         example2: list = field(validator=validators.instance_of(list))

    #     base_interface_example20 = InterfaceExampleHashVerifyWithDictAndList("test", [{"test2": "test3"}, ["test4", "test5"]])
    #     print([item for item in base_interface_example20.__iter__()])
    #     self.assertTrue(base_interface_example20.contains_item({"test2": "test3"}))
    #     self.assertTrue(base_interface_example20.contains_item(["test4", "test5"]))