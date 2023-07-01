import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(
    slots=True,
)
class SuperUnit:
    """
    The super unit class for all units.
    * Units can be initialized as a 'value'.
    * Units can be initialized as NoneType.
    * Units can be initialized as a random value.
    * Units can be initialized from a 'dictionary'.
    """

    value: Any = field(default=Any, init=True, repr=True, compare=True, hash=True, metadata=None)

    def __init__(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Initializes the Super Unit class and sets the value.
        """
        self.parse_input(*args, **kwargs)

    def parse_input(self, *args, **kwargs) -> None:
        """
        Parses the input.
        """

        # Check if 'random' kwarg and 'value' arg are set at the same time.
        if (
            len(args) == 1 and
            "random" in kwargs and
            kwargs["random"] is True
        ):
            raise ValueError("Cannot set 'random' and 'value' at the same time.")

        # Check if 'value' kwarg and 'value' kwarg are set at the same time.
        if (
            "random" in kwargs and
            "value" in kwargs
        ):
            raise ValueError("Cannot set 'random' and 'value' at the same time.")

        # Check if 'value' kwarg and 'value' arg are set at the same time.
        if (
            len(args) >= 1 and
            "value" in kwargs
        ):
            raise ValueError("Cannot set 'value' and pass a value at the same time.")

        # Check if 'args' is a dictionary with a value entry.
        if (
            len(args) == 1 and
            isinstance(args[0], dict) and
            dict(args[0]).get("value") is not None and 
            "random" not in kwargs and
            "value" not in kwargs
        ):
            self.value = dict(args[0]).get("value")
            return

        # Check if 'kwargs' contains the random key and that the value is set to True.
        if (
            len(args) == 0 and
            "random" in kwargs and
            kwargs["random"] is True and
            "value" not in kwargs
        ):
            self.value = self.random_value()
            return

        # Check if 'kwargs' contains the random key and that it is set to False.
        if (
            len(args) == 0 and
            "random" in kwargs and
            kwargs["random"] is False
        ):
            self.value = None
            return

        # Check for an empty input.
        if (
            len(args) == 0 and
            "random" not in kwargs and
            "value" not in kwargs
        ):
            self.value = None
            return

        # Check if 'kwargs' contains the value key. And that the value is not None.
        if (
            len(args) == 0 and
            "value" in kwargs and
            kwargs["value"] is not None
            and "random" not in kwargs
        ):
            self.value = kwargs["value"]
            return

        # Check if 'args' contains a value. And that 'kwargs' does not contain and keys.
        if (
            len(args) == 1 and
            "random" not in kwargs and
            "value" not in kwargs
        ):
            self.value = args[0]
            return

        # Check if 'args' contains a value. And that 'kwargs' contains the random key and that it is set to False.
        if (
            len(args) == 1 and
            "random" in kwargs and
            kwargs["random"] is False
        ):
            self.value = args[0]
            return

    def has_type(self, type_: Any) -> bool:
        """
        Returns True if the value has the type.
        """
        return isinstance(self.value, type_)

    def force_type(self, type_: Any) -> None:
        """
        Forces the value to be a type.
        """
        if not self.has_type(type_):
            self.value = type_(self.value)

    @staticmethod
    def random_value():
        """
        Returns a random value.
        """
        return uuid.uuid4().hex

    def get_type(self):
        """
        Returns the name of the value's type.
        """
        return type(self.value).__name__

    @staticmethod
    def from_dict(dictionary: Dict[str, Any]):
        """
        Returns a Super Unit from a dictionary.
        """
        return SuperUnit(
            value=dictionary["value"]
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary from a Super Unit.
        """
        return {
            "value": self.value
        }


@dataclass(
    slots=True,
)
class SchemaEntry:
    level: int
    schema: Dict[str, Any] = field(default_factory=dict)
    types: Dict[str, Any] = field(default_factory=dict)
    functions: Dict[str, Any] = field(default_factory=dict)
    overrides: Dict[str, Any] = field(default_factory=dict)


@dataclass(
    slots=True,
)
class Schema:
    """
    A Super Schema class to control the system of group objects and their units.
    """

    _schema: Optional[List[SchemaEntry]] = None

    def __init__(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Initializes the Super Schema class.
        """

        SUPER_SCHEMA: SchemaEntry = SchemaEntry(
            #  
            # The individual supported system types.
            # Super Units have no value field.
            # Super Units are used to store the system types.
            #
            level=0,
            schema={
                "system_types_schema": [Any],
                "default_super_type_schema": {
                    "id_": List[Any],
                    "aliases": List[Any],
                    "accepts": List[Any],
                    "sys_function": List[Any],
                }
            },
            types={
                "expected_system_types": [str, int, float, bool, list, dict, tuple, bytes],
                "default_super_types": [
                    {"id_": ["__RESERVED_STR__"], "aliases": ["string", "str"], "accepts": [Any], "sys_function": [str]},
                    {"id_": ["__RESERVED_INT__"], "aliases": ["integer", "int"], "accepts": [Any], "sys_function": [int]},
                    {"id_": ["__RESERVED_FLOAT__"], "aliases": ["float"], "accepts": [Any], "sys_function": [float]},
                    {"id_": ["__RESERVED_BOOL__"], "aliases": ["boolean", "bool"], "accepts": [Any], "sys_function": [bool]},
                    {"id_": ["__RESERVED_LIST__"], "aliases": ["list"], "accepts": List[Any], "sys_function": [list]},
                    {"id_": ["__RESERVED_DICT__"], "aliases": ["dictionary", "dict"], "accepts": [Any], "sys_function": [dict]},
                    {"id_": ["__RESERVED_TUPLE__"], "aliases": ["tuple"], "accepts": [Any], "sys_function": [tuple]},
                    {"id_": ["__RESERVED_BYTES__"], "aliases": ["bytes"], "accepts": [Any], "sys_function": [bytes]},
                ]
            },
            functions={
                "default_system_level_functions": [
                    {"get_expected_system_types(expected_system_types)": "Checks for the expected_system_types. Returns a list of expected system types."},
                    {"check_supported_system_types(expected_system_types)":  "Checks for support of the expected_system_types by the system. Returns a list of supported system types."},
                    {"check_supported_super_types(supported_system_types, default_system_types)": "Checks for the supported super types. Compares the default system types to the supported super types."},
                    {"get_super_types()": "Returns a list of the *supported_super_types*."},
                ]
            },
            overrides={
                # Example (Simplified System Types)
                "expected_system_types": [str, int, float],
                "default_super_types": [
                    {"id_": ["str"], "aliases": ["string", "str"], "accepts": [Any], "sys_function": [str]},
                    {"id_": ["int"], "aliases": ["integer", "int"], "accepts": [Any], "sys_function": [int]},
                ]
            }
        )
        
        BASE_SCHEMA: SchemaEntry = SchemaEntry(
            #
            # The default and custom defined base types.
            # Base Units have a value field.
            # Base Units are used to store a value, and the supported super types.
            #
            level=1,
            schema={
                "default_base_schema": {
                    "id_": List[Any],
                    "aliases": List[Any],
                    "super_base": ["*supported_super_types*"],
                    "accepts": List[Any],
                    "prefix": List[Any],
                    "suffix": List[Any],
                    "separator": List[Any],
                    "base_function": List[Any],
                }
            },
            types={
                "default_base_types": [
                    # The String Base Type Unit can accept any system type.
                    # Each __RESERVED__XXX__  super unit can only be used on a single base unit.
                    # Base Units cannot share super units.  But, base units can inherit super units from other base units by stacking them.
                    {"id_": ["str"], "aliases": ["string", "str"], "super_base": ["__RESERVED__STR__"], "accepts": ["*all_supported_super_types*"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["int"], "aliases": ["integer", "int"], "super_base": ["__RESERVED__INT__"], "accepts": ["__RESERVED__INT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["float"], "aliases": ["float"], "super_base": ["__RESERVED__FLOAT__"], "accepts": ["__RESERVED__FLOAT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["bool"], "aliases": ["boolean", "bool"], "super_base": ["__RESERVED__BOOL__"], "accepts": ["__RESERVED__BOOL__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["list"], "aliases": ["list"], "super_base": ["__RESERVED__LIST__"], "accepts": ["__RESERVED__LIST__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["dict"], "aliases": ["dictionary", "dict"], "super_base": ["__RESERVED__DICT__"], "accepts": ["__RESERVED__DICT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["tuple"], "aliases": ["tuple"], "super_base": ["__RESERVED__TUPLE__"], "accepts": ["__RESERVED__TUPLE__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["bytes"], "aliases": ["bytes"], "super_base": ["__RESERVED__BYTES__"], "accepts": ["__RESERVED__BYTES__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    
                    # Base Units can be stacked.
                    # Stacking a Base Unit ontop of another Base Unit will inherit the super_base of the Base Unit it is stacked ontop of.
                    # Accepted types can be defined for a stacked Base Unit, but the accepted types must be a subset of the accepted types of the Base Unit it is stacked ontop of.
                    # Lets declare a DID Base Type Unit.]
                    # The DID Base Type Unit stacks ontop of String Base Type Unit.
                    # This will be used to store a DID or VC starting with 'did:'
                    {"id_": ["did"], "aliases": ["did"], "super_base": ["str"], "accepts": ["str"], "prefix": ["did:"], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            },
            functions={
                "default_base_level_functions": [
                    {"prepare_base_types()": "Prepares the base types for use."},
                    {"create_base_type(id_, aliases, super_base, accepts, prefix, suffix, separator, base_function)": "Creates a base type."},
                    {"get_base_types()": "Returns a list of the *supported_base_types*."},
                    {"get_base_type(id_)": "Returns the base type for the given id_."},
                    {"get_base_type_by_alias(alias)": "Returns the base type for the given alias."},
                    {"get_base_type_by_super_base(super_base)": "Returns the base type for the given super base."},
                    {"get_base_type_by_accepts(accepts)": "Returns the base type for the given accepts."},
                    {"get_base_type_by_prefix(prefix)": "Returns the base type for the given prefix."},
                    {"get_base_type_by_suffix(suffix)": "Returns the base type for the given suffix."},
                    {"get_base_type_by_separator(separator)": "Returns the base type for the given separator."},
                    {"get_base_type_by_base_function(base_function)": "Returns the base type for the given base function."},
                    {"get_base_type_by_id_or_alias(id_or_alias)": "Returns the base type for the given id_ or alias."},
                ]
            },
            overrides={
                # Generally, the default base types should not be overridden. 
                # Instead, new base types should be created that inherit from the default base types.
                "custom_base_types": [
                    # Example (Simplified Base Types)
                    {"id_": ["text"], "aliases": ["text"], "super_base": ["str"], "accepts": ["str"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["number"], "aliases": ["number"], "super_base": ["int", "float"], "accepts": ["int", "float"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            }
        )

        GROUP_SCHEMA = SchemaEntry(
            #
            # Group Schema
            #
            level=2,
            schema={
                # Inherits from the default base unit schema.
                "default_unit_type_schema": {
                    "id_": List[Any],
                    "aliases": List[Any],
                    "super_base": List[Any],
                    "accepts": List[Any],
                    "prefix": Optional[Any],
                    "suffix": Optional[Any],
                    "separator": Optional[Any],
                    "base_function": Optional[Any]
                },
                # A new schema that defines the default group unit types.
                "default_group_unit_type_schema": {
                    "nonce_chain": ["nonce"],
                    "owners": ["owner"],
                    "creds": ["credential"],
                    "data": ["data"]
                },
                "default_group_type_schema": {
                    "group_id": ["str"],
                    "items": ["default_group_unit_type_schema"],
                }
            },
            types={
                "default_group_unit_types": [
                    # If the group type has a super_base that contains a "prefix", "suffix", "separator", or "base_function", the "accepts" value defines the types that can be passed to the unit.
                    # For ex
                    {"id_": ["nonce"], "aliases": ["nonce"], "super_base": ["str", 'int'], "accepts": ["str, int"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["nonce_chain"], "aliases": ["nonce_chain"], "super_base": ["list"], "accepts": ["nonce"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["owner"], "aliases": ["owner"], "super_base": ["did"], "accepts": ["did"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["owners"], "aliases": ["owners"], "super_base": ["list"], "accepts": ["owner"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["credential"], "aliases": ["credential, cred"], "super_base": ["did"], "accepts": ["did"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["credentials"], "aliases": ["credentials, creds"], "super_base": ["list"], "accepts": ["credential"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["data_entry"], "aliases": ["data_entry", "data"], "super_base": ["*all_supported_base_types*"], "accepts": ["*all_supported_base_types"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["data"], "aliases": ["data"], "super_base": ["dict"], "accepts": ["data_entry"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["group_unit"], "aliases": ["group_unit, unit"], "super_base": ["dict"], "accepts": ["nonce_chain", "owners", "creds", "data"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["group"], "aliases": ["group"], "super_base": ["dict"], "accepts": ["group_unit"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            },
            functions={
                "default_group_level_functions": [
                    {"create_group_unit": "Creates a group unit."},
                    {"create_group": "Creates a group."},
                    {"add_group_unit_to_group": "Adds a group unit to a group."},
                    {"remove_group_unit_from_group": "Removes a group unit from a group."},
                    {"get_group_unit_from_group": "Gets a group unit from a group."},
                    {"get_group_units_from_group": "Gets all group units from a group."},
                ]
            },
            overrides={
                # Generally, the default group unit types should not be overridden.
                # Instead, new group unit types should be created that inherit from the default group unit types.
                "custom_group_unit_types": [
                    # Example (Creating a group with a custom group unit type)
                    {"id_": ["my_custom_group_value"], "aliases": ["my_custom_group_value"], "super_base": ["str"], "accepts": ["str"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["custom_group_unit"], "aliases": ["custom_group_unit"], "super_base": ["group_unit"], "accepts": ["group_unit", "my_custom_group_value"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            }
        )

        self._schema = [
            SUPER_SCHEMA,
            BASE_SCHEMA,
            GROUP_SCHEMA
        ]
        
