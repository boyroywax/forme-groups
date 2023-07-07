import unittest
from typing import Dict
from src.groups.generator import Generator, ValueTypeGroup, ValueType, Unit
from src.groups.value import Value


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def test_type_groups(self):
        self.assertEqual(self.generator.type_groups, {})
        self.generator.add_type_group('numbers')
        self.assertEqual(len(self.generator.type_groups), 1)
        self.assertIn('numbers', self.generator.type_groups)
        self.assertIsInstance(self.generator.type_groups['numbers'], ValueTypeGroup)
        self.generator.remove_type_group('numbers')
        self.assertEqual(self.generator.type_groups, {})

    def test_types(self):
        self.assertEqual(self.generator.types, {})
        self.generator.add_type_group('numbers')
        self.generator.type_groups['numbers'].add_type('int')
        self.generator.type_groups['numbers'].add_type('float')
        self.assertEqual(len(self.generator.types), 2)
        self.assertIn('int', self.generator.types)
        self.assertIsInstance(self.generator.types['int'], ValueType)
        self.assertIn('float', self.generator.types)
        self.assertIsInstance(self.generator.types['float'], ValueType)

    def test_units(self):
        self.assertEqual(self.generator.units, {})
        self.generator.add_unit('answer', 'int', 42)
        self.assertEqual(len(self.generator.units), 1)
        self.assertIn('answer', self.generator.units)
        self.assertIsInstance(self.generator.units['answer'], Unit)
        self.assertEqual(self.generator.units['answer'].type.name, 'int')
        self.assertEqual(self.generator.units['answer'].value.value, 42)

    def test_add_type_group(self):
        self.assertEqual(self.generator.type_groups, {})
        self.generator.add_type_group('numbers')
        self.assertEqual(len(self.generator.type_groups), 1)
        self.assertIn('numbers', self.generator.type_groups)
        self.assertIsInstance(self.generator.type_groups['numbers'], ValueTypeGroup)

        with self.assertRaises(ValueError):
            self.generator.add_type_group('numbers')

    def test_remove_type_group(self):
        self.assertEqual(self.generator.type_groups, {})
        self.generator.add_type_group('numbers')
        self.assertEqual(len(self.generator.type_groups), 1)
        self.assertIn('numbers', self.generator.type_groups)
        self.assertIsInstance(self.generator.type_groups['numbers'], ValueTypeGroup)

        self.generator.remove_type_group('numbers')
        self.assertEqual(self.generator.type_groups, {})

        with self.assertRaises(ValueError):
            self.generator.remove_type_group('numbers')

    def test_add_unit(self):
        self.assertEqual(self.generator.units, {})
        self.generator.add_type_group('numbers')
        self.generator.type_groups['numbers'].add_type('int')
        self.generator.add_unit('answer', 'int', 42)
        self.assertEqual(len(self.generator.units), 1)
        self.assertIn('answer', self.generator.units)
        self.assertIsInstance(self.generator.units['answer'], Unit)
        self.assertEqual(self.generator.units['answer'].type.name, 'int')
        self.assertEqual(self.generator.units['answer'].value.value, 42)

    def test_remove_unit(self):
        self.assertEqual(self.generator.units, {})
        self.generator.add_type_group('numbers')
        self.generator.type_groups['numbers'].add_type('int')
        self.generator.add_unit('answer', 'int', 42)
        self.assertEqual(len(self.generator.units), 1)
        self.assertIn('answer', self.generator.units)
        self.assertIsInstance(self.generator.units['answer'], Unit)

        self.generator.remove_unit('answer')
        self.assertEqual(self.generator.units, {})

        with self.assertRaises(ValueError):
            self.generator.remove_unit('answer')