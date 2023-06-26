from typing import List, Optional, Dict, Any

from . import System


class SystemCheck():
    """
    Checks the system for any errors.
    """

    output: Dict[str, Any] = {}

    def __init__(
        self,
        system: System
    ) -> None:
        """
        Initializes the SystemCheck class.
        """
        self._system = system

    def check_system(
        self,
        process: List[str]
    ) -> List[str]:
        """
        Checks the system.
        """
        output: Dict[str] = {}
        if process is not None and "system_types" in process:
            self.output['supported_types'] = self.check_supported_system_types()
        else:
            self.output['supported_types'] = self.check_supported_system_types()

    def check_supported_system_types(self) -> List[str]:
        """
        Checks if the system types are supported.
        """
        supported_system_types: List[str] = []
        for system_type in self._system.defaults.system_types:
            match system_type:
                case "bytes":
                    if isinstance(b"string", bytes):
                        supported_system_types.append(system_type)
                case "str":
                    if isinstance("string", str):
                        supported_system_types.append(system_type)
                case "int":
                    if isinstance(1, int):
                        supported_system_types.append(system_type)
                case "float":
                    if isinstance(1.0, float):
                        supported_system_types.append(system_type)
                case "bool":
                    if isinstance(True, bool):
                        supported_system_types.append(system_type)
                case "list":
                    if isinstance([], list):
                        supported_system_types.append(system_type)
                case "tuple":
                    if isinstance((), tuple):
                        supported_system_types.append(system_type)
                case "dict":
                    if isinstance({}, dict):
                        supported_system_types.append(system_type)
                case "set":
                    if isinstance({1, 2, 3}, set):
                        supported_system_types.append(system_type)
                case "frozenset":
                    if isinstance(frozenset({1, 2, 3}), frozenset):
                        supported_system_types.append(system_type)
                case "complex":
                    if isinstance(1j, complex):
                        supported_system_types.append(system_type)
                case "range":
                    if isinstance(range(1), range):
                        supported_system_types.append(system_type)
                case "memoryview":
                    if isinstance(memoryview(b"string"), memoryview):
                        supported_system_types.append(system_type)
                case "None":
                    if isinstance(None, type(None)):
                        supported_system_types.append(system_type)
                case _:
                    raise ValueError("Invalid system type value provided.")

        return supported_system_types
