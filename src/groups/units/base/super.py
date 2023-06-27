from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Callable

_DEFAULT_SUPER_TYPES: Dict[str, Callable] = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "bytes": bytes,
}


@dataclass
class Super__():
    """
    Manages the super of the value object.
    """
    _super__: Optional[Callable] = None

    def __init__(
        self,
        _super__: Optional[Callable] = None
    ) -> None:
        """
        Initializes the Super__ class.
        """
        self.check_and_set_super(_super__)

    def check_for_none(self, super: Any) -> bool:
        """
        Checks if the super of the value object is valid.
        """
        if super is not None:
            return True
        else:
            return False

    def check_for_type(self, super: Any) -> bool:
        """
        Checks if the super of the value object is valid.
        """
        if super in _DEFAULT_SUPER_TYPES.values():
            return True
        else:
            return False
        
    def check_for_type_name(self, super: Any) -> bool:
        """
        Checks if the super of the value object is valid.
        """
        if str(super) in _DEFAULT_SUPER_TYPES.keys():
            return True
        else:
            return False

    def get_type_from_str_name(self, super: Any) -> Callable:
        """
        Gets the type from the string name.
        """
        if type(super).__name__ in _DEFAULT_SUPER_TYPES.keys():
            return _DEFAULT_SUPER_TYPES[type(super).__name__]
        
        if super in _DEFAULT_SUPER_TYPES.keys():
            return _DEFAULT_SUPER_TYPES[super]

    def set_super(self, _super__: Any) -> None:
        """
        Sets the super of the value object.
        """
        self._super__ = _super__

    def check_and_set_super(self, _super__: Any) -> None:
        """
        Checks and sets the super of the value object.
        """

        if self.check_for_none(_super__) and self.check_for_type_name(_super__):
            if self.check_for_type(_super__):
                self.set_super(_super__)
            else:
                callable = self.get_type_from_str_name(_super__)
                if callable is not None:
                    self.set_super(callable)
                else:
                    raise TypeError(f"Invalid type for super: {_super__}")
        elif not self.check_for_none(_super__) and self.check_for_type(_super__):
            self.set_super(str)
        else:
            callable = self.get_type_from_str_name(_super__)
            # raise TypeError(f"Invalid super: {_super__}")
            self.set_super(callable)

    def get_super(self) -> Any:
        """
        Gets the super of the value object.
        """
        return self._super__
    
    def __str__(self) -> str:
        """
        Converts the value object to a string.
        """
        return f"{type(self._super__).__name__}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the value object to a dictionary.
        """
        return {
            "_super__": self.__str__()
        }