import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .generator import TypeGenerator



_DEFUALT_UNIT_TYPE: Dict[str, Optional[List[str]]] = {
    "unit_type": "string",
    "unit_type_descriptors": ["string", "str"],
    "unit_type_prefix": None,
    "unit_type_suffix": None,
    "unit_type_separator": None,
}


@dataclass(
    init=False,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
    match_args=True,
    kw_only=False,
    slots=False,
    weakref_slot=False
)
class BaseUnitType():
    """
    The BaseUnitType class manages the individial unit type.
    """

    _unit_type: str = _DEFUALT_UNIT_TYPE
    _unit_type_descriptors: List[str] = field(default_factory=list)
    # _unit_type_prefix: Optional[str] = None
    # _unit_type_suffix: Optional[str] = None
    # _unit_type_separator: Optional[str] = None
    _unit_type_generator: Optional[TypeGenerator] = None

    def __init__(
            self,
            super_unit_type: Optional[str] = None,
            name: Optional[str] = None,
            descriptors: Optional[List[str]] = None,
            prefix: Optional[str] = None,
            suffix: Optional[str] = None,
            separator: Optional[str] = None,
    ) -> None:
        """
        Initializes the BaseUnitType class.
        If no unit type is provided, the default unit type is used.
        """
        if unit_type_name is not None:
            self.set_unit_type(unit_type)
        else:
            self.set_unit_type(_DEFUALT_UNIT_TYPE)

        if unit_type_descriptors is not None:
            self.set_unit_type_descriptors(unit_type_descriptors)

        if (
            (unit_type_prefix is not None) or
            (unit_type_suffix is not None) or
            (unit_type_separator is not None)
        ):
            self._unit_type_generator = TypeGenerator(
                super_unit_type=super_unit_type,
                unit_type_prefix=unit_type_prefix,
                unit_type_suffix=unit_type_suffix,
                unit_type_separator=unit_type_separator,
            )
        #     self.set_unit_type_prefix(unit_type_prefix)

        # if unit_type_suffix is not None:
        #     self.set_unit_type_suffix(unit_type_suffix)

    def get_unit_type(self) -> List[str]:
        """
        Returns the unit type.
        """
        return self._unit_type

    def get_unit_type_descriptors(self) -> List[str]:
        """
        Returns the unit type.
        """
        return self._unit_type_descriptors
    
    def get_unit_type_prefix(self) -> Optional[str]:
        """
        Returns the unit type prefix.
        """
        return self._unit_type_prefix

    def get_unit_type_suffix(self) -> Optional[str]:
        """
        Returns the unit type suffix.
        """
        return self._unit_type_suffix

    def set_unit_type(self, unit_type: str) -> None:
        """
        Sets the unit type.
        """
        self._unit_type = unit_type

    def set_unit_type_descriptors(self, unit_type_descriptors: Optional[List[str]] = None) -> None:
        """
        Sets the unit type descriptors.
        If no unit type descriptors are provided, the unit_type is used.
        """
        try:
            if unit_type_descriptors is None:
                self._unit_type_descriptors = [self.unit_type]
            else:
                self._unit_type_descriptors = unit_type_descriptors
        except AttributeError:

    def create_generator

    # def set_unit_type_prefix(self, unit_type_prefix: str) -> None:
    #     """
    #     Sets the unit type prefix.
    #     """
    #     self._unit_type_prefix = unit_type_prefix

    # def set_unit_type_suffix(self, unit_type_suffix: str) -> None:
    #     """
    #     Sets the unit type suffix.
    #     """
    #     self._unit_type_suffix = unit_type_suffix

    # def verify_unit_type(self, unit: str) -> bool:
    #     """
    #     Verifies that the unit is valid.
    #     """
    #     if self.verify_unit_type_prefix(unit) and self.verify_unit_type_suffix(unit):
    #         return True
    #     return False

    def to_json(self) -> Dict:
        """
        Returns the object in a JSON format.
        """
        return {
            "unit_type": self._unit_type,
            "unit_type_descriptors": self._unit_type_descriptors,
            "unit_type_prefix": self._unit_type_prefix,
            "unit_type_suffix": self._unit_type_suffix
        }

    def to_json_string(self) -> str:
        """
        Returns the object in a JSON string format.
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



# class BaseUnitTypeString(BaseUnitType):
#     """
#     The BaseUnitTypeString class manages the string unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeString class.
#         """
#         self._unit_type: str = "string"
#         self._unit_type_descriptors: List[str] = ['string', 'str']
#         self._unit_type_prefix: Optional[str] = None
#         self._unit_type_suffix: Optional[str] = None

