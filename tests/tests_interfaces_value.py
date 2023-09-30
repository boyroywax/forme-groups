import unittest
from attr import define, field, validators
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.interfaces.value import ValueInterface

class TestValueInterface(unittest.TestCase):
    def test_value_interface(self):
        value_interface = ValueInterface()
        self.assertIsInstance(value_interface, ValueInterface)

    def test_value_interface_slots(self):
        value_interface = ValueInterface()
        self.assertEqual(value_interface.__slots__, ("_value", ))

    def test_value_interface_value_none(self):
        value_interface = ValueInterface()
        self.assertIsNone(value_interface.value)

    def test_value_interface_value_int(self):
        value_interface = ValueInterface(value=1)
        self.assertEqual(value_interface.value, 1)

    def test_value_interface_value_str(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(value_interface.value, "test")

    def test_value_interface_value_bool(self):
        value_interface = ValueInterface(value=True)
        self.assertEqual(value_interface.value, True)

    def test_value_interface_value_list(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value=["test"])

    def test_value_interface_value_dict(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value={"test": "test"})

    def test_value_interface_value_tuple(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value=("test",))

    def test_value_interface_value_set(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value={"test"})

    def test_value_interface_value_frozenset(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value=frozenset({"test"}))

    def test_value_interface_value_bytes(self):
        value_interface = ValueInterface(value=b"test")
        self.assertEqual(value_interface.value, b"test")

    def test_value_interface_value_bytearray(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value=bytearray("test"))

    def test_value_interface_value_memoryview(self):
        with self.assertRaises(TypeError):
            value_interface = ValueInterface(value=memoryview(b"test"))

    def test_value_interface_value_none(self):
        value_interface = ValueInterface(value=None)
        self.assertIsNone(value_interface.value)

    def test_value_interface_str(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(str(value_interface), "test")

    def test_value_interface_repr(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(repr(value_interface), "ValueInterface(_value='test')")

    def test_value_interface_iter(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(list(value_interface), ["test"])

    def test_value_interface_type_ref(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(value_interface.type_ref, "str")

    def test_value_interface_type_ref_with_int(self):
        value_interface = ValueInterface(value=1)
        self.assertEqual(value_interface.type_ref, "int")

    def test_value_interface_type_ref_with_bool(self):
        value_interface = ValueInterface(value=True)
        self.assertEqual(value_interface.type_ref, "bool")

    def test_value_interface_type_ref_with_none(self):
        value_interface = ValueInterface(value=None)
        self.assertEqual(value_interface.type_ref, "NoneType")

    def test_value_interface_type_ref_with_bytes(self):
        value_interface = ValueInterface(value=b"test")
        self.assertEqual(value_interface.type_ref, "bytes")

    def test_value_interface_convert_to_int(self):
        value_interface = ValueInterface(value="1")
        self.assertEqual(value_interface.convert_to_type("int"), 1)

    def test_value_interface_convert_to_int_with_int(self):
        value_interface = ValueInterface(value=1)
        self.assertEqual(value_interface.convert_to_type("int"), 1)

    def test_value_interface_convert_to_int_with_float(self):
        value_interface = ValueInterface(value=1.0)
        self.assertEqual(value_interface.convert_to_type("int"), 1)

    def test_value_interface_convert_to_int_with_str(self):
        value_interface = ValueInterface(value="test")
        with self.assertRaises(ValueError):
            value_interface.convert_to_type("int")

    def test_value_interface_convert_to_int_with_bool(self):
        value_interface = ValueInterface(value=True)
        self.assertEquals(value_interface.convert_to_type("int"), 1)

    def test_value_interface_convert_to_none(self):
        value_interface = ValueInterface(value="test")
        self.assertIsNone(value_interface.convert_to_type("NoneType"))

    def test_value_interface_convert_to_none_with_none(self):
        value_interface = ValueInterface(value=None)
        self.assertIsNone(value_interface.convert_to_type("NoneType"))

    def test_value_interface_hash(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(value_interface.hash_sha256(), "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f")

    def test_value_interface_hash_tree(self):
        value_interface = ValueInterface(value="test")
        self.assertEqual(value_interface.hash_tree().root(), "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f")

    def test_value_interface_hash_tree_with_int(self):
        value_interface = ValueInterface(value=1)
        self.assertEqual(value_interface.hash_tree().root(), "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b")

    def test_value_interface_hash_tree_with_bool(self):
        value_interface = ValueInterface(value=True)
        self.assertEqual(value_interface.hash_tree().root(), "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18")

    def test_value_interface_hash_tree_with_none(self):
        value_interface = ValueInterface(value=None)
        self.assertEqual(value_interface.hash_tree().root(), "dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91")

    def test_value_interface_hash_tree_equals_for_same_value(self):
        value_interface1 = ValueInterface(value="test")
        value_interface2 = ValueInterface(value="test")
        self.assertEqual(value_interface1.hash_tree().root(), value_interface2.hash_tree().root())