import unittest

# from .tests_base_config import TestConfig
# from .tests_base_value import Test_Value_
# from .tests_base_config_1 import TestType_
from .tests_system_defaults import TestSystemDefaults
from .tests_system_check import TestSystemCheck
from .tests_system import TestSystem


def main():
    # Create the test suite
    test_suite = unittest.TestSuite()

    # Create the test loader
    test_loader = unittest.TestLoader()

    # Add the test cases to the test suite
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestConfig))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(Test_Value_))
    # test_suite.addTests(test_loader.loadTestsFromTestCase(TestType_))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestSystemDefaults))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestSystemCheck))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestSystem))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(test_suite)


if __name__ == '__main__':
    main()
