import unittest

from src.groups.decorators import check_frozen


class TestCheckFrozen(unittest.TestCase):
    def test_check_frozen(self):
        @check_frozen
        class MyClass:
            def __init__(self):
                self._frozen = True

        with self.assertRaises(Exception):
            obj = MyClass()