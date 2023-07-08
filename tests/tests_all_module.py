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
                # self._frozen = False

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

    # def test_unit_type_interface(self):
    #     aliases = (UnitTypeRef(int), UnitTypeRef(float))
    #     super_type = UnitTypeRef(int)
    #     prefix = 'prefix'
    #     suffix = 'suffix'
    #     separator = ','
    #     function_call = lambda x: x * 2

    #     unit_type_interface = UnitTypeInterface(
    #         aliases=aliases,
    #         super_type=super_type,
    #         prefix=prefix,
    #         suffix=suffix,
    #         separator=separator,
    #         function_call=function_call
    #     )

    #     self.assertEqual(unit_type_interface.aliases, aliases)
    #     self.assertEqual(unit_type_interface.super_type, super_type)
    #     self.assertEqual(unit_type_interface.prefix, prefix)
    #     self.assertEqual(unit_type_interface.suffix, suffix)
    #     self.assertEqual(unit_type_interface.separator, separator)
    #     self.assertEqual(unit_type_interface.function_call, function_call)

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