from typing import LiteralString, Optional

import json


class Value():
    """
    BaseValue class.
    """
    _value: Optional[LiteralString] = "Universal serializable object base value"

    def __init__(self, value: str) -> None:
        """
        Constructor for the BaseValue class.
        """
        self._value = value

    def get_value(self) -> str:
        """
        Returns the value.
        """
        return self._value

    def set_value(self, value: str) -> None:
        """
        Sets the value.
        """
        self._value = value

    def to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
