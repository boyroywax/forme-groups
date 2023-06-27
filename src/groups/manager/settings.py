from ..units.base.defaults import Defaults
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from ..units.unit import UnitType


@dataclass
class Settings():
    """
    This class handles the unit system settings
    """
    defaults: Defaults = Defaults()
    supported: Dict[str, UnitType] = field(default_factory=dict)
    active_types: Dict[str, UnitType] = field(default_factory=dict)

    def __init__(
        self,
        override_defaults: Optional[bool] = False,
        overrides: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes the Settings class.
        """
        self.defaults = Defaults(
            override_defaults=override_defaults,
            overrides=overrides
        )

    def get_defaults(self) -> Dict[str, Any]:
        """
        Returns the defaults.
        """
        return self.defaults.get_defaults()
    
    def check_system_support(self) -> None:
        """
        Checks if the defaults are supported by the system.
        """
        for type_id in self.defaults.get_default_type_ids():
            if not self.check_type(type_id):
                raise ValueError(
                    f"The type {type_id} is not supported by the system."
                )
    
    def check_type(self, type_id: str) -> bool:
        """
        Checks if the type is supported.
        """
        return type_id in self.supported_system_types.keys()
    
    def get_supported_types(self) -> List[str]:
        """
        Returns the supported types.
        """
        return list(self.supported_system_types.keys())
    
    def get_active_types(self) -> List[str]:
        """
        Returns the active types.
        """
        return list(self.active_types.keys())
    

    




