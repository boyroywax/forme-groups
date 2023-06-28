import unittest
from src.groups.base.type.defaults import Defaults
from src.groups.base.type import Type
from src.groups.base.type import Id
from src.groups.base.type import Alias
from src.groups.base.type import Super
from src.groups.base.type import Prefix
from src.groups.base.type import Suffix
from src.groups.base.type import Separator
from src.groups.base.type import Function


class TestDefaults(unittest.TestCase):
    def setUp(self):
        self.id = Id("test_id")
        self.alias = Alias("test_alias")
        self.super = Super("test_super")
        self.prefix = Prefix("test_prefix")
        self.suffix = Suffix("test_suffix")
        self.separator = Separator("test_separator")
        self.function = Function("test_function")
        self.type_obj = Type(self.id, self.alias, self.super, self.prefix, self.suffix, self.separator, self.function)
        self.defaults_types = [self.type_obj]
    
    
    def test_init(self):
        # Test creating a Defaults object with no arguments
        defaults_obj = Defaults()
        self.assertEqual(defaults_obj.types, [])

        # Test creating a Defaults object with types argument
        defaults_obj = Defaults([self.type_obj])
        self.assertEqual(defaults_obj.types, [self.type_obj])

    def test_generate(self):
        # Test generating defaults with no overrides
        defaults_obj = Defaults()
        defaults_obj.generate()
        self.assertNotEqual(defaults_obj.types, self.type_obj)

        # Test generating defaults with overrides
        defaults_obj = Defaults()
        defaults_obj.generate(overrides=[self.type_obj])
        self.assertEqual(defaults_obj.types, defaults_obj.types)

        # Test generating defaults with override_types=True
        defaults_obj = Defaults([self.type_obj])
        defaults_obj.generate(override_types=True, overrides=[self.type_obj])
        self.assertEqual(defaults_obj.types, [self.type_obj])

        # Test generating defaults with override_types=False
        defaults_obj = Defaults([self.type_obj])
        defaults_obj.generate(override_types=False, overrides=[self.type_obj])
        self.assertEqual(defaults_obj.types, defaults_obj.types)