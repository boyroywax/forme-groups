from dataclasses import dataclass
from typing import Any, Dict, List, Optional


from .type import Type as TypeClass
from .defaults import Defaults


@dataclass
class Supported():
    """
    Manages the supported of the group object.
    """
    _supported: Optional[List[TypeClass]] = None

    def __post_init__(self) -> None:
        """
        Post initialisation hook.
        """
        self._supported = []

    def get_supported(self) -> List[TypeClass]:
        """
        Gets the supported.
        """
        return self._supported
    
    def get(self, id: str) -> Optional[Any]:
        """
        Get the type by ID.
        """
        for type in self._supported:
            if type.get_id() == id:
                return type
        
        return None
    
    def get_by_alias(self, alias: str) -> Optional[Any]:
        """
        Get the type by alias.
        """
        for type in self._supported:
            if alias in type.get_aliases():
                return type
        
        return None

    def check_type_system_support(self) -> None:
        """
        Checks if the system supports the type system.
        """
        for system_type in self.DEFAULT_TYPES.keys():
            match system_type:
                case "bytes":
                    if isinstance(b"string", bytes):
                        self.SUPPORTED_TYPES.append(system_type)
                case "string":
                    if isinstance("string", str):
                        self.SUPPORTED_TYPES.append(system_type)
                case "integer":
                    if isinstance(1, int):
                        self.SUPPORTED_TYPES.append(system_type)
                case "float":
                    if isinstance(1.0, float):
                        self.SUPPORTED_TYPES.append(system_type)
                case "boolean":
                    if isinstance(True, bool):
                        self.SUPPORTED_TYPES.append(system_type)
                case "list":
                    if isinstance([], list):
                        self.SUPPORTED_TYPES.append(system_type)
                case "tuple":
                    if isinstance((), tuple):
                        self.SUPPORTED_TYPES.append(system_type)
                case "dictionary":
                    if isinstance({}, dict):
                        self.SUPPORTED_TYPES.append(system_type)
                case "set":
                    if isinstance({1, 2, 3}, set):
                        self.SUPPORTED_TYPES.append(system_type)
                case "frozenset":
                    if isinstance(frozenset({1, 2, 3}), frozenset):
                        self.SUPPORTED_TYPES.append(system_type)
                case "complex":
                    if isinstance(1j, complex):
                        self.SUPPORTED_TYPES.append(system_type)
                case "range":
                    if isinstance(range(1), range):
                        self.SUPPORTED_TYPES.append(system_type)
                case "memoryview":
                    if isinstance(memoryview(b"string"), memoryview):
                        self.SUPPORTED_TYPES.append(system_type)
                case "None":
                    if isinstance(None, type(None)):
                        self.SUPPORTED_TYPES.append(system_type)
                case _:
                    raise ValueError(f"Invalid system type value {system_type} provided.")