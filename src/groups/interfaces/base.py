"""



"""

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

    def __iter_all__(self, sub_item: Any = None):
        if sub_item is None:
            for item in self.__iter__():
                yield self.__iter_all__(item)
        else:
            if isinstance(item, __DEFAULT_COLLECTION_TYPES__):
                for sub_item in item:
                    yield self.__iter_all__(sub_item)
            else:
                yield item



    def hash_item(self, item: Any) -> str:
        """Return the hash of the item.

        Args:
            item (Any): The item to hash.

        Returns:
            str: The hash of the item.

        Example:
            
                @define(slots=True, frozen=True, weakref_slot=False)
                class InterfaceExample(BaseInterface):
                    example: str = field(validator=validators.instance_of(str))
    
                base_interface_example = InterfaceExample("test")
                print(base_interface_example.hash_item("test"))
                >>> "6e94a0aef218fd7aef18b257f0ba9fc33c92a2bc9788fc751868e43ab398137f"
        """
        if item in self.__iter__():
            return MerkleTree.hash_func(item)
        else:
            raise ValueError(f"Item {item} not in {self}.")

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
        attribute_hashes = []
        for item in self.__iter__():
            attribute_hashes.append(MerkleTree.hash_func(repr(item)))

        return MerkleTree(attribute_hashes)

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
        if item in self.__iter_all__():
            return True
        return False

    def contains_hash(self, hash: str) -> bool:
        """Return whether the object contains the hash.

        Args:
            hash (str): The hash to check.

        Returns:
            bool: Whether the object contains the hash.

        Example::

            @define(slots=True, frozen=True, weakref_slot=False)
            class InterfaceExample(BaseInterface):
                example: str = field(validator=validators.instance_of(str))

            base_interface_example = InterfaceExample("test")
            print(base_interface_example.contains_hash("test"))
            >>> True
        """
        return self.hash_tree().verify(hash)
