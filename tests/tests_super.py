import unittest
from src.groups.units.base.super import Super__

class TestSuper(unittest.TestCase):
    def test_init(self):
        # Test initializing the Super__ class with a valid super type
        super_ = str
        super_obj = Super__(super_)
        self.assertEqual(super_obj.get_super(), super_)

        # # Test initializing the Super__ class with None
        # with self.assertRaises(ValueError):
        #     super_obj = Super__(None)

        # # Test initializing the Super__ class with an invalid super type
        # with self.assertRaises(ValueError):
        #     super_obj = Super__(123)

    def test_check_for_none(self):
        # Test checking for None
        
        # with self.assertRaises(ValueError):
        #     super_obj.check_for_none(None)

        with self.assertRaises(TypeError):
            super_obj = Super__()

    def test_check_for_type(self):
        # Test checking for a valid super type
        super_obj = Super__(str())
        self.assertTrue(super_obj.check_for_type(str))
        self.assertTrue(super_obj.check_for_type(int))
        self.assertTrue(super_obj.check_for_type(float))
        self.assertTrue(super_obj.check_for_type(bool))
        self.assertTrue(super_obj.check_for_type(list))
        self.assertTrue(super_obj.check_for_type(dict))
        self.assertTrue(super_obj.check_for_type(tuple))
        self.assertTrue(super_obj.check_for_type(bytes))

        # Test checking for an invalid super type
        self.assertFalse(super_obj.check_for_type(123))
        with self.assertRaises(ValueError):
            super_obj.check_for_type("[test}")

    def test_check_for_type_name(self):
        # Test checking for a valid super type name
        super_obj = Super__(str)
        self.assertTrue(super_obj.check_for_type_name("str"))
        self.assertTrue(super_obj.check_for_type_name("int"))
        self.assertTrue(super_obj.check_for_type_name("float"))
        self.assertTrue(super_obj.check_for_type_name("bool"))
        self.assertTrue(super_obj.check_for_type_name("list"))
        self.assertTrue(super_obj.check_for_type_name("dict"))
        self.assertTrue(super_obj.check_for_type_name("tuple"))
        self.assertTrue(super_obj.check_for_type_name("bytes"))

        # Test checking for an invalid super type name
        self.assertFalse(super_obj.check_for_type_name("invalid_type"))

    def test_get_type_from_str_name(self):
        # Test getting a valid type from a super type name
        super_obj = Super__(str)
        self.assertEqual(super_obj.get_type_from_str_name("str"), str)

        super_obj.set_super(int)
        self.assertEqual(super_obj.get_type_from_str_name("int"), int)

        super_obj.set_super(float)
        self.assertEqual(super_obj.get_type_from_str_name("float"), float)

        super_obj.set_super(bool)
        self.assertEqual(super_obj.get_type_from_str_name("bool"), bool)
        
        super_obj.set_super(list)
        self.assertEqual(super_obj.get_type_from_str_name("list"), list)
        
        super_obj.set_super(dict)
        self.assertEqual(super_obj.get_type_from_str_name("dict"), dict)
        
        super_obj.set_super(tuple)
        self.assertEqual(super_obj.get_type_from_str_name("tuple"), tuple)
        
        super_obj.set_super(bytes)
        self.assertEqual(super_obj.get_type_from_str_name("bytes"), bytes)

        # Test getting an invalid type from a super type name
        with self.assertRaises(AssertionError):
            super_obj.get_type_from_str_name("invalid_type")

    def test_set_super(self):
        # Test setting a valid super type
        super_obj = Super__(str)
        # super_obj.set_super(str)
        self.assertEqual(super_obj._super__, str)

        # Test setting an invalid super type
        super_obj = Super__(int)
        with self.assertRaises(ValueError):
            super_obj.check_and_set_super(123)

    def test_check_and_set_super(self):
        # Test checking and setting a valid super type
        super_obj = Super__(str)
        super_obj.check_and_set_super(str)
        self.assertEqual(super_obj._super__, str)

        # Test checking and setting None
        with self.assertRaises(ValueError):
            super_obj.check_and_set_super(None)


        # Test checking and setting an invalid super type
        with self.assertRaises(ValueError):
            super_obj.check_and_set_super("[test}")