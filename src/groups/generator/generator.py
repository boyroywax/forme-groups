from . import System
from .type import SystemType
from typing import Optional, List, Dict, Any, Callable
from dataclasses import dataclass, field

@dataclass
class Generator():
    """
    The Generator class manages the generation of types, values, schemas, and groups.
    """
    _system: Optional[System] = None
    _system_types_str: Optional[List[str]] = None
    _system_types: Optional[List[SystemType]] = None

    def __init__(self, system: Optional[System]) -> None:
        """
        Initializes the Generator class.
        """
        if system is not None:
            self.set_system(system)
        else:
            self._system = System()

    def __post_init__(self) -> None:
        if self._system is not None:
            self._system_types_str = self._system.defaults.get_system_types()
            print(f'self._system_types_str: {self._system_types_str}')
        
        # if system is not None:
        #     super().__init__(system)

    def set_system(self, system: System) -> None:
        """
        Sets the system.
        """
        self._system = system

    def get_system(self) -> System:
        """
        Returns the system.
        """
        return self._system

    def create_generator(self, name: Optional[str] = "all") -> Any:
        """
        Creates generators for types, values, schemas, and groups or all.
        Defaults to 'all'.
        """
        match name:
            case "types":
                return TypesGenerator(self)
            # case "values":
            #     return ValuesGenerator(self)
            # case "schemas":
            #     return SchemasGenerator(self)
            # case "groups":
            #     return GroupsGenerator(self)
            # case "all":
            #     return AllGenerator(self)
            case _:
                raise ValueError(
                    "The name must be 'types', 'values',"
                    " 'schemas', 'groups', or 'all'."
                )


class TypesGenerator(Generator):
    """
    The Types_ class manages the generation of types.
    """
    _types: Optional[List[SystemType]] = None

    def __init__(self, generator: Generator) -> None:
        """
        Initializes the Types_ class.
        """
        super().__init__(generator)

    def generate_type(self, type_entry: Dict[str, Any]) -> SystemType:
        """
        Generates a type.
        """
        return SystemType().from_dict(type_entry)

    def generate(self) -> None:
        """
        Generates the types.
        """
        generated_types: List[SystemType] = list()
        types: List[str] = self._system_types_str
        for type_entry in types:
            match type_entry:
                case "str":
                    entry: Dict[str, Any] = {
                        "id": "str",
                        "alias": ["string"],
                        "super": None,
                        "prefix": None,
                        "suffix": None,
                        "separator": None,
                        "system_function": str()
                    }
                    generated_types.append(self.generate_type(entry))
                case "int":
                    entry: Dict[str, Any] = {
                        "id": "int",
                        "alias": ["integer"],
                        "super": None,
                        "prefix": None,
                        "suffix": None,
                        "separator": None,
                        "system_function": int()
                    }   
                    generated_types.append(self.generate_type(entry))
                case "float":
                    entry: Dict[str, Any] = {
                        "id": "float",
                        "alias": ["floating point"],
                        "super": None,
                        "prefix": None,
                        "suffix": None,
                        "separator": None,
                        "system_function": float()
                    }
                    generated_types.append(self.generate_type(entry))
                case "bool":
                    entry: Dict[str, Any] = {
                        "id": "bool",
                        "alias": ["boolean"],
                        "super": None,
                        "prefix": None,
                        "suffix": None,
                        "separator": None,
                        "system_function": bool()
                    }
                    generated_types.append(self.generate_type(entry))

        self._system_types = generated_types

