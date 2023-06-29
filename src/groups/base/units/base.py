from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ..type import Type as BaseType
from ..type._unit import Unit_ as SuperUnit


@dataclass
class BaseUnit(SuperUnit):
    """
    This is the base class for all units.
    All units are dataclasses.
    All units are initialized with a 'value' and a 'base_type'.
    """
    _base_type: Optional[BaseType] = None

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseUnit class.
        * Receives 'args' and 'kwargs'.

        :param args: The arguments to initialize the BaseUnit class.
        :type args: Tuple[Any]
        :info: The first argument is the 'value'. The second argument is the 'base_type'.

        :param kwargs: The keyword arguments to initialize the BaseUnit class.
        :type kwargs: Dict[str, Any]
        :info: The 'value' can be provided as a keyword argument.
        :info: The 'base_type' can be provided as a keyword argument.

        """
        super().__init__(*args, **kwargs)
        self.__post__init__(*args, **kwargs)

    def __post__init__(self, *args, **kwargs):

        if args[1] is not None:
            if isinstance(args[1], BaseType):
                self._base_type = args[1]
        if "base_type" in kwargs:
            self._base_type: Optional[BaseType] = None

    @property
    def base(self) -> BaseType:
        """
        The base of the group object.
        """
        return self._base_type

    @base.setter
    def base(self, base: BaseType) -> None:
        self._base_type = base

    @property
    def id(self) -> str:
        """
        The id of the group object.
        """
        return self._base_type.id.value

    @property
    def alias(self) -> str:
        """
        The alias of the group object.
        """
        return self._base_type.alias.value

    @property
    def super(self) -> str:
        """
        The super of the group object.
        """
        return self._base_type.super.value

    @property
    def prefix(self) -> str:
        """
        The prefix of the group object.
        """
        return self._base_type.prefix.value

    @property
    def suffix(self) -> str:
        """
        The suffix of the group object.
        """
        return self._base_type.suffix.value

    @property
    def separator(self) -> str:
        """
        The separator of the group object.
        """
        return self._base_type.separator.value

    @property
    def function(self) -> str:
        """
        The function of the group object.
        """
        return self._base_type.function.value
