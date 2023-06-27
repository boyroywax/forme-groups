from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .type import Type as TypeClass


@dataclass
class Defaults():
    """
    Manages the defaults of the group object.
    """
    _defaults: Optional[List[TypeClass]] = None

    def __post_init__(self) -> None:
        """
        Post initialisation hook.
        """
        self.set_defaults()

    def get_defaults(self) -> List[TypeClass]:
        """
        Gets the defaults.
        """
        return self._defaults
    
    def get(self, id: str) -> Optional[Any]:
        """
        Get the type by ID.
        """
        for type in self._defaults:
            if type.get_id() == id:
                return type
        
        return None
    
    def get_by_alias(self, alias: str) -> Optional[Any]:
        """
        Get the type by alias.
        """
        for type in self._defaults:
            if alias in type.get_aliases():
                return type
        
        return None

    
    def set_defaults(self) -> None:
        """
        Sets the defaults.
        """
        self._defaults = [
            TypeClass(
                id="string",
                aliases=["string", "str"],
                super_type="RESERVED",
                prefix="",
                suffix="",
                separator="",
                system_function=str
            ),
            TypeClass(
                id="integer",
                aliases=["integer", "int"],
                super_type="RESERVED",
                prefix="",
                suffix="",
                separator="",
                system_function=int
            ),
            TypeClass(
                id="float",
                aliases=["float", "flt"],
                super_type="RESERVED",
                prefix="",
                suffix="",
                separator="",
                system_function=float
            ),
            TypeClass(
                id="boolean",
                aliases=["boolean", "bool"],
                super_type="RESERVED",
                prefix="",
                suffix="",
                separator="",
                system_function=bool
            ),
            TypeClass(
                id="list",
                aliases=["list", "lst"],
                super_type="RESERVED",
                prefix="[",
                suffix="]",
                separator=",",
                system_function=list
            ),
            TypeClass(
                id="dictionary",
                aliases=["dictionary", "dict"],
                super_type="RESERVED",
                prefix="{",
                suffix="}",
                separator=",",
                system_function=dict
            ),
            TypeClass(
                id="tuple",
                aliases=["tuple", "tpl"],
                super_type="RESERVED",
                prefix="(",
                suffix=")",
                separator=",",
                system_function=tuple
            ),
            TypeClass(
                id="bytes",
                aliases=["bytes", "bts"],
                super_type="RESERVED",
                prefix="b'",
                suffix="'",
                separator="",
                system_function=bytes
            )
        ]
