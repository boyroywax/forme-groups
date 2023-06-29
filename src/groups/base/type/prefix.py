from dataclasses import dataclass

from ._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Prefix(SuperUnit):
    """
    Manages the prefix of the group object.
    """
    pass
