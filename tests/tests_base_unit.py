import unittest
from src.groups.base.units import Units
from src.groups.base.units.base import BaseUnit
from src.groups.base.type import Type_
from src.groups.base.type import Id
from src.groups.base.type import Alias
from src.groups.base.type import Super
from src.groups.base.type import Prefix
from src.groups.base.type import Suffix
from src.groups.base.type import Separator
from src.groups.base.type import Function


class TestBaseUnit(unittest.TestCase):
    def setUp(self):
        self.id_ = Id("test_id")
        self.alias = Alias("test_alias")
        self.super_ = Super("string")
        self.prefix = Prefix("test_prefix")
        self.suffix = Suffix("test_suffix")
        self.separator = Separator("test_separator")
        self.function_ = Function("test_function")
        type_obj = Type_(self.id_, self.alias, self.super_, self.prefix, self.suffix, self.separator, self.function_)
        self.units = Units("default", [type_obj])
        self.base_unit = BaseUnit("test", self.units.types[-1])

    def test_base(self):
        # Test setting and getting the base property
        new_type_obj = Type_(Id("new_id"), Alias("new_alias"), Super("new_super"), Prefix("new_prefix"), Suffix("new_suffix"), Separator("new_separator"), Function("new_function"))
        self.base_unit.base_type = new_type_obj
        self.assertEqual(self.base_unit._base_type, new_type_obj)

    def test_id(self):
        # Test getting the id property
        self.assertEqual(self.base_unit.id_, "test_id")

    def test_alias(self):
        # Test getting the alias property
        self.assertEqual(self.base_unit.alias, "test_alias")