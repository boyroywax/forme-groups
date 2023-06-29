import unittest
from src.groups.base.type import Type_
from src.groups.base.type import Id
from src.groups.base.type import Alias
from src.groups.base.type import Super
from src.groups.base.type import Prefix
from src.groups.base.type import Suffix
from src.groups.base.type import Separator
from src.groups.base.type import Function


class TestType(unittest.TestCase):
    def setUp(self):
        self.id_ = Id("test_id")
        self.alias = Alias("test_alias")
        self.super = Super("test_super")
        self.prefix = Prefix("test_prefix")
        self.suffix = Suffix("test_suffix")
        self.separator = Separator("test_separator")
        self.function = Function("test_function")

    def test_init(self):
        # Test creating a Type object with all arguments
        type_obj = Type_(self.id_, self.alias, self.super, self.prefix, self.suffix, self.separator, self.function)
        self.assertEqual(type_obj.id_, self.id_)
        self.assertEqual(type_obj.alias, self.alias)
        self.assertEqual(type_obj.super_, self.super)
        self.assertEqual(type_obj.prefix, self.prefix)
        self.assertEqual(type_obj.suffix, self.suffix)
        self.assertEqual(type_obj.separator, self.separator)
        self.assertEqual(type_obj.function_, self.function)

    def test_init_with_nones(self):
        # Test creating a Type object with default arguments
        id_obj = Id()
        alias_obj = Alias()
        super_obj = Super()
        prefix_obj = Prefix()
        suffix_obj = Suffix()
        separator_obj = Separator()
        function_obj = Function()
        
        type_obj = Type_(id_obj, alias_obj, super_obj, prefix_obj, suffix_obj, separator_obj, function_obj)
        self.assertIsNone(type_obj.id_.value)
        self.assertIsNone(type_obj.alias.value)
        self.assertIsNone(type_obj.super_.value)
        self.assertIsNone(type_obj.prefix.value)
        self.assertIsNone(type_obj.suffix.value)
        self.assertIsNone(type_obj.separator.value)
        self.assertIsNone(type_obj.function_.value)

    def test_str(self):
        # Test getting the string representation of a Type object
        type_obj = Type_(self.id_, self.alias, self.super, self.prefix, self.suffix, self.separator, self.function)
        self.assertEqual(str(type_obj), "Type_(id_=Id(value='test_id'), alias=Alias(value='test_alias'), super_=Super(value='test_super'), prefix=Prefix(value='test_prefix'), suffix=Suffix(value='test_suffix'), separator=Separator(value='test_separator'), function_=Function(value='test_function'))")

    def test_repr(self):
        # Test getting the string representation of a Type object
        type_obj = Type_(self.id_, self.alias, self.super, self.prefix, self.suffix, self.separator, self.function)
        self.assertEqual(repr(type_obj), "Type_(id_=Id(value='test_id'), alias=Alias(value='test_alias'), super_=Super(value='test_super'), prefix=Prefix(value='test_prefix'), suffix=Suffix(value='test_suffix'), separator=Separator(value='test_separator'), function_=Function(value='test_function'))")