from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .defaults import Defaults
from .defined import Defined
from .supported import Supported


@dataclass
class Types():
    """
    Manages the types of the group object.
    """
    _defaults: Optional[Defaults] = None
    _defined: Optional[Defined] = None
    _supported: Optional[Supported] = None

    def __post_init__(self):
        """
        Post initialisation hook.
        """
        self._defaults = Defaults()
        self._defined = Defined()
        self._supported = Supported()

    def get(self, id: str) -> Optional[Any]:
        """
        Get the type by ID.
        """
        type = self._defaults.get(id)

        if type is None:
            type = self._defined.get(id)

        if type is None:
            type = self._supported.get(id)

        return type