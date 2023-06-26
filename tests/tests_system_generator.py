import unittest
from unittest.mock import MagicMock
from groups.generator.generator import Generator, TypesGenerator, System


class TestGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.generator = Generator(self.system)
    
    def test_init(self):
        # # Create a new Generator object
        # generator = Generator()

        # Verify that the defaults attribute is set correctly
        self.assertIsNotNone(self.generator._system.defaults)

    def test_set_system(self):
        # Create a new Generator object
        generator = Generator(None)

        # Create a new System object
        system = System()

        # Call the set_system() method
        generator.set_system(system)

        # Verify that the system attribute was set correctly
        self.assertEqual(generator.get_system(), system)

    def test_create_generator(self):
        # Create a new Generator object
        generator = Generator(self.system)

        # Mock the TypesGenerator class
        TypesGenerator.__init__ = MagicMock(return_value=None)

        # Call the create_generator() method with the name "types"
        types_generator = generator.create_generator("types")

        # Verify that the TypesGenerator object was created correctly
        self.assertIsInstance(types_generator, TypesGenerator)


class TestTypesGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

    def test_generate_type(self):
        # Create a new TypesGenerator object
        generator = Generator(self.system)
        types_generator = generator.create_generator("types")

        # Create a type entry dictionary
        type_entry = {
            "id": "test_type",
            "alias": ["test_alias"],
            "super": None,
            "prefix": None,
            "suffix": None,
            "separator": None,
            "system_function": None
        }

        # Call the generate_type() method
        system_type = types_generator.generate_type(type_entry)

        # Verify that the SystemType object was created correctly
        self.assertEqual(system_type.id, "test_type")
        self.assertEqual(system_type.alias, ["test_alias"])
        self.assertIsNone(system_type.super)
        self.assertIsNone(system_type.prefix)
        self.assertIsNone(system_type.suffix)
        self.assertIsNone(system_type.separator)
        self.assertIsNone(system_type.system_function)

    def test_generate(self):
        # Create a new TypesGenerator object
        generator = Generator(self.system)
        types_generator = TypesGenerator(generator)

        # Mock the get_system_types() method
        # generator._system.defaults.get_system_types = MagicMock(return_value=["str", "int", "float"])

        # Call the generate() method
        types_generator.generate()

        # Verify that the system_types attribute was created correctly
        self.assertEqual(len(types_generator._types), 3)

    def test_generate_with_super(self):
        # Create a new TypesGenerator object
        generator = Generator(self.system)
        types_generator = TypesGenerator(generator)

        # Create a type entry dictionary with a super type
        type_entry = {
            "id": "test_type",
            "alias": ["test_alias"],
            "super": "str",
            "prefix": None,
            "suffix": None,
            "separator": None,
            "system_function": None
        }

        # Mock the get_system_types() method
        generator._system.defaults.get_system_types = MagicMock(return_value=["str", "int", "float"])

        # Call the generate_type() method with the type entry
        system_type = types_generator.generate_type(type_entry)

        # Verify that the SystemType object was created correctly
        self.assertEqual(system_type.id, "test_type")
        self.assertEqual(system_type.alias, ["test_alias"])
        self.assertIsNotNone(system_type.super)
        self.assertEqual(system_type.super.id, "str")
        self.assertIsNone(system_type.prefix)
        self.assertIsNone(system_type.suffix)
        self.assertIsNone(system_type.separator)
        self.assertIsNone(system_type.system_function)
