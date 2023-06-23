import json
from typing import Optional, List


class Value_():
    """
    Holds the value of a unit.
    """

    _value: Optional[str] = None

    def __init__(self, value: Optional[str] = None) -> None:
        """
        Initializes the Value class.
        """
        if value is not None:
            self.set_value(value)
        else:
            self.set_value("")

    def set_value(self, value: str) -> None:
        """
        Sets the value.
        """
        self._value = value

    def get_value(self) -> str:
        """
        Returns the value.
        """
        return self._value
    
    def to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
    def from_json_string(self, json_string: str) -> None:
        """
        Returns the object in a JSON string format.
        """
        json_dict = json.loads(json_string)
        if "_value" in json_dict:
            self._value = json_dict["_value"]
        else:
            raise KeyError("The key '_value' was not found in the JSON string.")
    
    def __str__(self) -> str:
        """
        Returns the value.
        """
        return self.get_value()
    
    def __repr__(self) -> str:
        """
        Returns the value.
        """
        return self.get_value()
    
    def __eq__(self, other: object) -> bool:
        """
        Determines if the value is equal to another value.
        """
        if not isinstance(other, Value_):
            return NotImplemented
        return self.get_value() == other.get_value()
    
    def __ne__(self, other: object) -> bool:
        """
        Determines if the value is not equal to another value.
        """
        if not isinstance(other, Value_):
            return NotImplemented
        return self.get_value() != other.get_value()
