import unittest

from tests_merkle_tree import TestMerkleTree
from tests_unit_type import TestUnitTypeRef, TestUnitTypeFunction, TestUnitType
from tests_pool import TestPool
from tests_unit_type_pool import TestUnitTypePool
from tests_unit_creator import TestUnitCreator
from tests_unit_pool import TestUnitPool
from tests_unit import TestUnit


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestMerkleTree))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeRef))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeFunction))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitType))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestPool))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypePool))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitCreator))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitPool))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))


    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
