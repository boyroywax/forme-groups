from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Type_():
    """
    
    """
    _id: str
    _alias: Optional[List[str]] = None
    _prefix: Optional[str] = None
    _suffix: Optional[str] = None
    _separator: Optional[str] = None

    def __init__(
        self,
        id: str,
        alias: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        separator: Optional[str] = None
    ) -> None:
        """
        Initializes the Type_ class.
        """
        self.set_id(id)

        if alias is not None:
            self.set_alias(alias)

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
    
    

@dataclass
class SystemType_():
    """
    System Class
    """
    
    _id: str


    def __init__(
        self,
        id: str,
        alias: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        separator: Optional[str] = None,
        args: Optional[List[str]] = None,
        kwargs: Optional[Dict[str]] = None
    ) -> None:
        """
        Initializes the SystemType_ class.
        """
        self.set_id(id)

        if alias is not None:
            self.set_alias(alias)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if separator is not None:
            self.set_separator(separator)

        if args is not None:
            self.set_args(args)

        if kwargs is not None:
            self.set_kwargs(kwargs)
