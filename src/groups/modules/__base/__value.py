import json
from typing import Optional, Any


class Value_():
    """
    Holds the value of a unit.
    """

    _value: str = None

    def __init__(self, value: Optional[Any] = None) -> None:
        """
        Initializes the Value class.
        """
        if value is not None:
            self.set_value(value)
        else:
            self.set_value("")

    def validate_system_type(self, value: Any) -> bool:
        """
        Validates the system type.
        """
        match _VALUE_SYSTEM_TYPE:
            case "string":
                if isinstance(value, str):
                    return True
                else:
                    return False
            case "int":
                if isinstance(value, int):
                    return True
                else:
                    return False

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

    def value_to_dict(self) -> dict:
        """
        Returns the object in a dictionary format.
        """
        return {
            "_value": self._value
        }

    def value_to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self.value_to_dict(), default=lambda o: o.__dict__, sort_keys=True)

    def value_from_json_string(self, json_string: str) -> None:
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
