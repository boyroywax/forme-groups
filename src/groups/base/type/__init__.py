from dataclasses import dataclass

# from ._unit import Unit
from .id import Id
from .alias import Alias
from .super import Super
from .prefix import Prefix
from .suffix import Suffix
from .separator import Separator
from .function import Function


@dataclass
class Type():
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
    "Type",
    "Id",
    "Alias",
    "Super",
    "Prefix",
    "Suffix",
    "Separator",
    "Function",
]
