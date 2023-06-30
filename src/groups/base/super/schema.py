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
            # Defines the system defaults.
            "system": {
                "default_system_type_schema": {
                    "type": List[Any],  #id and aliases
                },
                "default_system_types": [str, int, float, bool, list, dict, tuple, bytes, None],
                "check_system_types": True,  # System types are checked by default.
                "override_defaults": False,
                "overrides": {
                    # Example (Simplified System Types)
                    "default_system_types": [str, int, float]
                }
            },

            # Defines the super unit defaults.
            "super_units": {
                "default_super_schema": {
                    "id_": List[Any],  # id and aliases
                    "accepts": List[Any],  # system types accepted by the super unit.
                    "prefix": Optional[Any],  # prefix for the super unit.
                    "suffix": Optional[Any],  # suffix for the super unit.
                    "separator": Optional[Any]  # separator for the super unit.
                },
                "allow_none_value": True,  #  if True, the super unit can be NoneType.
                "allow_random_value": True,  #  if True, the super unit can be a random value.
                "default_base_unit_types": [
                    {"id_": ["str"], "accepts": [str]},
                    {"id_": ["int"], "accepts": [int]},
                    {"id_": ["float"], "accepts": [float]},
                    {"id_": ["bool"], "accepts": [bool]},
                    {"id_": ["list"], "accepts": [list]},
                    {"id_": ["dict"], "accepts": [dict]},
                    {"id_": ["tuple"], "accepts": [tuple]},
                    {"id_": ["bytes"], "accepts": [bytes]},
                    {"id_": ["NoneType"], "accepts": [None]},
                ],
                "override_defaults": False,
                "overrides": {
                    # Example (simplified basic type classes)
                    "default_base_types": [
                        {"id_": ['text'], "accepts": [str]},
                        {"id_": ['number'], "accepts": [int, float]},
                        {"id_": ['list'], "accepts": [str], "prefix": "[", "suffix": "]", "separator": ","},
                        {"id_": ['dict'], "accepts": [str], "prefix": "{", "suffix": "}", "separator": ","}
                    ]
                },
            },

            # Defines the base unit defaults.
            "base_units": {
                "default_group_unit_types": [
                    {"did": {"type": ["str"], "accepts": ["str"]}},
                    {"nonce": {"type": ["ANY_base_unit"], "accepts": ["ANY_base_units"]}},
                    {"owner": {"type": ["did"], "accepts": ["did"]}},
                    {"credential": {"type": ["did"], "accepts": ["did"]}},
                    {"data_entry": {"type": ["ANY_base_units"], "accepts": ["ANY_base_units"]}},
                    {"nonce_chain": {"type": ["list"], "accepts": ["nonce"]}},
                    {"owners": {"type": ["list"], "accepts": ["owner"]}},
                    {"credentials": {"type": ["list"], "accepts": ["cred"], "prefix": "creds:[", "suffix": "]", "separator": ","}},
                    {"data": {"type": ["list"], "accepts": ["entry"], "prefix": "data:[", "suffix": "]", "separator": ","}},
                ],
            },

            # Defines the group unit defaults.
            "group_units": {
                "default_group_unit": {"type": "dict", "accepts": [
                    "nonce_chain",
                    "owners",
                    "credentials",
                    "data",
                ], "prefix": "{", "suffix": "}", "separator": ","},
                "override_defaults": False,
                "overrides": {}
            },

            # Defines the group defaults.
            "group": {
                "default_group_type": {"type": ["group"], "accepts": ["default_group_unit"]},
                "override_defaults": False,
                "overrides": {}
            },
        }
