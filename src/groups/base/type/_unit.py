import uuid

from dataclasses import dataclass, InitVar
from typing import Any, Dict, Optional

from .checks import Checks


@dataclass(
    slots=True,
)
class Unit_():
    """
    The super base class for all units.
    * Units can be initialized as a 'value'.
    * Units can be initialized as NoneType.
    * Units can be initialized as a random value.
    * Units can be initialized from a 'dictionary'.

    Example (from NoneType):
    ```Python
    unit = Unit_()
    unit = Unit_(None)
    ```

    Example (from value):
    ```Python
    unit = Unit_("test")
    ```

    Example (from dictionary):
    ```Python
    unit = Unit_({
        "value": "test"
    })
    ```
    
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
        *args,
        **kwargs,
        # value: Optional[Any] = None,
        # _random_value: bool = False
    ) -> None:
        """
        Initializes the Super Unit_ class.
        * If 'value' is not None, the value is set.
        * If 'value' is None, the value is set to None.
        * If 'random' is True, and the value is None, a random value is set.
        * If 'random' is True, and the value is not None, a random value is not set.

        Example (from kwargs):
        ```Python
        unit = Unit_(value="test")
        unit = Unit_(random=True)
        ```

        Example (from args):
        ```Python
        unit = Unit_("test")
        """
        print("Unit_.__init__", args, kwargs)

        # self.value = None

        if len(args) > 0 and 'value' in kwargs:
            raise ValueError("Cannot provide both 'value' and 'kwargs['value']' to Unit_")

        if len(args) > 0 and 'random' in kwargs:
            raise ValueError("Cannot provide both 'value' and 'args' to Unit_")

        if len(args) == 0 and "value" in kwargs and "random" in kwargs:
            raise ValueError("Cannot provide both 'value' and 'random' to Unit_")

        if len(args) == 0 and "value" not in kwargs and "random" not in kwargs:
            self.value = None
        elif len(args) == 1 and "value" not in kwargs and "random" not in kwargs:
            self.set_value(args[0])
        elif len(args) == 0 and "value" not in kwargs and "random" in kwargs:
            self.set_random_value()
        elif len(args) == 0 and "value" in kwargs and "random" not in kwargs:
            self.set_value(kwargs["value"])

    # def __post_init__(self, _random_value: bool) -> None:
    #     """
    #     Post Initializes the Unit_ class.
    #     * If '_random_value' is True, a random value is generated.
    #     * If '_random_value' is True, and the value is None, a random value is set.
    #     * You cannot overwrite a value with a random value.
    #     * You can only set a random value if the value is None.
    #     """
    #     if _random_value and self.value is None:
    #         self.set_random_value()

    def get_type(self) -> str:
        """
        Returns the type name of the unit of the value.
        """
        return type(self).__name__

    def set_value(self, value: Optional[Any] = None) -> None:
        """
        Set the value of the unit object.
        """
        if value is not None:
            if Checks.check_value_for_empty(value):
                raise TypeError(
                    "The value is empty."
                    "The value must be a non-empty 'string', 'dictionary', 'tuple', or 'list'."
                    "The value cannot be 'None'."
                    "To create a NoneType unit, use Unit_()."
                )
            self.value = value

    def set_random_value(self) -> None:
        """
        Sets a random value.
        """
        self.value = uuid.uuid4().hex

    def from_dict(unit_dict: Dict) -> 'Unit_':
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
        if "value" in unit_dict:
            if Checks.check_value_for_empty(unit_dict["value"]):
                raise TypeError(
                    "The dictionary's value is empty."
                    "The dictionary's value must be a non-empty 'string', 'dictionary', 'tuple', or 'list'."
                    "The dictionary's value cannot be 'None'."
                    "To create a NoneType unit, use Unit_()."
                )
            else:
                return Unit_(unit_dict["value"])
        else:
            raise TypeError("The dictionary is missing the required key 'value'.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the unit as a dictionary.
        """
        return {
            "value": self.value
        }
