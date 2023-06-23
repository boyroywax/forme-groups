from typing import Dict, Optional, List, Callable

from groups.modules._base.generator import Generator


class Type():
    """

    """

    _parent: Optional[List[str]] = None
    _type: Optional[str] = None
    _descriptors: Optional[List[str]] = None
    _prefix: Optional[str] = None
    _suffix: Optional[str] = None
    _seperator: Optional[str] = None
    _generator: Optional[Generator] = None

    def __init__(
        self,
        parent: Optional[List[str]] = None,
        type: Optional[str] = None,
        descriptors: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        seperator: Optional[str] = None,
        generator: Optional[Generator] = None,
    ) -> None:
        """
        Initializes the BaseType class.
        """
        if parent is not None:
            self.set_parent(parent)

        if type is not None:
            self.set_type(type)

        if descriptors is not None:
            self.set_descriptors(descriptors)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if seperator is not None:
            self.set_seperator(seperator)

        if generator is not None:
            self.set_custom_generator(generator)

    def set_parent(self, parent: List[str]) -> None:
        """
        Sets the parent.
        """
        self._parent = parent

    def set_type(self, type: str) -> None:
        """
        Sets the type.
        """
        self._type = type

    def set_descriptors(self, descriptors: List[str]) -> None:
        """
        Sets the descriptors.
        """
        self._descriptors = descriptors

    def set_prefix(self, prefix: str) -> None:
        """
        Sets the prefix.
        """
        self._prefix = prefix

    def set_suffix(self, suffix: str) -> None:
        """
        Sets the suffix.
        """
        self._suffix = suffix

    def set_seperator(self, seperator: str) -> None:
        """
        Sets the seperator.
        """
        self._seperator = seperator

    def set_generator(self, generator: Callable) -> None:
        """
        Sets the generator.
        """
        self._generator = generator

    
