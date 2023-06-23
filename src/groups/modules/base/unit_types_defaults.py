from typing import List

from .type import BaseUnitType

_DEFAULT_UNIT_TYPES_LIST: List[BaseUnitType] = [
    BaseUnitType("string", ["string", "str"]),
    BaseUnitType("integer", ["integer", "int"]),
    BaseUnitType("float", ["float"]),
    BaseUnitType("boolean", ["boolean", "bool"]),
    BaseUnitType("hexadecimal", ["hexadecimal", "hex"], "0x"),
    BaseUnitType("binary", ["binary", "bin"], "0b"),
    BaseUnitType("decimal", ["decimal", "dec"], "0d"),
    BaseUnitType("list", ["list", "lst"], "[", "]"),
    BaseUnitType("tuple", ["tuple", "tpl"], "(", ")"),
    BaseUnitType("dictionary", ["dictionary", "dict", "dct"], "{", "}")
]
