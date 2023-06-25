from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Config():
    """
    The Config class manages the configuration of the module.
    """
    id: str
    system: Dict[str, Any]
    defined: Dict[str, Any]