#     def verify_unit_is_string(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         if isinstance(unit, str):
#             return True
#         return False


# class BaseUnitTypeInteger(BaseUnitTypeString):
#     """
#     The BaseUnitTypeInteger class manages the integer unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeInteger class.
#         """
#         self._unit_type: str = "integer"
#         self._unit_type_descriptors: List[str] = ['integer', 'int']
#         self._unit_type_prefix: Optional[str] = None
#         self._unit_type_suffix: Optional[str] = None

#     def verify_unit_contains_integer(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         return TypeScanners().is_integer(unit)


# class BaseUnitTypeFloat(BaseUnitTypeString):
#     """
#     The BaseUnitTypeFloat class manages the float unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeFloat class.
#         """
#         self._unit_type: str = "float"
#         self._unit_type_descriptors: List[str] = ['float']
#         self._unit_type_prefix: Optional[str] = None
#         self._unit_type_suffix: Optional[str] = None

#     def verify_unit_contains_float(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         return TypeScanners().is_float(unit)
    

# class BaseUnitTypeBoolean(BaseUnitTypeString):
#     """
#     The BaseUnitTypeBoolean class manages the boolean unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeBoolean class.
#         """
#         self._unit_type: str = "boolean"
#         self._unit_type_descriptors: List[str] = ['boolean', 'bool']
#         self._unit_type_prefix: Optional[str] = None
#         self._unit_type_suffix: Optional[str] = None

#     def verify_unit_contains_boolean(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         return TypeScanners().is_boolean(unit)
    

# class BaseUnitTypeList(BaseUnitTypeString):
#     """
#     The BaseUnitTypeList class manages the list unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeList class.
#         """
#         self._unit_type: str = "list"
#         self._unit_type_descriptors: List[str] = ['list']
#         self._unit_type_prefix: Optional[str] = "["
#         self._unit_type_suffix: Optional[str] = "]"

#     def verify_unit_contains_list(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         return TypeScanners().is_list(unit) 
    

# class BaseUnitTypeDict(BaseUnitTypeString):
#     """
#     The BaseUnitTypeDict class manages the dict unit type.
#     """

#     def __init__(self):
#         """
#         Initializes the BaseUnitTypeDict class.
#         """
#         self._unit_type: str = "dict"
#         self._unit_type_descriptors: List[str] = ['dict']
#         self._unit_type_prefix: Optional[str] = "{"
#         self._unit_type_suffix: Optional[str] = "}"

#     def verify_unit_contains_dict(self, unit: str) -> bool:
#         """
#         Verifies that the unit is valid.
#         """
#         return TypeScanners().is_dict(unit)


# class BaseUnitTypeCustom(BaseUnitTypeString):
#     """
#     The BaseUnitTypeCustom class manages a custom unit type.
#     """

#     def __init__(
#         self,
#         unit_type: str,
#         unit_type_descriptors: Optional[List[str]] = None,
#         unit_type_prefix: Optional[str] = None,
#         unit_type_suffix: Optional[str] = None
#     ):
#         """
#         Initializes the BaseUnitTypeCustom class.
#         """
#         super().__init__(
#             self._unit_type: str = unit_type
#             self._unit_type_descriptors: List[str] = unit_type_descriptors
#             self._unit_type_prefix: Optional[str] = unit_type_prefix
#             self._unit_type_suffix: Optional[str] = unit_type_suffix
#         )

