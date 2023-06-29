from dataclasses import dataclass
from typing import Optional

from ._unit import Unit_ as SuperUnit


@dataclass(
    slots=True,
)
class Id(SuperUnit):
    """
    Manages the id of the group object.
    """
    pass
