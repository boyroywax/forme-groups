from attrs import define, field
import json
from typing import Any, Optional, Tuple

__DEFAULT_SYSTEM_TYPES_PATH__ = "src/groups"


@define(frozen=True, slots=True)
class UnitTypeRef:
    """A reference to a UnitType.

    Attributes:
        alias (str): The alias of the UnitType.
    """
    alias: str = field(default=None)

    def __str__(self) -> str:
        return self.alias


@define(frozen=True, slots=True)
class UnitTypeFunction:
    """A function that can be used to generate a Unit.

    Attributes:
        object (callable): The function that will be called to generate a Unit.
        args (tuple): The arguments that will be passed to the function.
    """
    object: callable = field(factory=callable)
    args: tuple = field(factory=tuple)

    def call(self, input: Any = None) -> object:
        """Call the function with the given input.

        Args:
            input (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        if input is not None and len(self.args) > 0:
            new_args = list(self.args)
            new_args.insert(0, input)
            return self.object(*new_args)
        elif input is not None:
            return self.object(input)
        else:
            return self.object(*self.args)


@define(frozen=True, slots=True)
class UnitType:
    """A type of Unit.

    Attributes:
        aliases (list[UnitTypeRef]): The aliases of the UnitType.
        super_type (list[UnitTypeRef]): The super types of the UnitType.
        prefix (str): The prefix of the UnitType. Defaults to None.
        suffix (str): The suffix of the UnitType. Defaults to None.
        separator (str): The separator of the UnitType. Defaults to None.
        sys_function (UnitTypeFunction): The system function of the UnitType. Defaults to None.
    """
    aliases: Tuple[UnitTypeRef] = field(factory=tuple)
    super_type: Tuple[UnitTypeRef] = field(factory=tuple)
    prefix: Optional[str] = field(default=None)
    suffix: Optional[str] = field(default=None)
    separator: Optional[str] = field(default=None)
    sys_function: Optional[UnitTypeFunction] = field(default=None)