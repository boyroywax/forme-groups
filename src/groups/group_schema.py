from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value_type_group import ValueTypeGroup



@dataclass(slots=True)
class GroupSchemaInterface(FrozenInterface):
    """
    
    """
    pass


@dataclass(slots=True)
class GroupSchema(GroupSchemaInterface, Frozen):
    """
    
    """
    _group_types: Tuple[ValueTypeGroup] = field(default_factory=tuple)

    def __init__(self) -> None:
        """
        """
        
