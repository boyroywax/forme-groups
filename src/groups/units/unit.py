import json
from dataclasses import dataclass, field
from typing import Optional, Dict

from .value import Value_ as UnitValue
from .type import Type_ as UnitType

_DEFAULT_SYSTEM_SUPER_TYPE = UnitType(
    id_=UnitValue('string'),
    alias_=UnitValue('str'),
    system_function_=str
)

_DEFAULT_SYSTEM_TYPES: Dict[str, UnitType] = {
    'string': _DEFAULT_SYSTEM_SUPER_TYPE,
    'integer': UnitType(
        id_=UnitValue('integer'),
        alias_=UnitValue('int'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=int
    ),
    'float': UnitType(
        id_=UnitValue('float'),
        alias_=UnitValue('flt'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=float
    ),
    'boolean': UnitType(
        id_=UnitValue('boolean'),
        alias_=UnitValue('bool'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=bool
    ),
    'list': UnitType(
        id_=UnitValue('list'),
        alias_=UnitValue('lst'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=list
    ),
    'dictionary': UnitType(
        id_=UnitValue('dictionary'),
        alias_=UnitValue('dict'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=dict
    ),
    'tuple': UnitType(
        id_=UnitValue('tuple'),
        alias_=UnitValue('tup'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=tuple
    ),
    'set': UnitType(
        id_=UnitValue('set'),
        alias_=UnitValue('st'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=set
    ),
    'frozenset': UnitType(
        id_=UnitValue('frozenset'),
        alias_=UnitValue('fset'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=frozenset
    ),
    'bytes': UnitType(
        id_=UnitValue('bytes'),
        alias_=UnitValue('bts'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=bytes
    ),
    'bytearray': UnitType(
        id_=UnitValue('bytearray'),
        alias_=UnitValue('barr'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=bytearray
    ),
    'memoryview': UnitType(
        id_=UnitValue('memoryview'),
        alias_=UnitValue('mview'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=memoryview
    ),
    'none': UnitType(
        id_=UnitValue('none'),
        alias_=UnitValue('none'),
        super_=_DEFAULT_SYSTEM_SUPER_TYPE,
        system_function_=None
    )
}


@dataclass
class Unit():
    value: UnitValue = field(default_factory=UnitValue())
    type_: UnitType = field(default_factory=UnitType())

    def __init__(
        self,
        value_: Optional[UnitValue] = None,
        type_: Optional[UnitType] = None
    ) -> None:
        """
        Initializes the Unit class.
        """
        if value_ is not None:
            self.set_value_obj(value_)

        if type_ is not None:
            self.set_type_obj(type_)

    def set_value_obj(self, value_: UnitValue) -> None:
        """
        Sets the value of the unit.
        """
        self.value = UnitValue(value_)

    def set_type_obj(self, type_: UnitType) -> None:
        """
        Sets the type of the unit.
        """
        if type_ not in _DEFAULT_SYSTEM_TYPES.values():
            self.type_ = type_
        else:
            raise ValueError(f'Cannot set type to system type {type_.id_}')

    def create_and_set_value(self, value: str, super_type: Optional[str] = None) -> None:
        """
        Creates and sets the value of the unit.
        """
        self.set_value_obj(UnitValue(value, super_type))

    def create_and_set_value_from_dict(self, value_dict: dict) -> None:
        """
        Creates and sets the value of the unit from the given dictionary.
        """
        self.set_value_obj(UnitValue.from_dict(value_dict))

    def create_and_set_value_from_json(self, value_json: str) -> None:
        """
        Creates and sets the value of the unit from the given JSON.
        """
        self.set_value_obj(UnitValue.from_json(value_json))

    def create_and_set_type(self, type_: str) -> None:
        """
        Creates and sets the type of the unit.
        """
        self.set_type_obj(UnitType(type_))

    def create_and_set_type_from_dict(self, type_dict: dict) -> None:
        """
        Creates and sets the type of the unit from the given dictionary.
        """
        self.set_type_obj(UnitType.from_dict(type_dict))

    def create_and_set_type_from_json(self, type_json: str) -> None:
        """
        Creates and sets the type of the unit from the given JSON.
        """
        self.set_type_obj(UnitType.from_json(type_json))

    def get_value_obj(self) -> UnitValue:
        """
        Gets the value of the unit.
        """
        return self.value

    def get_type_obj(self) -> UnitType:
        """
        Gets the type of the unit.
        """
        return self.type_

    def get_value(self) -> str:
        """
        Gets the value of the unit.
        """
        return self.get_value_obj().to_json()

    def get_type(self) -> str:
        """
        Gets the type of the unit.
        """
        return self.get_type_obj().to_json()

    def to_dict(self) -> dict:
        """
        Returns the dictionary representation of the unit.
        """
        return {
            "value": self.get_value(),
            "type": self.get_type(),
        }

    def to_json(self) -> str:
        """
        Returns the JSON representation of the unit.
        """
        return json.dumps(self.to_dict())

    def __str__(self) -> str:
        """
        Returns the string representation of the unit.
        """
        return self.to_json()

    def __repr__(self) -> str:
        """
        Returns the string representation of the unit.
        """
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        """
        Returns whether the unit is equal to the other.
        """
        if not isinstance(other, Unit):
            return NotImplemented

        return (
            self.get_value() == other.get_value() and
            self.get_type() == other.get_type()
        )

    def __ne__(self, other: object) -> bool:
        """
        Returns whether the unit is not equal to the other.
        """
        if not isinstance(other, Unit):
            return NotImplemented

        return (
            self.get_value() != other.get_value() or
            self.get_type() != other.get_type()
        )

    @staticmethod
    def from_dict(unit_dict: dict) -> "Unit":
        """
        Generates a unit from the given dictionary.
        """
        return Unit(
            UnitValue.from_dict(unit_dict["value"]),
            UnitType.from_dict(unit_dict["type"])
        )

    @staticmethod
    def from_json(unit_json: str) -> "Unit":
        """
        Generates a unit from the given JSON.
        """
        return Unit.from_dict(json.loads(unit_json))
