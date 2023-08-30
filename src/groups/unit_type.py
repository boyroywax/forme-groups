from attrs import define, field
from typing import List, Optional, Callable

from .unit_type_ref import UnitTypeRef


@define(frozen=True, slots=True)
class UnitType:
    """A Unit Type defines a the type of unit

    """

    aliases: List[UnitTypeRef] = field(default=[])
    super_type: Optional[UnitTypeRef] = field(default=None)
    prefix: Optional[str] = field(default=None)
    suffix: Optional[str] = field(default=None)
    seperator: Optional[str] = field(default=None)
    container: bool = field(default=False)
    function_call: Callable = field(default=None)
