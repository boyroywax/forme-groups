from dataclasses import dataclass

from ..super._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Function(SuperUnit):
    """
    Manages the system function of the group object.
    """
    pass
