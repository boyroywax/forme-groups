import uuid

from dataclasses import dataclass, InitVar
from typing import Any, Dict, Optional

from .checks import Checks


@dataclass(
    slots=True,
)
class Unit():
    """
    The base class for all units.
    * Units can be initialized as a 'value'.
    * Units can be initialized as a 'dictionary'.
    * Units can be initialized as NoneType.
    * Units can be initialized as a random value.

    Example (from NoneType):
    ```Python
    unit = Unit()
    unit = Unit(None)
    ```

    Example (from value):
    ```Python
    unit = Unit("test")
    ```

    Example (from dictionary):
    ```Python
    unit = Unit({
        "value": "test"
    })

    Note: The 'value' is stored as a slot.
    A dataclass 'slot' is used to store the 'value' in memory.

    The advantages of a slot are:
    * Faster attribute access.
    * Less memory usage.
    """

    value: Any = None
    _random_value: InitVar[bool] = None

    def __init__(
        self,
        value: Optional[Any] = None,
        _random_value: bool = False
    ) -> None:
        """
        Initializes the Unit class.
        """

        if value is not None:
            if Checks.check_value_for_empty(value):
                raise TypeError(
                    "The value is empty."
                    "The value must be a non-empty 'string', 'dictionary', 'tuple', or 'list'."
                    "The value cannot be 'None'."
                    "To create a NoneType unit, use Unit()."
                )
            self.set_value(value)
        else:
            self.value = None
        self.__post_init__(_random_value)

    def __post_init__(self, _random_value: bool) -> None:
        """
        Post Initializes the Unit class.
        * If '_random_value' is True, a random value is generated.
        * If '_random_value' is True, and the value is None, a random value is set.
        * You cannot overwrite a value with a random value.
        * You can only set a random value if the value is None.
        """
        if _random_value and self.value is None:
            self.set_value()

    def get_type(self) -> str:
        """
        Returns the type name of the unit of the value.
        """
        return type(self).__name__

    def set_value(self, value: Optional[Any] = None) -> None:
        """
        Set the value of the unit object.
        * If the value is None, a random value is generated.
        """
        if value is not None:
            self.value = value
        else:
            self.value = uuid.uuid4().hex

    def from_dict(unit_dict: Dict) -> 'Unit':
        """
        Sets the unit from a dictionary.
        * Empty and None values are ignored.
        * Inlcuding empty strings, empty dictionaries, and empty lists.

        Example:
        ```Python
        {
            "value": "test"
        }
        ```
        The next example will raise a TypeError:
        ```Python
        {
            "value": None
        }
        ```

        """
        print(unit_dict)

        if "value" in unit_dict:
            if Checks.check_value_for_empty(unit_dict["value"]):
                raise TypeError(
                    "The dictionary's value is empty."
                    "The dictionary's value must be a non-empty 'string', 'dictionary', 'tuple', or 'list'."
                    "The dictionary's value cannot be 'None'."
                    "To create a NoneType unit, use Unit()."
                )
            else:
                return Unit(unit_dict["value"])
        else:
            raise TypeError("The dictionary is missing the required key 'value'.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the unit as a dictionary.
        """
        return {
            "value": self.value
        }
