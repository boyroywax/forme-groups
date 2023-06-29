from dataclasses import dataclass

# from ._unit import Unit_ as SuperUnit
from .id import Id
from .alias import Alias
from .super import Super
from .prefix import Prefix
from .suffix import Suffix
from .separator import Separator
from .function import Function


@dataclass(
    slots=True,
)
class Type_():
    """
    Manages the base of the group object.
    """
    id: Id
    alias: Alias
    super: Super
    prefix: Prefix
    suffix: Suffix
    separator: Separator
    function: Function


__all__ = [
    "Type_",
    "Id",
    "Alias",
    "Super",
    "Prefix",
    "Suffix",
    "Separator",
    "Function",
]
