from typing import Optional, List

from groups.modules.base.type import BaseUnitType


class TypeGenerator():
    """
    A class that scans a string to see if it contains a BaseUnitType.
    """

    _prefix: Optional[str] = None
    _suffix: Optional[str] = None
    _separator: Optional[str] = None
    _custom_function: Optional[List] = None

    def __init__(
            self,
            parent: Optional[BaseUnitType] = None,
            prefix: Optional[str] = None,
            suffix: Optional[str] = None,
            separator: Optional[str] = None,
            custom_function: Optional[List] = None
    ) -> None:
        """
        Initializes the Generator class.
        """
        self._prefix = prefix
        self._suffix = suffix
        self._separator = separator
        self._custom_function = custom_function

    def is_string(self, string: str) -> bool:
        """
        Returns True if the given string contains only strings, False otherwise.
        """
        try:
            str(string)
            return True
        except ValueError:
            return False

    def is_integer(self, string: str) -> bool:
        """
        Returns True if the given string contains only integers, False otherwise.
        """
        try:
            int(string)
            return True
        except ValueError:
            return False

    def is_float(self, string: str) -> bool:
        """
        Returns True if the given string contains only floats, False otherwise.
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def is_boolean(self, string: str) -> bool:
        """
        Returns True if the given string contains only booleans, False otherwise.
        """
        return string.lower() in ('true', 'false')

    def is_list(self, string: str) -> bool:
        """
        Returns True if the given string contains only lists, False otherwise.
        """
        return string.startswith('[') and string.endswith(']')

    def is_tuple(self, string: str) -> bool:
        """
        Returns True if the given string contains only tuples, False otherwise.
        """
        return string.startswith('(') and string.endswith(')')

    def is_dictionary(self, string: str) -> bool:
        """
        Returns True if the given string contains only dictionaries, False otherwise.
        """
        return string.startswith('{') and string.endswith('}')

    def is_custom(self, string: str, prefix: Optional[str] = None, suffix: Optional[str] = None) -> bool:
        """
        Returns True if the given string contains a custom type with the given prefix and suffix, False otherwise.
        """
        if prefix is not None and not string.startswith(prefix):
            return False
        if suffix is not None and not string.endswith(suffix):
            return False
        return True
    
    def get_lambda(self) -> function:
        """
        Returns True if the given string contains a lambda, False otherwise.
        """
        return lambda x: x
