import unittest
from attr.exceptions import FrozenInstanceError
from unittest.mock import MagicMock

import sys
sys.path.append('/Users/j/Documents/Forme/code/forme-groups')

from src.groups.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def test_value(self):
        value = self.base.Value_(123)
        self.assertEqual(value._value, 123)

    def test_value_frozen(self):
        value = self.base.Value_(123)
        with self.assertRaises(FrozenInstanceError):
            value._value = 456

    def test_value_slots(self):
        value = self.base.Value_(123)
        self.assertEqual(value.__slots__, ('_value',))

    def test_value_str(self):
        value = self.base.Value_(123)
        self.assertEqual(str(value), '123')

    def test_value_repr(self):
        value = self.base.Value_(123)
        self.assertEqual(repr(value), '123')

    def test_value_hash(self):
        value = self.base.Value_(123)
        self.assertEqual(value.__hash__(), 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')
        value2 = self.base.Value_(456)
        self.assertNotEqual(value.__hash__(), value2.__hash__())

    def test_callable(self):
        func = MagicMock()
        args = [self.base.Value_(123), self.base.Value_(456)]
        callable_ = self.base.Callable_(func, args)
        self.assertEqual(callable_._function, func)
        self.assertEqual(callable_._args, args)

    def test_callable_frozen(self):
        func = MagicMock()
        args = [self.base.Value_(123), self.base.Value_(456)]
        callable_ = self.base.Callable_(func, args)
        with self.assertRaises(FrozenInstanceError):
            callable_._function = MagicMock()
        with self.assertRaises(FrozenInstanceError):
            callable_._args = MagicMock()

    def test_callable_slots(self):
        func = MagicMock()
        args = [self.base.Value_(123), self.base.Value_(456)]
        callable_ = self.base.Callable_(func, args)
        self.assertEqual(callable_.__slots__, ('_function', '_args'))

    def test_callable_call(self):
        func = MagicMock()
        args = [self.base.Value_(123), self.base.Value_(456)]
        callable_ = self.base.Callable_(func, args)
        input_ = self.base.Value_(789)
        callable_(input_)
        func.assert_called_with(input_._value, *args)

    def test_function(self):
        callable_ = self.base.Callable_(str, [])
        function = self.base.Function_(callable_)
        print(function.__call__(self.base.Value_(123)))



    def test_container(self):
        prefix = self.base.Value_('prefix')
        suffix = self.base.Value_('suffix')
        sep = self.base.Value_('sep')
        container = self.base.Container_(prefix, suffix, sep)
        self.assertEqual(container._prefix, prefix)
        self.assertEqual(container._suffix, suffix)
        self.assertEqual(container._separator, sep)

