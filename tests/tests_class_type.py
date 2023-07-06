import unittest
from src.groups.classes.type import ValueType


class TestType(unittest.TestCase):
    # def setUp(self):
    #     self.type_ = ValueType(["int", "integer"], [int])

    # def test_type(self):
    #     # Test initialization
    #     self.assertEqual(self.type_.aliases, ["int", "integer"])
    #     self.assertEqual(self.type_.type, [int])

    #     # Test check_alias method
    #     self.assertTrue(self.type_.check_alias("int"))
    #     self.assertTrue(self.type_.check_alias("integer"))
    #     self.assertFalse(self.type_.check_alias("float"))

    # def test_name(self):
    #     # Test name method
    #     self.assertEqual(self.type_.name(), "ValueType")

    # def test_freeze(self):
    #     # Test freeze method
    #     self.type_.freeze()
    #     self.assertTrue(self.type_.frozen)

    # def test_frozen(self):
    #     # Test try_frozen method
    #     self.type_.freeze()
    #     with self.assertRaises(Exception):
    #         self.type_.aliases = ["float"]

    # def test_not_frozen(self):
    #     # Test inputing data into a non frozen class.
    #     # Expect an error for no setter.
    #     # This is desired behavior as value types should not be changed.
    #     with self.assertRaises(Exception):
    #         self.type_.aliases = ["float"]

    # def test_repr_not_frozen(self):
    #     # Test __repr__ method
    #     self.assertEqual(repr(self.type_), "ValueType(aliases=['int', 'integer'], type=[<class 'int'>], frozen=False)")

    # def test_repr_frozen(self):
    #     # Test __repr__ method
    #     self.type_.freeze()
    #     self.assertEqual(repr(self.type_), "ValueType(aliases=['int', 'integer'], type=[<class 'int'>], frozen=True)")



# class TestValueType(unittest.TestCase):
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