from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Schema:
    """
    A Super Schema class to control the system of group objects and their units.
    """

    _schema: Optional[Dict[str, Any]] = None

    def system_defaults(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Sets the system defaults.
        """
        self._schema = {
            "system": {
                "super_unit_system_types": [str, int, float, bool, list, dict, tuple, bytes, None],
                "default_super_unit_system_type": str,
            },
            "super_units": {
                "enforce_default_super_unit_system_type": False,
                "allow_none": True,
                "allow_random": True,
            },
            "base_units": {
                "default_base_unit_types": [
                    "str",
                    "int",
                    "float",
                    "bool",
                    "bytes",
                ],
                "default_base_unit_contaner_types": [
                    "list",
                    "dict",
                    "tuple",
                ],
                "override_defaults": False,
                "overrides": {}
            },
            "group_units": {
                "default_group_unit_types": [
                    {"did": {"accepts": ["str"]}},
                    {"nonce": {"accepts": ["base_units"]}},
                    {"owner": {"accepts": ["did"]}},
                    {"credential": {"accepts": ["did"]}},
                    {"data_entry": {"accepts": ["base_units"]}},
                ],
                "default_group_unit_container_types": [
                    {"nonce_chain": {"type": ["list"], "accepts": ["nonce"]}},
                    {"owners": {"type": ["list"], "accepts": ["owner"]}},
                    {"credentials": {"type": ["list"], "accepts": ["credential"]}},
                    {"data": {"type": ["list"], "accepts": ["data_entry"]}},
                ],
                "default_group_unit": {"type": "dict", "requires": [
                    "nonce_chain",
                    "owners",
                    "credentials",
                    "data",
                ]},
                "override_defaults": False,
                "overrides": {}
            },
            "group": {
                "default_group_type": ["default_group_unit"],
                "override_defaults": False,
                "overrides": {}
            },
        }
