from dataclasses import dataclass

from ._unit import Unit_ as SuperUnit


@dataclass
class Suffix(SuperUnit):
    """
    Manages the suffix of the group object.
    """
    pass
