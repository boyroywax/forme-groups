import json
from typing import List, Optional, Dict, Any


class SystemDefaults():
    """
    Default values for system group.
    """

    system_types: List[str] = [
        "bytes",
        "str",
        "int",
        "float",
        "bool",
        "list",
        "tuple",
        "dict",
        "set",
        "frozenset",
        "complex",
        "range",
        "memoryview",
        "None"
    ]

    system_super_type: Optional[str] = 'str'

    def __init__(
        self,
        override_defaults: Optional[bool] = False,
        overrides: Optional[Dict[str, Any]] = None
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

    def override_defaults(self, overrides: Dict[str, Any]) -> None:
        """
        Overrides the default values.
        """
        if "system_types" in overrides:
            self.set_system_types(overrides["system_types"])
        if "system_super_type" in overrides:
            self.set_system_super_type(overrides["system_super_type"])
        if len(overrides) > 2:
            raise ValueError(
                "Overrides must be a dictionary with the keys: "
                "'system_types' and/or 'system_super_type'."
            )

    def set_system_types(self, system_types: List[str]) -> None:
        """
        Sets the system types.
        """
        self.system_types = None
        self.system_types = system_types

    def get_system_types(self) -> List[str]:
        """
        Returns the system types.
        """
        return self.system_types

    def set_system_super_type(self, system_super_type: str) -> None:
        """
        Sets the system super type.
        """
        self.system_super_type = None
        self.system_super_type = system_super_type

    def get_system_super_type(self) -> str:
        """
        Returns the system super type.
        """
        return self.system_super_type

    def system_defaults_to_dict(self) -> Dict[str, Any]:
        """
        Returns the object in a dictionary format.
        """
        return {
            "system_types": self.system_types,
            "system_super_type": self.system_super_type
        }

    def system_defaults_to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(
            self.system_defaults_to_dict(),
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )

    def system_defaults_from_dict(self, dict_: Dict[str, Any]) -> None:
        """
        Sets the object from a Dictioniary.
        """
        if "system_types" in dict_:
            self.set_system_types(dict_["system_types"])
        if "system_super_type" in dict_:
            self.system_super_type = dict_["system_super_type"]

    def system_defaults_from_json_string(self, json_string: str) -> None:
        """
        Sets the object from a JSON string.
        """
        json_dict = json.loads(json_string)
        self.system_defaults_from_dict(json_dict)

    def system_defaults_from_json_file(self, json_file: str) -> None:
        """
        Sets the object from a JSON file.
        """
        with open(json_file, "r") as json_file:
            json_dict = json.load(json_file, )
            self.system_defaults_from_dict(json_dict)

    def system_defaults_to_json_file(self, json_file: str) -> None:
        """
        Sets the object from a JSON file.
        """
        with open(json_file, "w") as json_file:
            json.dump(
                self.system_defaults_to_dict(),
                json_file,
                default=lambda o: o.__dict__
            )
