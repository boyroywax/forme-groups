from dataclasses import dataclass

from ._unit import Unit
from .alias import Alias
from .super import Super
from .prefix import Prefix
from .suffix import Suffix
from .separator import Separator
from .function import Function


@dataclass
class Base:
    """
    Manages the base of the group object.
    """
    alias: Alias
    super: Super
    prefix: Prefix
    suffix: Suffix
    separator: Separator
    function: Function

