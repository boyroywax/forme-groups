from typing import List, Dict, Any, Optional

from .type import SystemType
from .defaults import SystemDefaults


class System():
    """
    A Class that represents a System.
    """
    defaults: SystemDefaults = SystemDefaults()
    supported_types: List[SystemType] = []

    def __init__(
        self,
        default_override: Optional[bool] = False,
        **kwargs: Optional[Dict[str, Any]]
    ) -> None:
        """
        Initializes the System class.
        """
        if default_override and len(kwargs) > 0:
            self.defaults.override_defaults(kwargs)
        elif default_override and len(kwargs) == 0:
            raise ValueError(
                "Overrides must be set if override_defaults is True."
            )
