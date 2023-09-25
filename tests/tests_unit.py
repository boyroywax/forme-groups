import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def test_value(self):
        value = self.base.Value_(123)
        self.assertEqual(value._value, 123)

    def test_function(self):
        value = self.base.Value_(123)
        func = self.base.Function_(value, [value])
        self.assertEqual(func._object, value)
        self.assertEqual(func._args, [value])

    def test_container(self):
        prefix = self.base.Value_('prefix')
        suffix = self.base.Value_('suffix')
        sep = self.base.Value_('sep')
        container = self.base.Container_(prefix, suffix, sep)
        self.assertEqual(container._prefix, prefix)
        self.assertEqual(container._suffix, suffix)
        self.assertEqual(container._separator, sep)

    def test_type(self):
        aliases = [self.base.Value_('alias1'), self.base.Value_('alias2')]
        super_type = self.base.Type_(aliases, None, False, None, None)
        container = self.base.Container_(None, None, None)
        func = self.base.Function_(None, [])
        typ = self.base.Type_(aliases, super_type, True, container, func)
        self.assertEqual(typ._aliases, aliases)
        self.assertEqual(typ._super_type, super_type)
        self.assertTrue(typ._is_container)
        self.assertEqual(typ._container, container)
        self.assertEqual(typ._function, func)

    def test_schema(self):
        unit1 = self.base.Unit_(self.base.Value_('value1'), self.base.Type_([], None, False, None, None))
        unit2 = self.base.Unit_(self.base.Value_('value2'), self.base.Type_([], None, False, None, None))
        pattern = {unit1: unit2}
        schema = self.base.Schema_(pattern)
        self.assertEqual(schema._pattern, pattern)

    def test_unit(self):
        value = self.base.Value_('value')
        typ_ref = self.base.Type_.Reference_(self.base.Value_('alias'))
        unit = self.base.Unit_(value, typ_ref)
        self.assertEqual(unit._value, value)
        self.assertEqual(unit._type_ref, typ_ref)

    def test_type_pool(self):
        typ1 = self.base.Type_([], None, False, None, None)
        typ2 = self.base.Type_([], None, False, None, None)
        pool = self.base.Type_Pool_([typ1, typ2])
        self.assertEqual(pool._types, [typ1, typ2])

    def test_unit_pool(self):
        value = self.base.Value_('value')
        typ_ref = self.base.Type_.Reference_(self.base.Value_('alias'))
        unit = self.base.Unit_(value, typ_ref)
        pool = self.base.Unit_Pool_([unit])
        self.assertEqual(pool._units, [unit])

    def test_group(self):
        type_pool = self.base.Type_Pool_([self.base.Type_([], None, False, None, None)])
        unit_pool = self.base.Unit_Pool_([self.base.Unit_(self.base.Value_('value'), self.base.Type_.Reference_(self.base.Value_('alias')))])
        group = self.base.Group_(type_pool, unit_pool)
        self.assertEqual(group._type_pool, type_pool)
        self.assertEqual(group._unit_pool, unit_pool)