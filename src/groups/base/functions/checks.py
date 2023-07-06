import uuid
from typing import Any, Dict, List, Optional


class Checks:
    """
    The Checks Helper class.

    NoneType and Empty Helper methods:
    * get_none_list() -> list
    * check_none() -> bool

    Random Value Helper methods:
    * random_value() -> Any

    """

    @staticmethod
    def get_none_list() -> list:
        """
        Get a list of values representing a NoneType.

        Returns:
            list: A list of values representing a NoneType.

        Example:
        ```Python
        SuperUnit.get_none_list()  # [None, "None", "", "null", "NULL", "none"]
        ```
        """
        return [
            None,
            "None",
            "none",
            "NONE",
            "",
            " ",
            "null",
            "Null",
            "NULL",
            "nil",
            "Nil",
            "NIL",
            str(""),
            str(" "),
            str("''"),
            str('""'),
            str(' ')
        ]

    @staticmethod
    def check_none(value: Any) -> bool:
        """
        Checks if the value is None or equal to any of the values on from the get_none_list() method.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is None or equal to any of the values on from the get_none_list() method.
        """
        return value is None or value in SuperUnit.get_none_list()

    @staticmethod
    def random_value(type_: Optional[Any] = None) -> Any:
        """
        Create a random value based on the uuid4() function.

        Returns:
            str: A random value.
        """
        if type_ is int or type_ is float or type_ == "int":
            return int(uuid.uuid4().int)
        if type_ is bool or type_ == "bool":
            return bool(uuid.uuid4().int % 2)
        if type_ is str or type_ is None or type_ == "str":
            return str(uuid.uuid4().hex)

        return uuid.uuid4()