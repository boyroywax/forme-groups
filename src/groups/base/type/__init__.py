from dataclasses import dataclass, field
from typing import Optional

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
class Type_:
    """
    Manages the base of the group object.
    """
    id_: Optional[Id] = field(default_factory=Id)
    alias: Optional[Alias] = field(default_factory=Alias)
    super_: Optional[Super] = field(default_factory=Super)
    prefix: Optional[Prefix] = field(default_factory=Prefix)
    suffix: Optional[Suffix] = field(default_factory=Suffix)
    separator: Optional[Separator] = field(default_factory=Separator)
    function_: Optional[Function] = field(default_factory=Function)

    # id: Id #= field(default_factory=Id)
    # alias: Alias #= field(default_factory=Alias)
    # super: Super #= field(default_factory=Super)
    # prefix: Prefix #= field(default_factory=Prefix)
    # suffix: Suffix #= field(default_factory=Suffix)
    # separator: Separator #= field(default_factory=Separator)
    # function: Function #= field(default_factory=Function)

    def __init__(
            self,
            id_: Id = None,
            alias: Alias = None,
            super_: Super = None,
            prefix: Prefix = None,
            suffix: Suffix = None,
            separator: Separator = None,
            function_: Function = None,
    ):
        """
        Post-initialization.
        """

        self.id_ = id_
        self.alias = alias
        self.super_ = super_
        self.prefix = prefix
        self.suffix = suffix
        self.separator = separator
        self.function_ = function_

    def to_dict(self):
        """
        Return the Type_ class as a dictionary.
        """
        return {
            "id": self.id.to_dict(),
            "alias": self.alias.to_dict(),
            "super": self.super_.to_dict(),
            "prefix": self.prefix.to_dict(),
            "suffix": self.suffix.to_dict(),
            "separator": self.separator.to_dict(),
            "function": self.function_.to_dict(),
        }


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
