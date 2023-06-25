from typing import Any, Dict, List, Optional
from src.groups.base.type import Type as Type_


class Config_Schema():
    """
    This class defines the Schema of the config.
    The default config is:
    {
        "name": "default",
        "system": {
            "super_type": "string",
            "types": [
                "str",
                "int",
                "float",
                "bool",
                "bytes",
                "list",
                "tuple",
                "dict"
            "schemas": [
                
            ]
        }
        "defined": {
            "types": [
                Types_...
            ],
            "
        }        
    }
    """
    _name: str
    _system_types: Dict[str, Any]
    _defined_types: List[Type_]
    
    def __init__(
        self,
        name: str = "default",
        system_types: Dict[str, Any] = {
            "super_type": _SUPER_TYPE,
            "supported": _DEFAULT_SYSTEM_TYPES
        },
        defined_types: Optional[List[Type_]] = None
    ) -> None:
        """
        Initializes the Config_Schema class.
        """
        self._name: str = name
        self._system_types: Dict[str, Any] = system_types

        if defined_types is not None:
            self._loaded_types: List[Type_] = defined_types


    @property
    def name(self) -> str:
        """
        Returns the name of the config.
        """
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of the config.
        """
        self._name = name

    @name.getter
    def name(self) -> str:
        """
        Returns the name of the config.
        """
        return self._name
    
    @name.deleter
    def name(self) -> None:
        """
        Deletes the name of the config.
        """
        del self._name

    @property
    def system_types(self) -> Dict[str, Any]:
        """
        Returns the system types of the config.
        """
        return self._system_types
    
    @property
    def loaded_types(self) -> List[Type_]:
        """
        Returns the loaded types of the config.
        """
        return self._loaded_types
    