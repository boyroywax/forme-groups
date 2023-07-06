from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


class SchemaEntryPropertyInterface(ABC):
    """
    The interface for the Level class.
    """
    @property
    @abstractmethod
    def value(self) -> Any:
        pass


@dataclass(
    init=False,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=True,
    frozen=True,
    match_args=True,
    kw_only=False,
    slots=True,
    weakref_slot=False
)
class SchemaEntryProperty(SchemaEntryPropertyInterface):
    """
    The SchemaEntryProperty class.
    * The SchemaEntryProperty class is used to store the value of a SchemaEntry.
    """

    _value: Any = field(
        default=None,
        init=False,
        repr=False,
        compare=False,
        hash=False,
        metadata=None
    )                          

    def __init__(
        self,
        value: Any
    ) -> None:
        """
        Initializes the Level class.
        """
        self._value = value

    @property
    def value(self) -> Any:
        """
        The value of the SchemaEntryProperty.
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Sets the value of the SchemaEntryProperty.
        """
        self._value = value

    @value.deleter
    def value(self) -> None:
        """
        Deletes the value of the SchemaEntryProperty.
        """
        del self._value

    @value.getter
    def value(self) -> Any:
        """
        Gets the value of the SchemaEntryProperty.
        """
        return self._value
