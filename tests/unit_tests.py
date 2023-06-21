import unittest

from unit_tests_nonce_types import TestNonceTypes
from unit_tests_nonce_unit import TestNonceUnit
from unit_tests_nonce import TestNonce
from unit_tests_integer_nonce import TestIntegerNonce
from unit_tests_decentralized_id import TestDecentralizedId
from unit_tests_default_schema import TestDefaultSchema
from unit_tests_generic_data import TestGenericData
from unit_tests_universal_object import TestUniversalObject
from unit_tests_credentials import TestCredentials
from unit_tests_owner import TestOwner
from unit_tests_unit_type import TestUnitType


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestNonceTypes))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestNonceUnit))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestNonce))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestIntegerNonce))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDecentralizedId))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDefaultSchema))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestGenericData))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUniversalObject))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestCredentials))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestOwner))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnitType))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
