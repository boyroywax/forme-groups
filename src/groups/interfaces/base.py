from abc import ABC
from attrs import define
from typing import Any, Optional, Tuple, List

from ..merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_UNIT_TYPE__ = str
__DEFAULT_COLLECTION_TYPES__ = list | tuple | dict | set


@define(slots=True)
class BaseInterface(ABC):
    """An abstract interface for a hashable Reference Object.
    """
    def _slots_to_string(
        self,
        values_only: Optional[bool] = True,
        keys_only: Optional[bool] = False
    ) -> str:
        """Return a string containing the slots of the object.

        Returns:
            str: A string containing the slots of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example._slots_to_string(values_only=True))
            >>> "example"

        """
        assert values_only is not True or keys_only is not True, "Cannot have both values_only and keys_only set to True."

        if values_only:
            _slot_values: str = ""
            for slot in self.__slots__:
                _slot_values += (f"{getattr(self, slot)}, ")
            return _slot_values[:-2]
        elif keys_only:
            return ", ".join(self.__slots__)
        else:
            _slots: str = ""
            for slot in self.__slots__:
                _slots += (f"{slot}={getattr(self, slot)}, ")
            return _slots[:-2]

    def __str__(self) -> str:
        """Return a string containing the attributes of the object.

        Returns:
            str: A string containing the attributes of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.__str__())
            >>> "test"

        """
        return self._slots_to_string(values_only=True)
        

    def __repr__(self) -> str:
        """Return a string containing the representation of the object.

        Returns:
            str: A string containing the representation of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.__repr__())
            >>> 'InterfaceExample(example="test")'
        """
        return f"{self.__class__.__name__}({self._slots_to_string(values_only=False, keys_only=False)})"

    def __iter__(self):
        """Return an iterator over the attributes of the object.

        Returns:
            Iterator[Any]: An iterator over the attributes of the object.

        Example::


            for attribute in base_ref:
                print(attribute)
            >>> "str"
        """
        slots = self.__slots__
        for slot in slots:
            if getattr(self, slot) is __DEFAULT_COLLECTION_TYPES__:
                for item in getattr(self, slot):
                    yield item.__iter__()
            yield getattr(self, slot)

    def hash_tree(self) -> MerkleTree:
        """Return the hash of the object.

        Returns:
            str: The hash of the object.

        Example:
            >>> from src.groups.base import UnitTypeRef
            >>> base_ref = UnitTypeRef(alias="str")
            >>> print(base_ref.__hash__())
            "8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702"
        """
        attribute_hashes = []
        for slot in self.__slots__:
            attribute = getattr(self, slot)
            if attribute is __DEFAULT_COLLECTION_TYPES__:
                for item in attribute:
                    attribute_hashes.append(MerkleTree.hash_func(repr(item)))

            attribute_hashes.append(MerkleTree.hash_func(getattr(self, slot)))

        return MerkleTree(attribute_hashes)

    def hash_sha256(self) -> str:
        """Return the hash tree of the object.

        Returns:
            MerkleTree: The hash tree of the object.

        Example:
            >>> from src.groups.base import UnitTypeRef
            >>> base_ref = UnitTypeRef(alias="str")
            >>> print(base_ref.hash_tree())
            MerkleTree(hashed_data=["8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702"])
        """
        return self.hash_tree().root()

    def contains_hash(self, hash: str) -> bool:
        """Return whether the object contains the hash.

        Args:
            hash (str): The hash to check.

        Returns:
            bool: Whether the object contains the hash.

        Example:
            >>> from src.groups.base import UnitTypeRef
            >>> base_ref = UnitTypeRef(alias="str")
            >>> print(base_ref.contains_hash("8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702"))
            True
        """
        return self.hash_tree().verify(hash)
