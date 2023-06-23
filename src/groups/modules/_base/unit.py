
from typing import Optional

from groups.modules._base.value import Value
from groups.modules._base.type import Type



class Unit():
    """
    
    """
    _value: Optional[Value] = None
    _type: Optional[Type] = None

    def __init__(
        self,
        value: Optional[Value] = None,
        type: Optional[Type] = None
    ) -> None:
        """
        Constructor for the Unit class.
        """
        assert value is not None
        assert type is not None

        self.set_value(value)
        self.set_type(type)

    def set_value(self, value: Value) -> None:
        """
        Sets the value.
        """
        self._value = value

    def set_type(self, type: Type) -> None:
        """
        Sets the type.
        """
        self._type = type

    def get_value(self) -> Value:
        """
        Returns the value.
        """
        return self._value
    
    def get_type(self) -> Type:
        """
        Returns the type.
        """
        return self._type
    
    def get_parent_type(self) -> Optional[Type]:
        """
        Returns the parent type.
        """
        return self._type.get_parent_type()

