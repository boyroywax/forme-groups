from .__value import Value_
from .__type import Type_

from typing import Optional


class Unit_():
    """
    
    """
    _value: Optional[Value_] = None
    _type: Optional[Type_] = None

    def __init__(
        self,
        value: Optional[Value_] = None,
        type: Optional[Type_] = None
    ) -> None:
        """
        Constructor for the Unit class.
        """
        assert value is not None
        assert type is not None

        self.set_value(value)
        self.set_type(type)

    def set_value(self, value: Value_) -> None:
        """
        Sets the value.
        """
        self._value = value

    def set_type(self, type: Type_) -> None:
        """
        Sets the type.
        """
        self._type = type

    def get_value(self) -> Value_:
        """
        Returns the value.
        """
        return self._value
    
    def get_type(self) -> Type_:
        """
        Returns the type.
        """
        return self._type
    
    def get_parent_type(self) -> Optional[Type_]:
        """
        Returns the parent type.
        """
        return self._type.get_parent_type()
    
    def get_parent_value(self) -> Optional[Value_]:
        """
        Returns the parent value.
        """
        return self._value.get_parent_value()
