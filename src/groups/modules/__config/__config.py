from typing import Optional, List, Any, Dict
from groups.modules.__base.__type import Type_


class Config_Type_Entry():
    """
    
    """
    _name: str
    _super_type: str
    _aliases: List[str]
    _prefix: str
    _suffix: str
    _attrs: Dict[str, Any]
    
    def __init__(
        self,
        name: str,
        super_type: str,
        aliases: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None
    ) -> None:
        """
        Initializes the Config_Type_Entry class.
        """
        self._name: str = name
        self._super_type: str = super_type
        self._aliases: List[str] = aliases if aliases is not None else []
        self._prefix: str = prefix if prefix is not None else ""
        self._suffix: str = suffix if suffix is not None else ""
        self._attrs: Dict[str, Any] = {}
    
    @property
    def name(self) -> str:
        """
        Returns the name of the Config_Type_Entry.
        """
        return self._name
    
    @property
    def super_type(self) -> str:
        """
        Returns the super_type of the Config_Type_Entry.
        """
        return self._super_type
    
    @property
    def aliases(self) -> List[str]:
        """
        Returns the aliases of the Config_Type_Entry.
        """
        return self._aliases
    
    @property
    def prefix(self) -> str:
        """
        Returns the prefix of the Config_Type_Entry.
        """
        return self._prefix
    
    @property
    def suffix(self) -> str:
        """
        Returns the suffix of the Config_Type_Entry.
        """
        return self._suffix
    
    @property
    def attrs(self) -> Dict[str, Any]:
        """
        Returns the attrs of the Config_Type_Entry.
        """
        return self._attrs
    
    def add_attr(self, key: str, value: Any) -> None:
        """
        Adds an attr to the Config_Type_Entry.
        """
        self._attrs[key] = value

    def remove_attr(self, key: str) -> None:
        """
        Removes an attr from the Config_Type_Entry.
        """
        del self._attrs[key]

    def get_attr(self, key: str) -> Any:
        """
        Returns an attr from the Config_Type_Entry.
        """
        return self._attrs[key]
    
    def type_entry_to_dict(self) -> dict:
        """
        Returns the Config_Type_Entry as a dict.
        """
        return {
            "name": self._name,
            "super_type": self._super_type,
            "aliases": self._aliases,
            "prefix": self._prefix,
            "suffix": self._suffix,
            "attrs": self._attrs
        }
    
    



class Config_():
    """
    This class is used to configure the group system.
    Creates a default config if no config is provided.
    """

    loaded_configs: List[Dict] = [{}]
    active_config: Optional[Dict] = loaded_configs[0]

    def __init__(
        self,
        config: Optional[Config_Schema] = None
    ) -> None:
        """
        Initializes the Config class.
        """

        if configs is not None:
            self.set_config_list(configs)

    def set_config_list(self, configs: List[Dict]) -> None:
        """
        Sets the config list.
        """
        if len(configs) > 0:
            for config in configs:
                self.set_config(config)
        elif len(configs) == 0:
            raise Exception("No configs provided.")
        else:
            raise Exception("Invalid config list provided.")

    def set_config(self, config: Dict) -> None:
        """
        Sets the config. 
        First, checks if the config is already loaded.
        Appends the config to the loaded configs.
        """
        if config in self.loaded_configs:
            raise Exception("Config already loaded.")
        else:
            self.loaded_configs.append(config)

    def get_config(
        self,
        index: Optional[int] = None,
        args: Optional[List] = None
    ) -> Dict:
        """
        Gets the config at the specified index.
        Or, if no index is provided, returns the
        specified config ('active' or 'loaded').
        """
        if index is None and args is None:
            return self.active_config
        elif index is not None and args is None:
            return self.loaded_configs[index]
        elif index is None and args is not None:
            if len(args) == 1 and args[0] == "active":
                return self.active_config
            elif len(args) == 1 and args[0] == "loaded":
                return self.loaded_configs
            else:
                raise Exception("Invalid args provided.")
        else:
            raise Exception("Invalid args provided.")
        

    def check_for_supported_system_types(self) -> List[str]:
        """
        Checks if the system types are supported.
        """
        default_system_types: List[str] = _DEFAULT_SYSTEM_TYPES
        supported_system_types: List[str] = []
        for system_type in default_system_types:
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
                    raise Exception("Invalid system type provided.")

        return supported_system_types

    def validate_super_type(self) -> bool:
        """
        Validates the super type.
        """
        if _SUPER_TYPE in self.check_for_supported_system_types():
            return True
        else:
            return False

    def set_default_config(
        self,
        super_type: Optional[str] = _SUPER_TYPE,
        system_types: Optional[List[str]] = _DEFAULT_SYSTEM_TYPES
    ) -> None:
        """
        Sets the default config list and active config.
        """
        if self.validate_super_type():
            self.active_config["super_type"] = super_type
        else:
            raise Exception("Invalid super type provided.")

        for system_type in system_types:
            if system_type in self.check_for_supported_system_types():
                self.active_config["system_types"].append(system_type)
            else:
                raise Exception("Invalid system type provided.")

