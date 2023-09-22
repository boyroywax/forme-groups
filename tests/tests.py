import unittest

from tests_unit_type import TestUnitTypeRef, TestUnitTypeFunction, TestUnitType
# from tests_group import TestGroupUnit, TestGroup, TestSchema
from tests_pool import TestPool
# TestGroupUnitGenerator, TestGroup


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeRef))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeFunction))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitType))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypePool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitGenerator))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestPool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnitGenerator))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroup))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestSchema))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
