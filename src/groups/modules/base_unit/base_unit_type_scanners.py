from typing import Optional


class TypeScanner:
    """
    A class that scans a string to see if it contains a BaseUnitType.
    """

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
