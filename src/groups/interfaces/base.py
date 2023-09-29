from abc import ABC
from attrs import define

from ..merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_UNIT_TYPE__ = str
__DEFAULT_COLLECTION_TYPES__ = list | tuple | dict | set


@define(slots=True)
class BaseInterface(ABC):
    """An abstract interface for a hashable Reference Object.
    """
    def __str__(self) -> str:
        """Return a string containing the attributes of the object.

        Returns:
            str: A string containing the attributes of the object.

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias="str")
            >>> print(unit_type_ref)
            "str"
        """
        slots = self.__slots__
        output = ""
        for slot in slots:
            output += f"{getattr(self, slot)}, "
        return output[:-2]

    def __repr__(self) -> str:
        """Return a string containing the representation of the object.

        Returns:
            str: A string containing the representation of the object.

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias="str")
            >>> print(unit_type_ref.__repr__())
            "UnitTypeRef(alias='str')"

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias=("str", "int",))
            >>> print(unit_type_ref.__repr__())
            "UnitTypeRef(alias='str')"
        """
        slots = self.__slots__
        output = ""
        for slot in slots:
            if getattr(self, slot) is __DEFAULT_COLLECTION_TYPES__:
                output += f"{slot}=["
                for item in getattr(self, slot):
                    output += f"{item.__repr__()}, "
                output = output[:-2] + "], "
            else:
                output += f"{slot}={getattr(self, slot).__repr__()}, "
        return f"{self.__class__.__name__}({output[:-2]})"

    def __iter__(self):
        """Return an iterator over the attributes of the object.

        Returns:
            Iterator[Any]: An iterator over the attributes of the object.

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias="str")
            >>> for attribute in unit_type_ref:
            ...     print(attribute)
            "str"
        """
        slots = self.__slots__
        for slot in slots:
            if getattr(self, slot) is __DEFAULT_COLLECTION_TYPES__:
                for item in getattr(self, slot):
                    yield item
            yield getattr(self, slot)

    def hash_tree(self) -> MerkleTree:
        """Return the hash of the object.

        Returns:
            str: The hash of the object.

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias="str")
            >>> print(unit_type_ref.__hash__())
            "8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702"
        """
        attribute_hashes = []
        for slot in self.__slots__:
            if getattr(self, slot) is __DEFAULT_COLLECTION_TYPES__:
                unit_hashes = []
                for item in getattr(self, slot):
                    unit_hashes.append(MerkleTree.hash_func(item.__repr__()))
                attribute_hashes.append(MerkleTree(hashed_data=unit_hashes).root())
            else:
                attribute_hashes.append(MerkleTree.hash_func(self.__repr__()))

        return MerkleTree(attribute_hashes)

    def hash_sha256(self) -> MerkleTree:
        """Return the hash tree of the object.

        Returns:
            MerkleTree: The hash tree of the object.

        Example:
            >>> from src.groups.unit_type import UnitTypeRef
            >>> unit_type_ref = UnitTypeRef(alias="str")
            >>> print(unit_type_ref.hash_tree())
            MerkleTree(hashed_data=["8f245b629f9dbd96e39c50751394daf5b1791a35ec4e9213ecec3d157aaf5702"])
        """
        return self.hash_tree().root()
