import hashlib
from attrs import define, field, validators
import json
from typing import Any, Optional, Tuple

from .unit_type import UnitType, UnitTypeRef, UnitTypeFunction

# from merkle_tree import MerkleTree

__DEFAULT_SYSTEM_TYPES_PATH__ = "src/groups"


@define(frozen=True, slots=True)
class Unit:
    value: Any = field(default=None)
    type_ref: UnitTypeRef = field(default=None)


