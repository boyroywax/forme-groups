from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Config():
    override_system_defaults: Optional[bool] = False
    system_default_overrides: Optional[Dict[str, Any]] = None # A dictionary with the keys: "system_types" and/or "system_super_type".
    use_system_super_types: Optional[bool] = True