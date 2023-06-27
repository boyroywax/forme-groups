import json
from typing import List, Optional, Dict, Any

from .type import Type_ as UnitType
from .value import Value_ as UnitValue


class Defaults():
    """
    Default values for system group.
    """
    DEFAULT_SUPER_TYPE = UnitType(
        id=UnitValue('string'),
        alias=UnitValue('str'),
        system_function=str
    )

    DEFAULT_TYPES: Dict[str, UnitType] = {
        'string': DEFAULT_SUPER_TYPE,
        'integer': UnitType(
            id=UnitValue('integer'),
            alias=UnitValue('int'),
            super=DEFAULT_SUPER_TYPE,
            system_function=int
        ),
        'float': UnitType(
            id=UnitValue('float'),
            alias=UnitValue('flt'),
            super=DEFAULT_SUPER_TYPE,
            system_function=float
        ),
        'boolean': UnitType(
            id=UnitValue('boolean'),
            alias=UnitValue('bool'),
            super=DEFAULT_SUPER_TYPE,
            system_function=bool
        ),
        'list': UnitType(
            id=UnitValue('list'),
            alias=UnitValue('lst'),
            super=DEFAULT_SUPER_TYPE,
            prefix=UnitValue('['),
            suffix=UnitValue(']'),
            separator=UnitValue(','),
            system_function=list
        ),
        'dictionary': UnitType(
            id=UnitValue('dictionary'),
            alias=UnitValue('dict'),
            super=DEFAULT_SUPER_TYPE,
            prefix=UnitValue('{'),
            suffix=UnitValue('}'),
            separator=UnitValue(','),
            system_function=dict
        ),
        'tuple': UnitType(
            id=UnitValue('tuple'),
            alias=UnitValue('tup'),
            super=DEFAULT_SUPER_TYPE,
            prefix=UnitValue('('),
            suffix=UnitValue(')'),
            separator=UnitValue(','),
            system_function=tuple
        ),
        # 'set': UnitType(
        #     id=UnitValue('set'),
        #     alias=UnitValue('st'),
        #     super=DEFAULT_SUPER_TYPE,
        #     prefix=UnitValue('set({'),
        #     suffix=UnitValue('}'),
        #     separator=UnitValue(','),
        #     system_function=set
        # ),
        # 'frozenset': UnitType(
        #     id=UnitValue('frozenset'),
        #     alias=UnitValue('fset'),
        #     super=DEFAULT_SUPER_TYPE,
        #     prefix=UnitValue('{'),
        #     suffix=UnitValue('}'),
        #     separator=UnitValue(','),
        #     system_function=frozenset
        # ),
        'bytes': UnitType(
            id=UnitValue('bytes'),
            alias=UnitValue('bts'),
            super=DEFAULT_SUPER_TYPE,
            prefix=UnitValue('b\''),
            suffix=UnitValue('\''),
            system_function=bytes
        ),
        # 'bytearray': UnitType(
        #     id=UnitValue('bytearray'),
        #     alias=UnitValue('barr'),
        #     super=DEFAULT_SUPER_TYPE,
        #     system_function=bytearray
        # ),
        # 'memoryview': UnitType(
        #     id=UnitValue('memoryview'),
        #     alias=UnitValue('mview'),
        #     super=DEFAULT_SUPER_TYPE,
        #     prefix=UnitValue('b\''),
        #     suffix=UnitValue('\''),
        #     system_function=memoryview
        # ),
        # 'none': UnitType(
        #     id=UnitValue('none'),
        #     alias=UnitValue('none'),
        #     super=DEFAULT_SUPER_TYPE,
        #     system_function=None
        # )
    }

    SUPPORTED_TYPES: List[str] = []

    def __init__(
        self,
        override_defaults: Optional[bool] = False,
        overrides: Optional[Dict[str, UnitType]] = None
    ) -> None:
        """
        Initializes the SystemDefaults class.
        """
        if override_defaults and overrides is not None:
            self.override_defaults(overrides)
        elif override_defaults and overrides is None:
            raise ValueError(
                "Overrides must be set if override_defaults is True."
            )
        
        # self.check_type_system_support()

    def override_defaults(self, overrides: Dict[str, UnitType]) -> None:
        """
        Overrides the default values.
        """
        if "system_types" in overrides:
            self.set_default_types(overrides["default_types"])
        if "system_super_type" in overrides:
            self.set_default_super_type(overrides["default_super_type"])
        if len(overrides) > 2:
            raise ValueError(
                "Overrides must be a dictionary with the keys: "
                "'system_types' and/or 'system_super_type'."
            )

    def set_default_types(self, system_types: Dict[str, UnitType]) -> None:
        """
        Sets the system types.
        """
        self.DEFAULT_TYPES = system_types

    def set_default_super_type(self, system_super_type: UnitType) -> None:
        """
        Sets the system super type.
        """
        self.DEFAULT_SUPER_TYPE = system_super_type

    def get_default_types(self) -> Dict[str, UnitType]:
        """
        Returns the system types.
        """
        return self.DEFAULT_TYPES

    def get_default_super_type(self) -> UnitType:
        """
        Returns the system super type.
        """
        return self.DEFAULT_SUPER_TYPE

    def get_default_type_ids(self) -> List[str]:
        """
        Returns the default ids.
        """
        ids: List[str] = self.DEFAULT_TYPES.keys()
        return ids

    def get_default_type_aliases(self) -> List[str]:
        """
        Returns the default aliases.
        """
        aliases: List[str] = []
        for alias in self.DEFAULT_TYPES.values():
            aliases.append(alias)
        return aliases

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

    def get_supported_types(self) -> List[str]:
        """
        Returns the supported types.
        """
        return self.SUPPORTED_TYPES