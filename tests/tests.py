import unittest

from tests_merkle_tree import TestMerkleTree
from tests_unit_type import TestReferenceInterface, TestUnitTypeRef, TestUnitTypeFunction, TestUnitType
from tests_pool import TestPool
from tests_unit_type_pool import TestUnitTypePool
from tests_unit_creator import TestUnitCreator
from tests_unit_pool import TestUnitPool
from tests_unit import TestUnit
from tests_nonce import TestNonce
from tests_data_schema import TestDataSchema
from tests_data import TestData
from tests_group_unit_creator import TestGroupUnitCreator
from tests_group_unit_pool import TestGroupUnitPool
from tests_group_unit import TestGroupUnit
from tests_group_subunit import TestGroupSubUnit
from tests_group import TestGroup


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestMerkleTree))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestReferenceInterface))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeRef))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypeFunction))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitType))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestPool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitTypePool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitCreator))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitPool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupSubUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestNonce))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestDataSchema))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestData))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnitCreator))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnitPool))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroupUnit))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestGroup))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
