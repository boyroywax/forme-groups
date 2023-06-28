from typing import Any, List, Optional, Dict


class Checks():
    """
    Checks the system and data values for any errors.
    """

    @staticmethod
    def check_value_for_empty(value: Any) -> bool:
        """
        Checks if the value is empty or contains an empty construct.
        """
        if value is None:
            return True

        if (
            value is None or
            value == "" or
            value == "{}" or
            value == "[]" or
            value == "()" or
            value == "''" or
            value == '""' or
            value == "``" or
            value == "'''" or
            value == '"""' or
            str(value).lower() is None or
            str(value).lower() == "none" or
            str(value).lower() == "null" or
            str(value).lower() == "{}" or
            str(value).lower() == "[]" or
            str(value).lower() == "()" or
            str(value).lower() == str("") or
            str(value).lower() == str('') or
            str(value).lower() == str("''") or
            str(value).lower() == '""' or
            str(value).lower() == "``" or
            str(value).lower() == "'''"
        ):
            return True
        else:
            return False
