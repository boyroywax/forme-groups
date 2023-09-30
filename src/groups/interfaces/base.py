"""



"""

from abc import ABC, ABCMeta
from attrs import define, field, validators
from typing import Any, Optional, Tuple, List

from ..utils.merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"
__DEFAULT_UNIT_TYPE__ = str
__DEFAULT_COLLECTION_TYPES__ = list | tuple | dict | set


@define(frozen=True, slots=True, weakref_slot=False)
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

        _slot_str: str = ""
        for slot in self.__slots__:
            print(self.__slots__)
            if values_only:
                _slot_str += (f"{getattr(self, slot)}, ")
            elif keys_only:
                _slot_str += (f"{slot}, ")
            else:
                _slot_str += (f"{slot}={getattr(self, slot)}, ")
        return _slot_str[:-2]

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
        """Return an iterator for the object.

        Returns:
            Iterator: An iterator for the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            for item in base_interface_example:
                print(item)
            >>> "test"
        """
        for slot in self.__slots__:
            yield getattr(self, slot)

    def hash_items(self) -> List[str]:
        """Return the hash of the object.

        Returns:
            List[str]: The hash of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.hash_items())
            >>> ["6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f"]
        """
        attribute_hashes: List[str] = []
        for attribute in self.__iter__():
            attribute_hashes.append(MerkleTree.hash_func(repr(attribute)))
        return attribute_hashes

    def hash_tree(self) -> MerkleTree:
        """Return the hash of the object.

        Returns:
            MerkleTree: The hash tree of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.hash_tree())
            >>> "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f"
        """
        return MerkleTree(hashed_data=self.hash_items())

    def hash_sha256(self) -> str:
        """Return the hash tree of the object.

        Returns:
            MerkleTree: The hash tree of the object.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.hash_sha256())
            >>> "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f"
        """
        return self.hash_tree().root()
    
    def contains_item(self, item: Any) -> bool:
        """Return whether the object contains the item.

        Args:
            item (Any): The item to check.

        Returns:
            bool: Whether the object contains the item.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.contains_item("test"))
            >>> True
        """
        if item in self.__iter__():
            return True
        return False

    @property
    def __weakref__(self):
        """Return the weak reference of the object.

        Returns:
            Any: The weak reference of the object.
        """
        raise NotImplementedError

    # def contains_hash(self, hash: str) -> bool:
    #     """Return whether the object contains the hash.

    #     Args:
    #         hash (str): The hash to check.

    #     Returns:
    #         bool: Whether the object contains the hash.

    #     Example::

    #         @define(slots=True, frozen=True, weakref_slot=False)
    #         class InterfaceExample(BaseInterface):
    #             example: str = field(validator=validators.instance_of(str))

    #         base_interface_example = InterfaceExample("test")
    #         print(base_interface_example.contains_hash("test"))
    #         >>> True
    #     """
    #     return self.hash_tree().verify(hash)

