from dataclasses import dataclass
from typing import List, Optional

from . import Type_ as BaseType
from .id import Id
from .alias import Alias
from .super import Super
from .prefix import Prefix
from .suffix import Suffix
from .separator import Separator
from .function import Function
from .checks import Checks


@dataclass
class Defaults:
    """
    Manages the defaults of the base type object.
    """
    types: Optional[List[BaseType]] = None

    def __post_init__(self):
        if self.types is None:
            self.types = list()

    def add(self, type: BaseType) -> None:
        """
        Adds a type to the defaults.
        """
        self.types.append(type)

    def remove(self, type: BaseType) -> None:
        """
        Removes a type from the defaults.
        """
        self.types.remove(type)

    def clear(self) -> None:
        """
        Clears the defaults.
        """
        self.types.clear()

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

            for type_ in self.types:
                if Checks.check_supported_system_type(type_.function_.value) is False:
                    print(f"Removing unsupported type: {type_.function_.value}")
                    self.remove(type_)

    def generate_defaults(self) -> List[BaseType]:
        """
        Generates the defaults for the base type object.
        """
        string_type: BaseType = BaseType(
            id_=Id(value="string"),
            alias=Alias(value=["string", "str"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function_=Function(value=str)
        )

        integer_type: BaseType = BaseType(
            id_=Id(value="integer"),
            alias=Alias(value=["integer", "int"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function_=Function(value=int)
        )

        float_type: BaseType = BaseType(
            id_=Id(value="float"),
            alias=Alias(value=["float"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function_=Function(value=float)
        )

        boolean_type: BaseType = BaseType(
            id_=Id(value="boolean"),
            alias=Alias(value=["boolean", "bool"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(),
            suffix=Suffix(),
            separator=Separator(),
            function_=Function(value=bool)
        )

        list_type: BaseType = BaseType(
            id_=Id(value="list"),
            alias=Alias(value=["list"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(value="["),
            suffix=Suffix(value="]"),
            separator=Separator(value=","),
            function_=Function(value=list)
        )

        tuple_type: BaseType = BaseType(
            id_=Id(value="tuple"),
            alias=Alias(value=["tuple"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(value="("),
            suffix=Suffix(value=")"),
            separator=Separator(value=","),
            function_=Function(value=tuple)
        )

        dictionary_type: BaseType = BaseType(
            id_=Id(value="dictionary"),
            alias=Alias(value=["dictionary", "dict"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(value="{"),
            suffix=Suffix(value="}"),
            separator=Separator(value=","),
            function_=Function(value=dict)
        )

        bytes_type: BaseType = BaseType(
            id_=Id(value="bytes"),
            alias=Alias(value=["bytes"]),
            super_=Super(value="RESERVED"),
            prefix=Prefix(value="b'"),
            suffix=Suffix(value="'"),
            separator=Separator(),
            function_=Function(value=bytes)
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

