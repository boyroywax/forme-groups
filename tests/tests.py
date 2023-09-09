import unittest

from tests_unit import TestUnitTypeRef, TestUnitTypeFunction, TestUnitType, TestUnitTypePool, TestUnit, TestUnitGenerator
from tests_group import TestGroupUnit, TestGroupUnitGenerator, TestGroup


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeRef))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeFunction))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitType))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypePool))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitGenerator))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnit))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnitGenerator))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroup))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
