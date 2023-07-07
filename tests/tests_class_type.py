import unittest
from src.groups.type import Type
from src.groups.type_group import TypeGroup


class TestType(unittest.TestCase):
    def test_type_property(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(value_type.type, type_)

    def test_aliases_property(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(value_type.aliases, aliases)

    def test_freeze_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        value_type.freeze()
        with self.assertRaises(Exception):
            value_type.aliases = ['float']
        with self.assertRaises(Exception):
            value_type.type = [float]

    def test_str_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(str(value_type), "Type(_aliases=['int', 'integer'], _type=[<class 'int'>], _frozen=False)")

    def test_repr_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(repr(value_type), "Type(_aliases=['int', 'integer'], _type=[<class 'int'>], _frozen=False)")

    def test_init_method(self):
        aliases = ['int', 'integer']
        type_ = [int]
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(value_type._aliases, aliases)
        self.assertEqual(value_type._type, type_)
        self.assertFalse(value_type.frozen)

        frozen_value_type = Type(aliases=aliases, type_=type_, freeze=True)
        self.assertTrue(frozen_value_type.frozen)

    def test_default_values(self):
        value_type = Type(aliases=[], type_=[], freeze=True)
        self.assertEqual(value_type._aliases, [])
        self.assertEqual(value_type._type, [])
        self.assertTrue(value_type.frozen)

    def test_type_setter_frozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_, freeze=True)
        with self.assertRaises(Exception):
            value_type.type = ['float']

    def test_type_setter_unfrozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_)
        value_type.type = ['float']
        self.assertEqual(value_type.type, ['float'])

    def test_type_getter(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(value_type.type, ['int'])

    def test_aliases_setter_frozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_, freeze=True)
        with self.assertRaises(Exception):
            value_type.aliases = ['float']

    def test_aliases_setter_unfrozen(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_)
        value_type.aliases = ['float']
        self.assertEqual(value_type.aliases, ['float'])

    def test_aliases_getter(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_)
        self.assertEqual(value_type.aliases, ['int', 'integer'])

    def test_frozen_property(self):
        aliases = ['int', 'integer']
        type_ = ['int']
        value_type = Type(aliases=aliases, type_=type_)
        self.assertFalse(value_type.frozen)

        frozen_value_type = Type(aliases=aliases, type_=type_, freeze=True)
        self.assertTrue(frozen_value_type.frozen)


class TestTypeGroup(unittest.TestCase):
    def test_name_property(self):
        # test name property
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')

    def test_group_property(self):
        # test group property
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.group, group)

    def test_freeze_property(self):
        # test freeze property
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)

    def test_check_alias_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertTrue(value_type_group.check_alias(['int']))
        self.assertFalse(value_type_group.check_alias(['float']))

    def test_freeze_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        value_type_group.freeze()
        self.assertTrue(value_type_group.frozen)
        with self.assertRaises(Exception):
            value_type_group.group['int'].aliases = ['integer']

    def test_init_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertEqual(value_type_group.name, 'test')
        self.assertEqual(value_type_group.group, group)
        self.assertFalse(value_type_group.frozen)

    def test_frozen_setter_frozen(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group, freeze=True)
        with self.assertRaises(Exception):
            value_type_group.frozen = False

    def test_frozen_setter_unfrozen(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        value_type_group.frozen = True
        self.assertTrue(value_type_group.frozen)

    def test_frozen_getter(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertFalse(value_type_group.frozen)

    def test_check_name_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        self.assertTrue(value_type_group.check_name('test'))
        self.assertFalse(value_type_group.check_name('float'))

    def test_add_method_alias_in_use(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.add(Type(aliases=['int'], type_=[int]))

    def test_add_method_name_in_use(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.add(Type(aliases=['integer'], type_=[int]), name='int')

    def test_add_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        value_type_group.add(Type(aliases=['float'], type_=[float]))
        with self.assertRaises(ValueError):
            value_type_group.add(Type(aliases=['integer'], type_=[int]))

    def test_remove_method_alias_not_in_use(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        with self.assertRaises(ValueError):
            value_type_group.remove(['float'])

    def test_remove_method(self):
        group = {'int': Type(aliases=['int'], type_=[int])}
        value_type_group = TypeGroup(name='test', group=group)
        value_type_group.remove(aliases=['int'])
        self.assertFalse(value_type_group.check_alias(['int']))

    def test_has_alias_method(self):
        self.group = {
            'int': Type(aliases=['int'], type_=['int']),
            'float': Type(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = TypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.has_alias('int'), 'int')
        self.assertEqual(self.value_type_group.has_alias('double'), 'float')
        self.assertIsNone(self.value_type_group.has_alias('str'))

    def test_get_aliases_method(self):
        self.group = {
            'int': Type(aliases=['int'], type_=['int']),
            'float': Type(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = TypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.get_aliases(), ['int', 'float', 'double'])

    def test_get_value_type_method(self):
        self.group = {
            'int': Type(aliases=['int'], type_=['int']),
            'float': Type(aliases=['float', 'double'], type_=['float'])
        }
        self.value_type_group = TypeGroup(name='test', group=self.group)
        self.assertEqual(self.value_type_group.get_value_type(alias='int'), self.group['int'])
        self.assertEqual(self.value_type_group.get_value_type(alias='float'), self.group['float'])
        self.assertIsNone(self.value_type_group.get_value_type(alias='str'))
        self.assertEqual(self.value_type_group.get_value_type(value_type_id='int'), self.group['int'])
        self.assertEqual(self.value_type_group.get_value_type(value_type_id='float'), self.group['float'])
        self.assertIsNone(self.value_type_group.get_value_type(value_type_id='str'))
