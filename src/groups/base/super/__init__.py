from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .unit import Unit_
from .enforcer import Enforcer


@dataclass
class Super:
    """
    The super class manages the super units for all units.
    """

    enforcer: Enforcer = None
    enforcer_activated: bool = False
    super_unit_type: Optional[str] = None

    def __init__(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Initializes the Super class.
        """
        self.enforcer = Enforcer()

    def set_super_unit_type(
        self,
        super_unit_type: Optional[str] = None
    ) -> None:
        """
        Sets the super unit type.
        """
        self.enforcer.set_super_unit_type(super_unit_type)

    def create(
        self,
        *args,
        **kwargs
    ) -> Unit_:
        """
        Creates a super unit.
        """
        return Unit_(
            *args,
            **kwargs
        )
    


