"""



"""

from abc import ABCMeta
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from .base import BaseInterface
from ..utils.merkle_tree import MerkleTree


__DEFAULT_COLLECTION_TYPES__ = list | tuple | dict | set
    

@define(slots=True)
class ContainerInterface(BaseInterface, metaclass=ABCMeta):
    """An abstract interface for a collection of hashable BaseInterface objects.
    """
    _items: Optional[__DEFAULT_COLLECTION_TYPES__] = field(default=None, validator=validators.optional(validators.instance_of(__DEFAULT_COLLECTION_TYPES__)))

    def __init__(self, items: Optional[__DEFAULT_COLLECTION_TYPES__] = None):
        """Initialize the ContainerInterface.

        Args:
            items (__DEFAULT_COLLECTION_TYPES__ | None): The items to initialize the ContainerInterface with. Defaults to None.
        """
        if items is None:
            raise ValueError("Cannot initialize ContainerInterface with None.")
        setattr(self, "_items", items)