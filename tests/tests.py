import unittest

# from .tests_super import TestSuper
from .tests_defaults import TestDefaults
from .tests_defined import TestDefined
from .tests_types import TestTypes


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestSuper))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDefaults))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDefined))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestTypes))


    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
