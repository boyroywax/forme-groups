import unittest

from .tests_checks import TestChecks
from .tests_unit import TestUnit
from .tests_id import TestId
from .tests_type import TestType
from .tests_defaults import TestDefaults
from .tests_base_unit import TestBaseUnit
from .tests_units import TestUnits




def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestChecks))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnit))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestId))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestType))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDefaults))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestBaseUnit))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestUnits))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
