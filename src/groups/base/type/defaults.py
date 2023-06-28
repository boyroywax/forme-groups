from dataclasses import dataclass, field
from typing import List, Optional

from . import Type as BaseType
from .id import Id
from .alias import Alias
from .super import Super
from .prefix import Prefix
from .suffix import Suffix
from .separator import Separator
from .function import Function
from ._unit import Unit


@dataclass
class Defaults:
    """
    Manages the defaults of the base type object.
    """
    types: Optional[List[BaseType]] = None

    def __post_init__(self):
        if self.types is None:
            self.types = list()

    def __iter__(self):
        return iter(self.types)

    def generate(
        self,
        override_types: Optional[bool] = False,
        overrides: Optional[List[BaseType]] = None
    ):
        """
        Generates the defaults for the base type object.
        """
        if len(self.types) > 0 and override_types is (False or None):
            raise AssertionError("Existing types must be empty to generate defaults. "
                                 "Use 'override_types' to override existing types.")
        if override_types:
            if len(overrides) <= 0:
                raise ValueError("'overrides' must be provided if 'override_types' is True")
            self.types = overrides
        else:
            print("Generating Types from Defaults...")
            self.types = self.generate_defaults()

    def generate_defaults(self) -> List[BaseType]:
        """
        Generates the defaults for the base type object.
        """
        string_type: BaseType = BaseType(
            id=Id(value="string"),
            alias=Alias(value=["string", "str"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function=Function(value=str)
        )

        integer_type: BaseType = BaseType(
            id=Id(value="integer"),
            alias=Alias(value=["integer", "int"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function=Function(value=int)
        )   

        float_type: BaseType = BaseType(
            id=Id(value="float"),
            alias=Alias(value=["float"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function=Function(value=float)
        )

        boolean_type: BaseType = BaseType(
            id=Id(value="boolean"),
            alias=Alias(value=["boolean", "bool"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function=Function(value=bool)
        )

        list_type: BaseType = BaseType(
            id=Id(value="list"),
            alias=Alias(value=["list"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(value="["),
            suffix=Suffix(value="]"),
            separator=Separator(value=","),
            function=Function(value=list)
        )

        tuple_type: BaseType = BaseType(
            id=Id(value="tuple"),
            alias=Alias(value=["tuple"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(value="("),
            suffix=Suffix(value=")"),
            separator=Separator(value=","),
            function=Function(value=tuple)
        )

        dictionary_type: BaseType = BaseType(
            id=Id(value="dictionary"),
            alias=Alias(value=["dictionary", "dict"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(value="{"),
            suffix=Suffix(value="}"),
            separator=Separator(value=","),
            function=Function(value=dict)
        )

        bytes_type: BaseType = BaseType(
            id=Id(value="bytes"),
            alias=Alias(value=["bytes"]),
            super=Super(value="RESERVED"),
            prefix=Prefix(value="b'"),
            suffix=Suffix(value="'"),
            separator=Separator(),
            function=Function(value=bytes)
        )

        return [
            string_type,
            integer_type,
            float_type,
            boolean_type,
            list_type,
            tuple_type,
            dictionary_type,
            bytes_type
        ]

