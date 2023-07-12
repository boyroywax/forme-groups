import unittest
from dataclasses import dataclass
from src.groups.all import UnitTypeRef, UnitValue, UnitType, UnitTypePool, frozen, Frozen, Unit, Generator


class TestAll(unittest.TestCase):
    def test_unit_type_ref(self):
        type_ref = int
        unit_type_ref = UnitTypeRef(type_ref)

        self.assertEqual(unit_type_ref.type_ref, type_ref)

    def test_frozen(self):
        unit_type_ref = UnitTypeRef(int)
        unit_type_ref = Frozen(unit_type_ref)

        print(unit_type_ref.__dir__())
        unit_type_ref.freeze()
        print(unit_type_ref.__dir__())

        self.assertEqual(unit_type_ref.type_ref, int)
        self.assertEqual(unit_type_ref.__class__.__name__, "FrozenUnitTypeRef")

        with self.assertRaises(AttributeError):
            unit_type_ref.type_ref = float

        with self.assertRaises(AttributeError):
            del unit_type_ref.type_ref

    def test_frozen_subclass_name(self):
        unit_type_ref = UnitTypeRef(int)
        unit_type = UnitType((unit_type_ref))
        unit = Frozen(unit_type)
        self.assertEqual(unit.__class__.__name__, "FrozenUnitType")

    def test_frozen_subclass_name_again(self):
        unit_type_ref = UnitTypeRef(int)
        unit_type = UnitType((unit_type_ref))
        value = UnitValue(42)
        unit = Unit(value, unit_type)
        unit = Frozen(unit)
        self.assertEqual(unit.__class__.__name__, "FrozenUnit")

    def test_frozen_decorator(self):

        @frozen
        @dataclass(slots=True)
        class MyClass:
            def __init__(self, *args, **kwargs):
                self._test = True

        class MyClassNotFrozen:
            def __init__(self):
                self._frozen = False

        self.assertEqual(MyClass.__name__, "FrozenMyClass")

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
        @dataclass(slots=True)
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

    def test_add_type(self):
        pool = UnitTypePool()
        with self.assertRaises(ValueError):
            pool.add_type(name="my_type", unit_type=UnitType(aliases=(UnitTypeRef("int"),)))
        self.assertNotIn("my_type", pool.pool.keys())


    def test_get_type(self):
        pool = UnitTypePool()
        pool.add_type(name="my_type", unit_type=UnitType(aliases=(UnitTypeRef("my_type"),)))
        my_type = pool.get_type(name="my_type")
        self.assertEqual(my_type.aliases, (UnitTypeRef("my_type"),))

    def test_get_type_with_alias(self):
        pool = UnitTypePool()
        pool.add_type(name="my_type", unit_type=UnitType(aliases=(UnitTypeRef("type1"),)))
        my_type = pool.get_type(alias=UnitTypeRef("type1"))
        self.assertEqual(my_type.aliases, (UnitTypeRef("type1"),))

    def test_get_type_with_missing_type(self):
        pool = UnitTypePool()
        with self.assertRaises(ValueError):
            pool.get_type(name="my_type")

    def test_get_type_with_missing_alias(self):
        pool = UnitTypePool()
        # pool.add_type(name="my_type", unit_type=UnitType(aliases=(UnitTypeRef("int"),)))
        # with self.assertRaises(ValueError):
        pool.get_type("float")

    def test_system_reserved(self):
        pool = UnitTypePool()
        pool.__SYSTEM_RESERVED__()
        self.assertIn("integer", pool.pool)
        self.assertIn("float", pool.pool)
        self.assertIn("string", pool.pool)
        self.assertIn("boolean", pool.pool)
        self.assertEqual(pool.pool["integer"].aliases, (UnitTypeRef("integer"), UnitTypeRef("int"),))
        self.assertEqual(pool.pool["float"].aliases, (UnitTypeRef("float"), UnitTypeRef("double"), UnitTypeRef("FLOAT"), UnitTypeRef("DOUBLE")))
        self.assertEqual(pool.pool["string"].aliases, (UnitTypeRef("string"), UnitTypeRef("STRING")))
        self.assertEqual(pool.pool["boolean"].aliases, (UnitTypeRef("boolean"), UnitTypeRef("BOOLEAN")))

    def setUpPool(self):
        self.pool = UnitTypePool()

    def test_add_type_(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(unit_type=UnitType(aliases=(UnitTypeRef("int"),)))
        self.assertIn(UnitType(aliases=(UnitTypeRef(type_ref='integer'), UnitTypeRef("int")), super_type=UnitTypeRef(type_ref='__RESERVED_INT__'), prefix=None, suffix=None, separator=None, function_call=int), self.pool.pool.values())

    def test_add_type_with_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(unit_type=UnitType(aliases=(UnitTypeRef("int"),)), name="my_type")
        self.assertNotIn("my_type", self.pool.pool)

    def test_get_type_by_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(UnitType(aliases=(UnitTypeRef("int"),)), name="my_type")
        with self.assertRaises(ValueError):
            my_type = self.pool.get_type(name="my_type")

        reserved_type = self.pool.get_type(alias=UnitTypeRef("int"))
        self.assertEqual(reserved_type.aliases, (UnitTypeRef("integer"), UnitTypeRef("int"),))

    def test_get_type_by_alias(self):
        self.setUpPool()

        self.pool.add_type(UnitType(aliases=(UnitTypeRef("integer1"),)), name="my_type")
        my_type = self.pool.get_type(alias=UnitTypeRef("integer1"))
        self.assertEqual(my_type.aliases, (UnitTypeRef("integer1"),))

    def test_get_type_with_missing_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.get_type(name="my_type")

    def test_get_type_with_missing_alias_(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.get_type(alias=UnitTypeRef("int1"))

    def test_remove_type_by_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(UnitType(aliases=(UnitTypeRef("int"),)), name="my_type")
        with self.assertRaises(ValueError):
            self.pool.remove_type(name="my_type")
        self.assertNotIn("my_type", self.pool.pool.keys())

    def test_remove_type_by_alias(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(UnitType(aliases=(UnitTypeRef("int"),)), name="my_type")
        self.pool.remove_type(alias=UnitTypeRef("int"))
        self.assertNotIn("my_type", self.pool.pool.keys())

    def test_remove_type_with_missing_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.remove_type(name="my_type")

    def test_remove_type_with_missing_alias(self):
        self.setUpPool()
        self.pool.remove_type(alias=UnitTypeRef("int"))
        self.assertNotIn("int", self.pool.pool.keys())

    def test_add_type_with_reserved_name(self):
        self.setUpPool()
        with self.assertRaises(ValueError):
            self.pool.add_type(UnitType(aliases=(UnitTypeRef("int"),)), name="int")

    def setUpPool2(self):
        self.unit_type_pool = UnitTypePool()
        self.unit_type1 = UnitType(super_type=UnitTypeRef("NONE"), aliases=[UnitTypeRef("None1")], prefix="NONE1:{", suffix="}:NONE1", separator="")
        self.unit_type2 = UnitType(super_type=UnitTypeRef("None1"), aliases=[UnitTypeRef("None2")], prefix="N2:{", suffix="}:N2", separator="")
        self.unit_type_pool.add_type(self.unit_type1)
        self.unit_type_pool.add_type(self.unit_type2)

    def test_get_type_with_pool2(self):
        self.setUpPool2()
        # Test getting a type that exists in the pool
        unit_type = self.unit_type_pool.get_type("None1")
        self.assertEqual(unit_type, self.unit_type1)

        # Test getting a type that inherits from another type in the pool
        unit_type = self.unit_type_pool.get_type("None2")
        self.assertEqual(unit_type, self.unit_type2)

        # Test getting a type that does not exist in the pool
        with self.assertRaises(ValueError):
            self.unit_type_pool.get_type("nonexistent_type")

    def setUpGenerator(self, pool=None):
        if pool is None:
            self.unit_type_pool = UnitTypePool()
        else:
            self.unit_type_pool = pool
        self.unit_type_ref = UnitTypeRef(type_ref="test_type")
        self.unit_type = UnitType(super_type=UnitTypeRef("string"), aliases=[UnitTypeRef("test_type")], prefix="", suffix="", separator="")
        self.unit_type_pool.add_type(self.unit_type)
        self.unit_generator = Generator(unit_type_pool=self.unit_type_pool)

    def test_generate_unit(self):
        self.setUpGenerator()
        unit = self.unit_generator.create_unit(self.unit_type_ref, UnitValue(value="10"))
        self.assertIsInstance(unit, Unit)
        self.assertEqual(unit.value.value, "10")
        self.assertEqual(unit.type_ref.type_ref, "test_type")

    def test_generate_unit_type(self):
        self.setUpGenerator()
        super_type = UnitTypeRef(type_ref="parent_type")
        aliases = [UnitTypeRef(type_ref="alias1"), UnitTypeRef(type_ref="alias2")]
        unit_type = self.unit_generator.create_unit_type(
            super_type=super_type,
            aliases=aliases,
            prefix="",
            suffix="",
            separator="",
        )
        self.assertIsInstance(unit_type, UnitType)
        self.assertEqual(unit_type.super_type.type_ref, "parent_type")
        self.assertEqual(unit_type.aliases, aliases)
        self.assertEqual(unit_type.prefix, "")
        self.assertEqual(unit_type.suffix, "")
        self.assertEqual(unit_type.separator, "")

    def test_generate_unit_type_pool(self):
        self.setUpPool()
        self.setUpGenerator()
        self.maxDiff = None
        unit_type_pool = self.unit_generator.create_unit_type_pool(pool=self.pool)
        self.assertIsInstance(unit_type_pool, UnitTypePool)
        self.assertEqual(unit_type_pool.pool, self.pool.pool)

    def test_generate_unit_value(self):
        self.setUpGenerator()
        unit_value = self.unit_generator.create_unit_value("10")
        self.assertIsInstance(unit_value, UnitValue)
        self.assertEqual(unit_value.value, "10")
        # self.assertEqual(unit_value.unit_typ, self.unit_type

    def test_generate_unit_type_ref(self):
        self.setUpGenerator()
        unit_type_ref = self.unit_generator.create_unit_type_ref("test_type")
        self.assertIsInstance(unit_type_ref, UnitTypeRef)
        self.assertEqual(unit_type_ref.type_ref, "test_type")

    def test_check_pool_for_type(self):
        self.setUpGenerator()
        self.assertTrue(self.unit_generator.check_pool_for_type(UnitTypeRef("int")))
        self.assertFalse(self.unit_generator.check_pool_for_type(UnitTypeRef("int1")))

    def test_check_pool_for_type_with_pool2(self):
        self.setUpPool2()
        self.setUpGenerator(self.unit_type_pool)

        self.assertTrue(self.unit_generator.check_pool_for_type(UnitTypeRef("None1")))
        self.assertTrue(self.unit_generator.check_pool_for_type(UnitTypeRef("None2")))
        self.assertFalse(self.unit_generator.check_pool_for_type(UnitTypeRef("None3")))

    def setUpFrozenPool(self):
        self.setUpPool2()
        self.frozen_pool = Frozen(self.unit_type_pool)
        self.test_type1_ = UnitType(super_type=UnitTypeRef("string"), aliases=[UnitTypeRef("test_type1")], prefix="test1:", suffix=":test1", separator="")
        self.test_type2_ = UnitType(super_type=UnitTypeRef("test_type1"), aliases=[UnitTypeRef("test_type2")], prefix="<", suffix=">", separator="")
        self.frozen_pool.add_type(self.test_type1_)
        self.frozen_pool.add_type(self.test_type2_)
        self.frozen_pool.freeze()

    def test_add_unit_type_frozen(self):
        self.setUpFrozenPool()
        # Test adding a unit type to the pool
        with self.assertRaises(AttributeError):
            self.frozen_pool.add_type(UnitType(super_type=None, aliases=[UnitTypeRef("test")], prefix="test:", suffix=":test", separator=""))

    def test_get_type_frozen(self):
        self.setUpFrozenPool()
        # Test getting a type that exists in the pool
        # test_type1 = UnitType(super_type=UnitTypeRef("string"), aliases=[UnitTypeRef("test_type1")], prefix="test1:", suffix=":test1", separator="")
        unit_type = self.frozen_pool.get_type("test_type1")
        self.assertEqual(unit_type, self.test_type1_)

        # Test getting a type that inherits from another type in the pool
        unit_type = self.frozen_pool.get_type("test_type2")
        self.assertEqual(unit_type, self.test_type2_)

        # Test getting a type that does not exist in the pool
        with self.assertRaises(ValueError):
            self.frozen_pool.get_type("nonexistent_type")

    def test_get_type_ref_frozen(self):
        self.setUpFrozenPool()
        # Test getting a type ref that exists in the pool
        unit_type_ref = self.frozen_pool.get_type("test_type1")
        self.assertEqual(unit_type_ref.aliases[0], UnitTypeRef("test_type1"))

        # Test getting a type ref that does not exist in the pool
        with self.assertRaises(ValueError):
            self.frozen_pool.get_type("nonexistent_type")

    def test_get_type_ref_frozen2(self):
        self.setUpFrozenPool()
        # Test getting a type ref that exists in the pool
        unit_type_ref = self.frozen_pool.get_type("test_type2")
        self.assertEqual(unit_type_ref.aliases[0], UnitTypeRef("test_type2"))

        # Test getting a type ref that does not exist in the pool
        with self.assertRaises(ValueError):
            self.frozen_pool.get_type("nonexistent_type")

    # def test_freeze(self):
    #     class MyClass:
    #         def my_function(self):
    #             print("This is a function defined in MyClass.")

    #     FrozenClass = freeze_class(MyClass)
    #     my_object = FrozenClass()
    #     my_object.freeze()

    #     with self.assertRaises(AttributeError):
    #         my_object.my_function = lambda: print("This is a modified function.")

    # def test_create_instance(self):
    #     class MyClass:
    #         def my_function(self):
    #             print("This is a function defined in MyClass.")

    #     FrozenClass = freeze_class(MyClass)
    #     my_object = FrozenClass()
    #     my_object.freeze()

    #     with self.assertRaises(AttributeError):
    #         my_object.my_function = lambda: print("This is a modified function.")

    #     my_object2 = FrozenClass()
    #     self.assertIsNot(my_object, my_object2)
