import unittest
from src.groups.types.defaults import Defaults
from src.groups.types.type import Type as TypeClass


class TestDefaults(unittest.TestCase):
    def setUp(self) -> None:
        self.defaults = Defaults()

    def test_get_defaults(self):
        # Test getting the defaults when no defaults are set
        # self.assertEqual(self.defaults.get_defaults(), [])

        # Test getting the defaults when defaults are set
        type1 = TypeClass("string", ["string", "str"], "RESERVED", "", "", "", str)
        type2 = TypeClass("integer", ["integer", "int"], "RESERVED", "", "", "", int)
        type3 = TypeClass("float", ["float", "flt"], "RESERVED", "", "", "", float)
        type4 = TypeClass("boolean", ["boolean", "bool"], "RESERVED", "", "", "", bool)
        type5 = TypeClass("list", ["list", "lst"], "RESERVED", "[", "]", ",", list)
        type6 = TypeClass("dictionary", ["dictionary", "dict"], "RESERVED", "{", "}", ",", dict)
        type7 = TypeClass("tuple", ["tuple", "tpl"], "RESERVED", "(", ")", ",", tuple)
        type8 = TypeClass("bytes", ["bytes", "bts"], "RESERVED", "b'", "'", "", bytes)
        # self.defaults._defaults = [type1, type2]
        self.maxDiff = None
        self.assertEqual(self.defaults.get_defaults(), [type1, type2, type3, type4, type5, type6, type7, type8])

    def test_get(self):
        # Test getting a type by ID when no defaults are set
        self.assertIsNone(self.defaults.get("type1"))

        # Test getting a type by ID when defaults are set
        type1 = TypeClass("type1", ["alias1", "alias2"])
        type2 = TypeClass("type2", ["alias3", "alias4"])
        self.defaults._defaults = [type1, type2]
        self.assertEqual(self.defaults.get("type1"), type1)
        self.assertEqual(self.defaults.get("type2"), type2)
        self.assertIsNone(self.defaults.get("type3"))

    def test_get_by_alias(self):
        # Test getting a type by alias when no defaults are set
        self.assertIsNone(self.defaults.get_by_alias("alias1"))

        # Test getting a type by alias when defaults are set
        type1 = TypeClass("type1", ["alias1", "alias2"])
        type2 = TypeClass("type2", ["alias3", "alias4"])
        self.defaults._defaults = [type1, type2]
        self.assertEqual(self.defaults.get_by_alias("alias1"), type1)
        self.assertEqual(self.defaults.get_by_alias("alias2"), type1)
        self.assertEqual(self.defaults.get_by_alias("alias3"), type2)
        self.assertEqual(self.defaults.get_by_alias("alias4"), type2)
        self.assertIsNone(self.defaults.get_by_alias("alias5"))