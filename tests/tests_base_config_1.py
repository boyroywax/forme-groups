import unittest
from src.groups.base.type import Type_


class TestType_(unittest.TestCase):
    def setUp(self):
        self.type1 = Type_("str", "string")
        self.type2 = Type_("string2", "string")
        self.type3 = Type_("string3", "string", ["str3"], "prefix3:", ":suffix3")

    def test_get_full(self):
        self.assertEqual(self.type1.get_full(), "int")
        self.assertEqual(self.type2.get_full(), "float")

    def test_get_full_with_super(self):
        self.assertEqual(self.type1.get_full_with_super(), "int")
        self.assertEqual(self.type2.get_full_with_super(), "float")

    def test_str(self):
        self.assertEqual(str(self.type1), "int")
        self.assertEqual(str(self.type2), "float")

    def test_repr(self):
        self.assertEqual(repr(self.type1), "int")
        self.assertEqual(repr(self.type2), "float")

    def test_eq(self):
        self.assertEqual(self.type1, self.type3)
        self.assertNotEqual(self.type1, self.type2)

    def test_ne(self):
        self.assertNotEqual(self.type1, self.type2)
        self.assertNotEqual(self.type2, self.type3)

    def test_hash(self):
        self.assertEqual(hash(self.type1), hash(self.type3))
        self.assertNotEqual(hash(self.type1), hash(self.type2))
