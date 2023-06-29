from dataclasses import dataclass

from ._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Separator(SuperUnit):
    """
    Manages the separator of the group object.
    """
    pass
