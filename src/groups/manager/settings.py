from .defaults import Defaults
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from ..units import UnitType
from .. import Config


@dataclass
class Settings():
    """
    This class handles the unit system settings
    """
    config: Optional[Config] = None
    defaults: Optional[Defaults] = None
    overrides: Optional[Dict[str, Any]] = None
    supported: Optional[Dict[str, UnitType]] = None
    active_types: Optional[Dict[str, UnitType]] = None

    def __init__(
        self,
        overrides: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes the Settings class.
        """
        if overrides is not None:
            self.overrides = overrides

    def init_defaults(self) -> None:
        """
        Initializes the defaults.
        """
        self.defaults = Defaults()

    def init_supported_types(self) -> None:
        """
        Initializes the supported types.
        """
        self.supported = self.defaults.get_supported_types()
        

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
    

    




