from dataclasses import dataclass

from ._unit import Unit_ as SuperUnit


@dataclass
class Super(SuperUnit):
    """
    Manages the super of the group object.
    """
    pass
