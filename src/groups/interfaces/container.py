"""



"""

from abc import ABC
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from ..utils.merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_UNIT_TYPE__ = str
__DEFAULT_COLLECTION_TYPES__ = list | tuple | dict | set
    

@define(slots=True)
class ContainerInterface(ABC):
    """An abstract interface for a collection of hashable BaseInterface objects.
    """

    def __init__(self, items: Optional[__DEFAULT_COLLECTION_TYPES__] = None):
        """Initialize the ContainerInterface.

        Args:
            items (__DEFAULT_COLLECTION_TYPES__, optional): The items to initialize the ContainerInterface with. Defaults to None.
        """
        if items is None:
            raise ValueError("Cannot initialize ContainerInterface with None.")
        setattr(self, "items", items)