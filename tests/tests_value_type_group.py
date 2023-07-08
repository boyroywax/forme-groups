import unittest

from src.groups.value_type import ValueType
from src.groups.value_type_group import ValueTypeGroup


class TestValueTypeGroup(unittest.TestCase):
    def test_name_property(self):
        # test name property
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')

    def test_group_property(self):
        # test group property
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.group, group)

    def test_freeze_property(self):
        # test freeze property
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)

    def test_check_alias_method(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertTrue(value_type_group.check_alias(['int']))
        self.assertFalse(value_type_group.check_alias(['float']))

    def test_freeze_method(self):
        group = (ValueType(aliases=['int'], type_=[int]))
        value_type_group = ValueTypeGroup(name='test', group=group, level=0)
        value_type_group.freeze()
        self.assertTrue(value_type_group.frozen)
        with self.assertRaises(Exception):
            value_type_group.group['int'].aliases = ['integer']

    def test_init_method(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')
        self.assertEqual(value_type_group.group, group)
        self.assertFalse(value_type_group.frozen)

    def test_frozen_setter_frozen(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group, freeze=True)
        with self.assertRaises(Exception):
            value_type_group.frozen = False

    def test_frozen_setter_unfrozen(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        with self.assertRaises(Exception):
            value_type_group.frozen = True
        # self.assertTrue(value_type_group.frozen)

    def test_frozen_getter(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)

    def test_check_name_method(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertTrue(value_type_group.check_name('test'))
        self.assertFalse(value_type_group.check_name('float'))

    def test_add_method_alias_in_use(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.add(ValueType(aliases=['int'], type_=[int]))

    def test_add_method_name_in_use(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.add(ValueType(aliases=['integer'], type_=[int]), name='int')

    def test_add_method(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        value_type_group.add(ValueType(aliases=['float'], type_=[float]))
        with self.assertRaises(ValueError):
            value_type_group.add(ValueType(aliases=['integer'], type_=[int]))

    def test_remove_method_alias_not_in_use(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.remove(['float'])

    def test_remove_method(self):
        group = tuple(ValueType(aliases=['int'], type_=(int)))
        value_type_group = ValueTypeGroup(name='test', group=group)
        value_type_group.remove(aliases=['int'])
        self.assertFalse(value_type_group.check_alias(['int']))

    def test_has_alias_method(self):
        self.group = {
            'int': ValueType(aliases=['int'], type_=['int']),
            'float': ValueType(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = ValueTypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.has_alias('int'), 'int')
        self.assertEqual(self.value_type_group.has_alias('double'), 'float')
        self.assertIsNone(self.value_type_group.has_alias('str'))

    def test_get_aliases_method(self):
        self.group = {
            'int': ValueType(aliases=['int'], type_=['int']),
            'float': ValueType(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = ValueTypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.get_aliases(), ('int', 'float', 'double'))

    def test_get_value_type_method(self):
        self.group = {
            'int': ValueType(aliases=['int'], type_=['int']),
            'float': ValueType(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = ValueTypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.get_value_type(alias='int'), self.group['int'])
        self.assertEqual(self.value_type_group.get_value_type(alias='float'), self.group['float'])
        self.assertIsNone(self.value_type_group.get_value_type(alias='str'))
        self.assertEqual(self.value_type_group.get_value_type(value_type_id='int'), self.group['int'])
        self.assertEqual(self.value_type_group.get_value_type(value_type_id='float'), self.group['float'])
        self.assertIsNone(self.value_type_group.get_value_type(value_type_id='str'))


    def setUp__(self):
        self.int_type = ValueType(['int'], ['int'])
        self.float_type = ValueType(['float'], ['float'])
        self.group = ValueTypeGroup('numbers', tuple(self.int_type, self.float_type))

    def test_group_getter(self):
        self.setUp__()
        self.assertEqual(self.group.group, tuple(self.int_type, self.float_type))

    def test_group_setter(self):
        self.setUp__()
        new_group = tuple(self.int_type)
        self.group.group = new_group
        self.assertEqual(self.group.group, new_group)

    def test_group_deleter(self):
        self.setUp__()
        self.group.group.__delitem__('int')
        self.assertEqual(self.group.group, {'float': self.float_type})
        self.group.group.__delitem__('float')
        self.assertEqual(self.group.types, ())

    def test_freeze(self):
        self.setUp__()
        self.assertFalse(self.group.frozen)
        self.group.level = 1
        self.group.freeze()
        self.assertTrue(self.group.frozen)
        self.assertTrue(self.int_type.frozen)
        self.assertTrue(self.float_type.frozen)

    def test_name_getter(self):
        self.setUp__()
        self.assertEqual(self.group.name, 'numbers')

    def test_name_setter(self):
        self.setUp__()
        new_name = 'new_numbers'
        self.group.name = new_name
        self.assertEqual(self.group.name, new_name)

    def test_name_setter_with_existing_name(self):
        self.setUp__()
        with self.assertRaises(ValueError):
            self.group.name = 'numbers'
