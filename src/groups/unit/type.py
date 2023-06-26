from dataclasses import dataclass
from typing import Optional, List, Dict

from 


@dataclass
class UnitType():
    """
    The Type class manages the type of the module.
    """

    _id: str
    _alias: Optional[List[str]] = None
    _super: Optional['Type'] = None
    _prefix: Optional[str] = None
    _suffix: Optional[str] = None
    _separator: Optional[str] = None

    def __init__(
        self,
        id: str,
        super: Optional['Type'] = None,
        alias: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        separator: Optional[str] = None
    ) -> None:
        """
        Initializes the 'Type' class.
        """
        self.set_id(id)

        if alias is not None:
            self.set_alias(alias)

        if super is not None:
            self.set_super(super)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if separator is not None:
            self.set_separator(separator)

    def set_id(self, id: str) -> None:
        """
        Sets the id.
        """
        self._id = id

    def set_super(self, super: 'Type') -> None:
        """
        Sets the super.
        """
        self._super = super

    def set_alias(self, alias: List[str]) -> None:
        """
        Sets the alias.
        """
        self._alias = alias

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

    def get_id(self) -> str:
        """
        Gets the id.
        """
        return self._id

    def get_super(self) -> 'Type':
        """
        Gets the super.
        """
        return self._super

    def get_suffix(self) -> Optional[str]:
        """
        Gets the suffix.
        """
        if self._suffix is None and self._super is not None:
            return self._super.get_suffix()
        elif self._super is not None:
            return self._super.get_suffix() + self._suffix
        elif self._suffix is not None:
            return self._suffix
        else:
            return None

    def get_prefix(self) -> Optional[str]:
        """
        Gets the prefix.
        """
        if self._prefix is None and self._super is not None:
            return self._super.get_prefix()
        elif self._super is not None:
            return self._prefix + self._super.get_prefix()
        elif self._prefix is not None:
            return self._prefix
        else:
            return None

    def get_separator(self) -> Optional[str]:
        """
        Gets the separator.
        """
        if self._separator is None and self._super is not None:
            return self._super.get_separator()
        elif self._super is not None:
            return self._separator + self._super.get_separator()
        elif self._separator is not None:
            return self._separator
        else:
            return ''
        
    def get_full(self) -> str:
        """
        Gets the full.
        """
        return self.get_prefix() + self.get_suffix()
    
    def get_full_with_separator(self) -> str:
        """
        Gets the full with separator.
        """
        return self.get_prefix() + self.get_separator() + self.get_suffix()
    
    def get_full_with_separator_and_super(self) -> str:
        """
        Gets the full with separator and super.
        """
        if self._super is not None:
            return self.get_prefix() + self.get_super().get_full_with_separator_and_super() + self.get_separator() + self.get_suffix()
        else:
            return self.get_prefix() + self.get_separator() + self.get_suffix()
    
    def get_full_with_super(self) -> str:
        """
        Gets the full with super.
        """
        return self.get_prefix() + self.get_super().get_full_with_super() + self.get_suffix()

    def __str__(self) -> str:
        """
        Returns the string representation.
        """
        return self.get_full()

    def __repr__(self) -> str:
        """
        Returns the string representation.
        """
        return self.get_full()

    def __eq__(self, other: 'Type') -> bool:
        """
        Returns the equality.
        """
        return self.get_full() == other.get_full()

    def __ne__(self, other: 'Type') -> bool:
        """
        Returns the inequality.
        """
        return self.get_full() != other.get_full()

    def __hash__(self) -> int:
        """
        Returns the hash.
        """
        return hash(self.get_full())