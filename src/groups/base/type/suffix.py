from dataclasses import dataclass

from ..super._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Suffix(SuperUnit):
    """
    Manages the suffix of the group object.
    """
    pass
