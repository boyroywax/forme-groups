import unittest
from unittest.mock import Mock
from src.groups.types import Types


class TestTypes(unittest.TestCase):
    def setUp(self) -> None:
        self.types = Types()
        self.default_type = Mock(id="type1")
        self.defined_type = Mock(id="type2")
        self.supported_type = Mock(id="type3")

    def test_get(self):
        # Test getting a type by ID when no types are set
        # self.assertIsNone(self.types.get("type1"))

        # Test getting a type by ID when a default type is set
        self.types._defaults.get = Mock(return_value=self.default_type)
        self.assertIs(self.types.get("type1"), self.default_type)

        # Test getting a type by ID when a defined type is set
        self.types._defaults.get = Mock(return_value=None)
        self.types._defined.get = Mock(return_value=self.defined_type)
        self.assertIs(self.types.get("type2"), self.defined_type)

        # Test getting a type by ID when a supported type is set
        self.types._defaults.get = Mock(return_value=None)
        self.types._defined.get = Mock(return_value=None)
        self.types._supported.get = Mock(return_value=self.supported_type)
        self.assertIs(self.types.get("type3"), self.supported_type)

        # Test getting a type by ID when multiple types are set
        self.types._defaults.get = Mock(return_value=self.default_type)
        self.types._defined.get = Mock(return_value=self.defined_type)
        self.types._supported.get = Mock(return_value=self.supported_type)
        self.assertIs(self.types.get("type1"), self.default_type)
        self.assertIs(self.types.get("type2"), self.defined_type)
        self.assertIs(self.types.get("type3"), self.supported_type)
