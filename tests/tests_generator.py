import unittest
from typing import Dict
from src.groups.generator import Generator, ValueTypeGroup, ValueType, Unit
from src.groups.value import Value
from src.groups.value_type import ValueTypeRef


class TestGenerator(unittest.TestCase):
    def setUp(self):
        name = 'my_group'
        value_type = ValueTypeRef('int')
        value_type_group = ValueTypeGroup(name, (value_type))
        self.generator = Generator((value_type_group))

    def test_type_groups(self):
        self.assertEqual(self.generator.type_groups, ())


        # value_type_group = ValueTypeGroup(name)
        self.generator.add_type_group(value_type_group)

        self.assertEqual(self.generator.type_groups, {name: value_type_group})

    def test_types(self):
        self.assertEqual(self.generator.types, ())

        name = 'int'
        base_types = ['int']
        value_type = ValueTypeRef(name)
        value_type_group = ValueTypeGroup('my_group', {name: value_type})
        self.generator.add_type_group(value_type_group.name)

        self.assertEqual(self.generator.types, {name: value_type})

    def test_units(self):
        self.assertEqual(self.generator.units, ())

        class MyUnit(Unit):
            pass

        name = 'my_unit'
        unit = MyUnit(ValueTypeRef('int'), Value(42))
        self.generator._units = unit

        self.assertEqual(self.generator.units, (unit))