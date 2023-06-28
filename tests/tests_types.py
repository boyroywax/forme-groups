import unittest
from src.groups.types import Types
from src.groups.types.defaults import Defaults
from src.groups.types.defined import Defined
from src.groups.types.supported import Supported


class TestTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.types = Types()
        self.default_type = Defaults()
        self.defined_type = Defined()
        self.supported_type = Supported()

    def test_get(self):
        # Test getting a type by ID when no types are set
        self.assertIsNotNone(self.types.get("type1"))

        # Test getting a type by ID when a default type is set
        self.types._defaults.set_defaults([self.default_type])
        self.assertIs(self.types.get("type1"), self.default_type.get_defaults())

        # Test getting a type by ID when a defined type is set
        self.types._defaults.set_defaults([])
        self.types._defined.set_defined([self.defined_type])
        self.assertIs(self.types.get("type2"), self.defined_type)

        # Test getting a type by ID when a supported type is set
        self.types._defined.set_defined([])

        # Test getting a type by ID when multiple types are set
        self.types._defaults.set_defaults([self.default_type])
        self.types._defined.set_defined([self.defined_type])
        # self.types._supported.set([self.supported_type])
        self.assertIs(self.types.get("type1"), self.default_type)
        self.assertIs(self.types.get("type2"), self.defined_type)
        # self.assertIs(self.types.get("type3"), self.supported_type)
