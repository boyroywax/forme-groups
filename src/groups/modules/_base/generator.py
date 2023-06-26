from typing import Optional, List

from .type import Type
from .system_types import SystemTypes
from .value import Value


class Generator():
    """
    
    """

    _suffix: Optional[str] = None
    _prefix: Optional[str] = None
    _separator: Optional[str] = None
    _super: Optional[Type] = None

    def __init__(
        self,
        super: Optional[Type] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        separator: Optional[str] = None
    ) -> None:
        """
        Initializes the Generator class.
        """
        if super is not None:
            self.set_super(super)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if separator is not None:
            self.set_separator(separator)

    def set_super(self, super: Type) -> None:
        """
        Sets the super.
        """
        self._super = super

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

    def set_separator(self, separator: str) -> None:
        """
        Sets the separator.
        """
        self._separator = separator

    def get_super(self) -> Type:
        """
        Gets the super.
        """
        return self._super

    def get_suffix(self) -> str:
        """
        Gets the suffix.
        """
        if self._suffix is None:
            return self._super.get_suffix()
        else:
            return self._suffix + self._super.get_suffix()
        
    def get_prefix(self) -> str:
        """
        Gets the prefix.
        """
        if self._prefix is None:
            return self._super.get_prefix()
        else:
            return self._prefix + self._super.get_prefix()
        
    def get_separator(self) -> str:
        """
        Gets the separator.
        """
        if self._separator is None:
            return self._super.get_separator()
        else:
            return f'{self._separator}'
        
    def generate(self, value: Value) -> str:
        """
        
        """


