from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .super import Super__

_FORCE_SUPER_TYPE = False


@dataclass
class Value_(Super__):

    value__: Optional[Any] = None

    def __init__(
        self,
        value__: Optional[Any] = None,
        _super: Optional[Super__] = None
    ) -> None:
        """
        Initializes the Value__ class.
        """
        self.value__ = value__
        super().__init__(_super)

    def validate(self) -> bool:
        """
        Validates the value of the Value__ object.
        """
        return True