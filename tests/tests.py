import unittest

from .tests_decorators import TestCheckFrozen
from .tests_value import TestValue
from .tests_value_type import TestValueType
from .tests_value_type_group import TestValueTypeGroup


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestCheckFrozen))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestValue))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestValueType))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestValueTypeGroup))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
