from dataclasses import dataclass
from typing import Any, Dict, List, Optional

# from . import System
from .defaults import Defaults as SystemDefaults
from .checks import Checks as SystemChecks
from ..units.value import Value_ as SystemValue


@dataclass
class Config():

    # _system: Optional[System] = None
    _super_value_type_name: Optional[Any] = None

    def __init__(
        self,
        override_defaults: Optional[bool] = False,
        overrides: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes the Config class.
        """
        self._defaults = SystemDefaults(
            override_defaults=override_defaults,
            overrides=overrides
        )
        self._checks = SystemChecks(self._defaults)
        self._value = SystemValue()
        self._super_value_type_name = self._defaults.get_system_super_type_name()

    def get_defaults(self) -> Dict[str, Any]:
        """
        Returns the defaults.
        """
        return self._defaults.get_defaults()
    
    def get_super_value_type_name(self) -> str:
        """
        Returns the super value type name.
        """
        return self._super_value_type_name
    
