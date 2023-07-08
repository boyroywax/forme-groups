import unittest
from dataclasses import dataclass
from src.groups.all import UnitTypeRef, UnitValue, UnitType, frozen, Frozen


class TestAll(unittest.TestCase):
    def test_unit_type_ref(self):
        type_ref = int
        unit_type_ref = UnitTypeRef(type_ref)

        self.assertEqual(unit_type_ref.type_ref, type_ref)

    def test_frozen(self):
        unit_type_ref = Frozen(UnitTypeRef(int))

        with self.assertRaises(AttributeError):
            unit_type_ref.type_ref = float

    def test_frozen_decorator(self):
        
        @frozen
        class MyClass:
            def __init__(self, *args, **kwargs):
                self._test = True

        class MyClassNotFrozen:
            def __init__(self):
                self._frozen = False

        # with self.assertRaises(Exception):
        myClassNF = MyClassNotFrozen()
        self.assertFalse(myClassNF._frozen)

        myClass = MyClass()
        self.assertTrue(myClass._frozen)

        with self.assertRaises(AttributeError):
            myClass._frozen = False

    def test_unit_value(self):
        value = 42
        unit_value = UnitValue(value)

        self.assertEqual(unit_value.value, value)

    def test_frozen_class(self):
        @frozen
        class MyClass:
            my_attribute: int = 42

        my_class = MyClass()
        self.assertEqual(my_class.my_attribute, 42)

        with self.assertRaises(AttributeError):
            my_class.my_attribute = 43

        with self.assertRaises(AttributeError):
            del my_class.my_attribute

    def test_frozen_subclass(self):
        @frozen
        class MyBaseClass:
            my_attribute: int = 42

        class MySubClass(MyBaseClass):
            pass

        my_subclass = MySubClass()
        self.assertEqual(my_subclass.my_attribute, 42)

        with self.assertRaises(AttributeError):
            my_subclass.my_attribute = 43

        with self.assertRaises(AttributeError):
            del my_subclass.my_attribute

    def test_frozen_args(self):
        @frozen
        class MyClass:
            arg1: int
            arg2: int

            def __init__(self, *args, **kwargs):

                if args:
                    self.arg1, self.arg2 = args
                else:
                    self.arg1 = kwargs.pop('arg1')
                    self.arg2 = kwargs.pop('arg2')

        # my_class = MyClass(1, 2)
        my_class = MyClass(arg1=1, arg2=2)
        self.assertEqual(my_class.arg1, 1)
        self.assertEqual(my_class.arg2, 2)

        with self.assertRaises(AttributeError):
            my_class.arg1 = 3

        with self.assertRaises(AttributeError):
            del my_class.arg2

    def test_frozen_kwargs(self):
        @frozen
        class MyClass:
            def __init__(self, **kwargs):
                self.arg1 = kwargs.pop('arg1')
                self.arg2 = kwargs.pop('arg2')

        my_class = MyClass(arg1=1, arg2=2)
        self.assertEqual(my_class.arg1, 1)
        self.assertEqual(my_class.arg2, 2)

        with self.assertRaises(AttributeError):
            my_class.arg1 = 3

        with self.assertRaises(AttributeError):
            del my_class.arg2

    def test_frozen_args_kwargs(self):
        @frozen
        class MyClass:
            def __init__(self, arg1, arg2, **kwargs):
                self.arg1 = arg1
                self.arg2 = arg2
                self.arg3 = kwargs.pop('arg3')

        my_class = MyClass(1, 2, arg3=3)
        self.assertEqual(my_class.arg1, 1)
        self.assertEqual(my_class.arg2, 2)
        self.assertEqual(my_class.arg3, 3)

        with self.assertRaises(AttributeError):
            my_class.arg1 = 4

        with self.assertRaises(AttributeError):
            del my_class.arg2

        with self.assertRaises(AttributeError):
            del my_class.arg3

    def test_unit(self):
        aliases = (UnitTypeRef(int), UnitTypeRef(float))
        super_type = UnitTypeRef(int)
        prefix = 'prefix'
        suffix = 'suffix'
        separator = ','
        function_call = lambda x: x * 2

        unit = UnitType(
            aliases=aliases,
            super_type=super_type,
            prefix=prefix,
            suffix=suffix,
            separator=separator,
            function_call=function_call
        )

        self.assertEqual(unit.aliases, aliases)
        self.assertEqual(unit.super_type, super_type)
        self.assertEqual(unit.prefix, prefix)
        self.assertEqual(unit.suffix, suffix)
        self.assertEqual(unit.separator, separator)
        self.assertEqual(unit.function_call, function_call)