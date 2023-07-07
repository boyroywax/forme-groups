from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from .decorators import check_frozen
from .frozen import Frozen, FrozenInterface
from .value_type import ValueTypeInterface, ValueType
from .value_type_group import ValueTypeGroup



@dataclass(slots=True)
class GroupSchemaInterface(FrozenInterface):
    """
    
    """
    pass


@dataclass(slots=True)
class GroupSchema(GroupSchemaInterface, Frozen):
    """
    The class that manages the group schema.
    * The schema is a set of value type groups.
    * 

    """
    _type_groups: Dict[str, ValueTypeGroup] = field(default_factory=dict)

    def __init__(self, type_groups: Optional[Tuple[ValueTypeGroup]] = None) -> None:
        """
        """

        for type_group in type_groups:
            if type_group.name in self._type_groups:
                raise ValueError(f'The type group {type_group.name} already exists.')
            self._type_groups[type_group.name] = type_group

    @property
    def type_groups(self) -> Dict[str, ValueTypeGroup]:
        """
        The type groups of the group schema.
        """
        return self._type_groups
    
    @property
    def types(self) -> Dict[str, ValueType]:
        """
        The types of the group schema.
        """
        types = {}
        for type_group in self._type_groups.values():
            types.update(type_group.types)
        return types
