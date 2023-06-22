import unittest

from groups.modules.base_unit_type_scanners import TypeScanner


class TestBaseUnitScanners(unittest.TestCase):
    # def test_is_integer():
    #     assert TypeScanner.is_integer("12345") is True
    #     assert TypeScanner.is_integer("12.345") is False
    #     assert TypeScanner.is_integer("12345a") is False

    # def test_is_float():
    #     assert TypeScanner.is_float("12.345") is True
    #     assert TypeScanner.is_float("12345") is False
    #     assert TypeScanner.is_float("12.3.4.5") is False

    # def test_is_boolean():
    #     assert TypeScanner.is_boolean("true") is True
    #     assert TypeScanner.is_boolean("false") is True
    #     assert TypeScanner.is_boolean("True") is not True
    #     assert TypeScanner.is_boolean("yes") is not True

    # def test_is_list():
    #     assert TypeScanner.is_list("[1, 2, 3]") is True
    #     assert TypeScanner.is_list("[1, 2, 3") is False
    #     assert TypeScanner.is_list("1, 2, 3]") is False

    # def test_is_tuple():
    #     assert TypeScanner.is_tuple("(1, 2, 3)") is True
    #     assert TypeScanner.is_tuple("(1, 2, 3") is False
    #     assert TypeScanner.is_tuple("1, 2, 3)") is False

    # def test_is_dictionary():
    #     assert TypeScanner.is_dictionary("{}") is True
    #     assert TypeScanner.is_dictionary("{1: 'one', 2: 'two'}") is True
    #     assert TypeScanner.is_dictionary("{1: 'one', 2: 'two'") is False
    #     assert TypeScanner.is_dictionary("[1, 2, 3]") is False

    # def test_is_custom():
    #     assert TypeScanner.is_custom("my_custom_type", prefix="my_", suffix="_type") is True
    #     assert TypeScanner.is_custom("my_custom_type", prefix="your_", suffix="_type") is not True
    #     assert TypeScanner.is_custom("my_custom_type", prefix="my_", suffix="_class") is not True
    #     assert TypeScanner.is_custom("my_custom_type", prefix="my_", suffix="_type_") is not True
