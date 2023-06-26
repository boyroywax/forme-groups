import unittest

from .tests_value import TestValue
# from .tests_system import TestSystem
from .tests_unit import TestUnit
from .tests_type import TestType


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestValue))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestSystem))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestType))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
