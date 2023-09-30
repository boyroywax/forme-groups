"""



"""

from abc import ABCMeta
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from .base import BaseInterface
from ..utils.defaults import __DEFAULT_COLLECTION_TYPES__
from ..utils.merkle_tree import MerkleTree


@define(frozen=True, slots=True, weakref_slot=False)
class ContainerInterface(BaseInterface):
    """An abstract interface for a collection of hashable BaseInterface objects.
    """
    _items: Optional[__DEFAULT_COLLECTION_TYPES__] = field(default=None, validator=validators.optional(validators.instance_of(__DEFAULT_COLLECTION_TYPES__)))

    def __pre_init__(self, items: Optional[__DEFAULT_COLLECTION_TYPES__] = None):
        """Initialize the ContainerInterface.

        Args:
            items (__DEFAULT_COLLECTION_TYPES__ | None): The items to initialize the ContainerInterface with. Defaults to None.
        """
        if items is None:
            raise ValueError("Cannot initialize ContainerInterface with None.")
        setattr(self, "_items", items)

    @property
    def items(self) -> __DEFAULT_COLLECTION_TYPES__ | None:
        """Get the items of the ContainerInterface.

        Returns:
            __DEFAULT_COLLECTION_TYPES__: The items of the ContainerInterface.
        """
        return self._items
    
    @property
    def type_ref(self) -> str:
        """Get the type_ref of the ContainerInterface.

        Returns:
            str: The type_ref of the ContainerInterface.
        """
        return type(self._items).__name__