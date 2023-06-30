from dataclasses import dataclass

from ..super.unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Alias(SuperUnit):
    """
    Manages the alias of the group object.
    """
    

