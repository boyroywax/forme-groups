import unittest
from src.groups.classes.type import ValueType, ValueTypeGroup


class TestType(unittest.TestCase):
    def test_type_property(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(value_type.type, type_)

    def test_aliases_property(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(value_type.aliases, aliases)

    def test_freeze_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        value_type.freeze()
        with self.assertRaises(Exception):
            value_type.aliases = ['float']
        with self.assertRaises(Exception):
            value_type.type = [float]

    def test_str_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(str(value_type), "ValueType(_aliases=['int', 'integer'], _type=[<class 'int'>], _frozen=False)")

    def test_repr_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(repr(value_type), "ValueType(_aliases=['int', 'integer'], _type=[<class 'int'>], _frozen=False)")

    def test_init_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(value_type._aliases, aliases)
        self.assertEqual(value_type._type, type_)
        self.assertFalse(value_type.frozen)

        frozen_value_type = ValueType(aliases=aliases, type_=type_, freeze=True)
        self.assertTrue(frozen_value_type.frozen)

    def test_default_values(self):
        value_type = ValueType(aliases=[], type_=[], freeze=True)
        self.assertEqual(value_type._aliases, [])
        self.assertEqual(value_type._type, [])
        self.assertTrue(value_type.frozen)

    def test_type_setter_frozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_, freeze=True)
        with self.assertRaises(Exception):
            value_type.type = ['float']

    def test_type_setter_unfrozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_)
        value_type.type = ['float']
        self.assertEqual(value_type.type, ['float'])

    def test_type_getter(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(value_type.type, ['int'])

    def test_aliases_setter_frozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_, freeze=True)
        with self.assertRaises(Exception):
            value_type.aliases = ['float']

    def test_aliases_setter_unfrozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_)
        value_type.aliases = ['float']
        self.assertEqual(value_type.aliases, ['float'])

    def test_aliases_getter(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertEqual(value_type.aliases, ['int', 'integer'])

    def test_frozen_property(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = ValueType(aliases=aliases, type_=type_)
        self.assertFalse(value_type.frozen)

        frozen_value_type = ValueType(aliases=aliases, type_=type_, freeze=True)
        self.assertTrue(frozen_value_type.frozen)


class TestValueTypeGroup(unittest.TestCase):
    def test_name_property(self):
        # test name property
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')

    def test_group_property(self):
        # test group property
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.group, group)

    def test_freeze_property(self):
        # test freeze property
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)

    def test_check_alias_method(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertTrue(value_type_group.check_alias('int'))
        self.assertFalse(value_type_group.check_alias('float'))

    def test_freeze_method(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        value_type_group.freeze()
        self.assertTrue(value_type_group.frozen)
        with self.assertRaises(Exception):
            value_type_group.group['int'].aliases = ['integer']

    def test_init_method(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')
        self.assertEqual(value_type_group.group, group)
        self.assertFalse(value_type_group.frozen)

    def test_frozen_setter_frozen(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group, freeze=True)
        with self.assertRaises(Exception):
            value_type_group.frozen = False

    def test_frozen_setter_unfrozen(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        value_type_group.frozen = True
        self.assertTrue(value_type_group.frozen)

    def test_frozen_getter(self):
        group = {'int': ValueType(aliases=['int'], type_=['int'])}
        value_type_group = ValueTypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)