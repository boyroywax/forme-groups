from dataclasses import dataclass, field, fields
from typing import Any, Dict, List, Optional

from ..type import Type_ as BaseType
from ..type._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class BaseUnit(SuperUnit):
    """
    This is the base class for all units.
    All units are dataclasses.
    All units are initialized with a 'value' and a 'base_type'.
    """

    _base_type: Optional[BaseType] = field(default_factory=BaseType)

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseUnit class.

        Args:
            *args: The arguments to initialize the BaseUnit class.
                The first argument is the 'value'.
                The second argument is the 'base_type'.
            **kwargs: The keyword arguments to initialize the BaseUnit class.
                The 'value' can be provided as a keyword argument.
                The 'base_type' can be provided as a keyword argument.
        """
        # Initialize the 'SuperUnit' class.
        SuperUnit.__init__(self, *args, **kwargs)

        # Post initialize the 'BaseUnit' class.
        self.__post__init__(*args, **kwargs)

    def __post__init__(self, *args, **kwargs):
        """
        Post Initializes the BaseUnit class.
        * Receives 'args' and 'kwargs'.
        """
        self.base_type: Optional[BaseType] = None

        # Check if the 'base_type' is provided as an argument.
        if (
            len(args) > 0 and
            args[1] is not None and
            isinstance(args[1], BaseType) and
            'base_type' not in kwargs
            # self.base_type is None
        ):
            # print(f"Post Init - args - {args}")
            self.base_type = args[1]

        # Check if the 'base_type' is provided as a keyword argument.
        elif (
            'base_type' in kwargs and
            isinstance(kwargs['base_type'], BaseType)
            # self.base_type is None
        ):
            self.base_type = kwargs["base_type"]

        # else the 'base_type' is not provided as an arg or kwarg.
        else:
            self.base_type = BaseType()

    @property
    def base_type(self) -> Optional[BaseType]:
        """
        The base type of the base object.
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base: BaseType) -> None:
        """
        Sets the base type of the base object.
        """
        self._base_type = base

    @base_type.getter
    def base_type(self) -> BaseType:
        """
        Gets the base type of the base object.
        """
        return self._base_type

    @property
    def id_(self) -> BaseType:
        """
        The id of the base object.
        """
        return self._base_type.id_

    @id_.setter
    def id_(self, id: Any) -> None:
        """
        Sets the id of the base object.
        """
        self._base_type.id.value = id

    @id_.getter
    def id_(self) -> BaseType:
        """
        Gets the id of the base object.
        """
        return self._base_type.id_.value

    @property
    def alias(self) -> Any:
        """
        The alias of the group object.
        """
        return self._base_type.alias.value
        # return fields(BaseType)[1].default_factory(BaseType).value

    @property
    def super_(self) -> Any:
        """
        The super of the group object.
        """
        return self._base_type.super_.value

    @property
    def prefix(self) -> Any:
        """
        The prefix of the group object.
        """
        return self._base_type.prefix.value

    @property
    def suffix(self) -> Any:
        """
        The suffix of the group object.
        """
        return self._base_type.suffix.value

    @property
    def separator(self) -> Any:
        """
        The separator of the group object.
        """
        return self._base_type.separator.value

    @property
    def function_(self) -> Any:
        """
        The function of the group object.
        """
        # return fields(BaseType)[6].default_factory(BaseType).value
        return self._base_type.function_.value
