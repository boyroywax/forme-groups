from dataclasses import dataclass, field
from typing import List

from .base import BaseUnit
from .nonce import Nonce
from .owner import Owner
from .credential import Credential
from .data_entry import Data_Entry

from ..type import Type as BaseType
from ..type.defaults import Defaults as BaseDefaults
from ..type.checks import Checks as BaseChecks

_OPTION_DEFAULT = ["defaults", "default", "DEFAULTS", "DEFAULT", "Defaults", "Default"]
_OPTION_CUSTOM = ["custom", "CUSTOM", "Custom", "defined", "DEFINED", "Defined", "DEFINE", "define", "Define"]
_OPTION_ALL = ["all", "ALL", "All", "ALL_TYPES", "all_types", "All_Types", "All_Types", "ALL_TYPES", "all_types", "All_Types"]


@dataclass
class Units():
    """
    Manages the units of the base group object.
    """

    _base_types: List[BaseType] = field(init=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes the 'Units' object.
        """
        if (
            args is not None and
            len(args) == 0 and
            kwargs is not None and
            len(kwargs) == 0
        ):
            self._base_types = list()

        if (
            args is not None and
            len(args) == 0 and
            kwargs is not None and
            'types' in kwargs and
            kwargs['types'] is not None and
            isinstance(kwargs['types'], List[BaseType])
        ):
            self.type.set(kwargs['types'])

        if (
            args is not None and
            len(args) > 0 and
            kwargs is not None and
            'types' not in kwargs and
            isinstance(args[0], List[BaseType])
        ):
            self.type.set(args[0])

        if (
            args is not None and
            len(args) > 0 and
            kwargs is not None and
            'types' in kwargs
        ):
            raise ValueError("Cannot provide 'types' as a keyword argument and as a positional argument.")

        if (
            args is not None and
            len(args) > 0 and
            kwargs is not None and
            len(kwargs) == 0 and
            isinstance(args[0], str)
        ):
            self.__post_init__(*args, **kwargs)

    def __post_init__(self, *args, **kwargs):
        """
        Post initializes the 'Units' object.
        """
        if (
            args is not None and
            args[0] is not None and
            isinstance(args[0], str) and
            args[0] in _OPTION_DEFAULT or
            args[0] in _OPTION_CUSTOM or
            args[0] in _OPTION_ALL

        ):
            self._load(args[0])

        if (
            (
                args is not None and
                args[0] is not None and
                isinstance(args[0], str) and
                args[0] in _OPTION_DEFAULT or
                args[0] in _OPTION_CUSTOM or
                args[0] in _OPTION_ALL
            ) and (
                args[1] is not None and
                isinstance(args[1], str) and
                args[1] in _OPTION_CUSTOM
            )
        ):
            self._load(args[1])

    def _load(self, option: str) -> None:
        """
        Loads the defaults for the units object.
        """
        if option in _OPTION_DEFAULT:
            self._load_defaults()
        elif option in _OPTION_CUSTOM:
            self._load_custom()
        elif option in _OPTION_ALL:
            self._load_defaults()
            self._load_custom()

        print(self._base_types)

    def _add_type(self, base_type: BaseType) -> None:
        """
        Adds a type to the units object.
        """
        if base_type not in self._base_types:
            self._base_types.append(base_type)

    def _add_types(self, base_types: List[BaseType]) -> None:
        """
        Adds types to the units object.
        """
        for base_type in base_types:
            self._add_type(base_type)

    def _remove_type(self, base_type: BaseType) -> None:
        """
        Removes a type from the units object.
        """
        if base_type in self._base_types:
            self._base_types.remove(base_type)

    def _clear_types(self) -> None:
        """
        Clears the types from the units object.
        """
        self._base_types.clear()

    def _load_defaults(self) -> None:
        """
        Loads the defaults for the units object.
        """
        defaults = BaseDefaults()
        defaults.generate()
        loaded_types = defaults.types
        print(loaded_types)
        for type_ in loaded_types:
            if self._check_system_type(type_):
                self._add_type(type_)
            else:
                print(f"Default type '{type_.function.value}' is not supported.")

    def _load_custom(self) -> None:
        """
        Loads the custom types for the units object.
        """
        pass

    def _check_system_type(self, type_: BaseType) -> bool:
        """
        Checks system types for supported types.
        """
        if type_.super.value == "RESERVED":
            return BaseChecks.check_supported_system_type(type_.function.value)
        else:
            raise ValueError("The type provided is not a system type.")

    @property
    def types(self) -> List[BaseType]:
        """
        The types of the units object.
        """
        return self._base_types

    @types.setter
    def types(self, types: List[BaseType]) -> None:
        """
        The types setter of the units object.
        """
        self._base_types = types

    @types.getter
    def types(self) -> List[BaseType]:
        """
        The types getter of the units object.
        """
        return self._base_types


__all__ = [
    BaseUnit,
    Nonce,
    Owner,
    Credential,
    Data_Entry,
]
