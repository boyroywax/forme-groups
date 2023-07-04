import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(
    slots=True,
)
class SuperUnit:
    """
    The super unit class for all base units.
    * Units can be initialized as a 'value'.
    * Units can be initialized as NoneType.
    * Units can be initialized as a random value.
    * Units can be initialized from a 'dictionary'.

    Example (from NoneType):
    ```Python
    unit = SuperUnit()
    unit = SuperUnit(None)
    ```

    Example (from value):
    ```Python
    unit = SuperUnit("test")
    ```

    Example (from dictionary):
    ```Python
    unit = SuperUnit({"value": "test"})
    ```

    Note: The 'value' is stored as a slot.
    """

    _value: Any = field(
        default=Any,
        init=True,
        repr=True,
        compare=True,
        hash=True,
        metadata=None)

    def __init__(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Initializes the Super Unit class and sets the value.

        Args:
            *args: The arguments to initialize the Super Unit class.
                value (Any): The value to set the unit to.
                value (Dict[str, Any]): The dictionary to set the unit to. The dictionary must contain a 'value' entry.

        Keyword Args:
            **kwargs: The keyword arguments to initialize the Super Unit class.
                random (bool): If True, a random value is set.
                value (Any): The value to set the unit to.
                force_type (str): A Callable Type. The type to force the value to.

        Raises:
            ValueError: If 'random' is True and 'value' are set at the same time.
            ValueError: If 'force_type' is set and 'value' is None and 'random' is None or False.
        """
        self._value: Any = None
        self.parse_input(*args, **kwargs)
        self.__post_init__(*args, **kwargs)

    def __post_init__(
        self,
        *args,
        **kwargs
    ) -> None:
        """
        Post initializes the Super Unit class.

        Keyword Args:
            **kwargs: The keyword arguments to post initialize the Super Unit class.
                force_type (str): A Callable Type. The type to force the value to.
                
        """
        # if (
        #     "random" in kwargs and
        #     kwargs["random"] is not None and
        #     kwargs["random"] is True and
        #     "force_type" in kwargs and
        #     kwargs["force_type"] is not None
        # ):
        #     return

        # args = list(args)
        # kwargs = dict(kwargs)

        # random = kwargs.pop("random", None)
        # force_type = kwargs.pop("force_type", None)
        # value = self.value

        # if random is not None and random is True:
        #     if self._value is not None:
        #         print('value already set')
        #     self._value = self.random_value()
        #     return
        
        # if force_type is not None and force_type is not False and value is not None:
        #     # if random is None:
        #     #     raise ValueError("Cannot force a type if the value is None.")
        #     self.value = self.force_type(force_type)
        #     return
        # if (
        #     "random" in kwargs and
        #     kwargs["random"] is not None and
        #     kwargs["random"] is True and
        #     # self.value is not None and
        #     ("force_type" in kwargs and kwargs["force_type"] is not None)
        # ):
        #     raise ValueError("Cannot set a random value if the value is not None.")
        
        # if (
        #     "random" in kwargs and
        #     kwargs["random"] is not None and
        #     kwargs["random"] is True and
        #     self.value is not None and
        #     ("force_type" in kwargs and kwargs["force_type"] is True)
        # ):
        #     return
        
        # if (
        #     "force_type" in kwargs and
        #     kwargs["force_type"] is not None and
        #     kwargs["force_type"] is not False and
        #     # self.value is not None and
        #     ("random" not in kwargs or kwargs["random"] is not None or kwargs["random"] is False)):
        #     return self.force_type(kwargs["force_type"])

        # if (
        #     "force_type" in kwargs and
        #     kwargs["force_type"] is not None and
        #     self.value is None and
        #     ("random" not in kwargs or (kwargs["random"] is None or kwargs["random"] is False))
        # ):
        #     raise ValueError("Cannot force a type if the value is None.")

    def parse_input(self, *args, **kwargs) -> None:
        """
        Parses the input.

        Args:
            *args: The arguments to parse.
                value (Any): The value to set the unit to.
                value (Dict[str, Any]): The dictionary to set the unit to. The dictionary must contain a 'value' entry.

        Keyword Args:
            **kwargs: The keyword arguments to parse.
                random (bool): If True, a random value is set.
                value (Any): The value to set the unit to.
                force_type (str): A Callable Type. The type to force the value to.

        Raises:
            ValueError: If 'random' is True and 'value' are set at the same time.
            ValueError: If 'force_type' is set and 'value' is None and 'random' is None or False.

        Note:
            The 'value' is stored as a slot.

        Example:
        ```Python
        unit = SuperUnit()
        unit = SuperUnit(None)
        unit = SuperUnit("test")
        unit = SuperUnit({"value": "test"})
        unit = SuperUnit(random=True)
        unit = SuperUnit(random=False)
        unit = SuperUnit(value="test")
        ```
        """

        args: List[Any] = list(args)
        kwargs: Dict[str, Any] = dict(kwargs)

        value: Any = None
        force_type: Any = None
        random: bool = False

        value_arg: Any = None
        value_kwarg: Any = None
        
        # collect args
        if len(args) > 0:
            value_arg = args.pop(0)

        # collect kwargs
        if "value" in kwargs:
            value_kwarg = kwargs.pop("value", None)

        if "force_type" in kwargs:
            force_type = kwargs.pop("force_type")

        if "random" in kwargs:
            random = kwargs.pop("random")

        # check if value is set
        if value_arg is not None:
            if value_kwarg is not None:
                raise ValueError("Cannot set 'value' arg and 'value' kwarg at the same time.")
            value = value_arg
        else:
            value = value_kwarg
        
        # check if value is set
        if value is not None:
            if isinstance(value, dict):
                if "value" not in value:
                    raise ValueError("Cannot set 'value' if 'value' is not in the dictionary.")
                value = value["value"]

        # check if random is set    
        if random is True:
            if value is not None:
                raise ValueError("Cannot set 'random' if 'value' is not None.")
            if force_type is not None and force_type is not False:
                value = self.random_value(force_type)
            else:
                value = self.random_value()

        self.value = value

        if force_type is not None and force_type is not False and value is not None and random is not True:
            self.value = self.force_type(force_type)

        # # Check if 'value' arg is set.
        # if len(args) == 1:
        #     value = args.pop(0)

        # # Check if 'value' kwarg is set.
        # if "value" in kwargs:
        #     if value is not None:
        #         raise ValueError("Cannot set 'value' and 'value' at the same time.")
        #     else:
        #         value = kwargs.pop("value", None)

        #     if value is not None and isinstance(value, dict):
        #         if "value" not in value:
        #             raise ValueError("Cannot set 'value' if 'value' is not in the dictionary.")
        #         value = value["value"]

        # # Check if 'random' kwarg is set.
        # if "random" in kwargs:
        #     random = kwargs.pop("random")
        #     if value is not None:
        #         if random is True:
        #             raise ValueError("Cannot set 'random' and 'value' at the same time.")
        #     else:
        #         if random is True:
        #             value = self.random_value()

        # # Check if 'force_type' kwarg is set.
        # if "force_type" in kwargs:
        #     if value is None:
        #         if kwargs["force_type"] is not False and random is None or random is False:
        #             raise ValueError("Cannot set 'force_type' if 'value' is None.")
                
        #     force_type = kwargs.pop("force_type")

        #     if force_type is not False:
        #         if value is None:
        #             raise ValueError("Cannot set 'force_type' if 'value' is None.")
                
        #         value = self.force_type(force_type)

        # self.value = value

        

            

        # Check if 'random' kwarg and 'value' arg are set at the same time.
        # if (
        #     len(args) == 1 and
        #     "random" in kwargs and
        #     kwargs["random"] is True
        # ):
        #     raise ValueError("Cannot set 'random' and 'value' at the same time.")

        # # Check if 'value' kwarg and 'value' kwarg are set at the same time.
        # if (
        #     "random" in kwargs and
        #     "value" in kwargs
        # ):
        #     raise ValueError("Cannot set 'random' and 'value' at the same time.")

        # # Check if 'value' kwarg and 'value' arg are set at the same time.
        # if (
        #     len(args) >= 1 and
        #     "value" in kwargs
        # ):
        #     raise ValueError("Cannot set 'value' and pass a value at the same time.")

        # # Check if 'args' is a dictionary with a value entry.
        # if (
        #     len(args) == 1 and
        #     isinstance(args[0], dict) and
        #     dict(args[0]).get("value") is not None and
        #     "random" not in kwargs and
        #     "value" not in kwargs
        # ):
        #     self.value = dict(args[0]).get("value")
        #     return

        # #Check if 'kwargs' contains the random key and that it is set to True.
        # if (
        #     len(args) == 0 and
        #     "random" in kwargs and
        #     kwargs["random"] is True and
        #     "value" not in kwargs and
        #     "force_type" not in kwargs
        # ):
        #     self.value = self.random_value()
        #     return None
    
        # if (
        #     "random" in kwargs and
        #     kwargs["random"] is True and
        #     # self.value is None and
        #     'value' not in kwargs and
        #     "force_type" in kwargs and
        #     kwargs["force_type"] is not None and
        #     kwargs["force_type"] is not False
        # ):
        #     self.value = self.random_value(type_=kwargs["force_type"])
        #     return None

        # # Check if 'kwargs' contains the random key and that it is set to False.
        # if (
        #     len(args) == 0 and
        #     "random" in kwargs and
        #     kwargs["random"] is False
        # ):
        #     self.value = None
        #     return None

        # # Check for an empty input.
        # if (
        #     len(args) == 0 and
        #     "random" not in kwargs and
        #     "value" not in kwargs
        # ):
        #     self.value = None
        #     return

        # # Check if 'kwargs' contains the value key. And that the value is not None.
        # if (
        #     len(args) == 0 and
        #     "value" in kwargs and
        #     kwargs["value"] is not None
        #     and "random" not in kwargs
        # ):
        #     self.value = kwargs["value"]
        #     return

        # # Check if 'args' contains a value. And that 'kwargs' does not contain and keys.
        # if (
        #     len(args) == 1 and
        #     "random" not in kwargs and
        #     "value" not in kwargs
        # ):
        #     self.value = args[0]
        #     return

        # # Check if 'args' contains a value. And that 'kwargs' contains the random key and that it is set to False.
        # if (
        #     len(args) == 1 and
        #     "random" in kwargs and
        #     kwargs["random"] is False
        # ):
        #     self.value = args[0]
        #     return

    def has_type(self, type_: Any) -> bool:
        """
        Checks if the value has a type.

        Args:
            type_ (Any): The type to check for.

        Returns:
            bool: True if the value has the type. 
                  Else False if the value does not have the type or is None.

        Example:
        ```Python
        unit = SuperUnit()
        unit.has_type(str)  # False type is None
        unit = SuperUnit("test")
        unit.has_type(str)  # True type is str
        unit.has_type(int)  # False type is str
        unit = SuperUnit(1234)
        unit.has_type(int)  # True type is int
        ```
        """
        if not self.is_none():
            return isinstance(self.value, type_)
        return False

    def force_type(self, type_: Any) -> None:
        """
        Forces the value to be a type.

        Args:
            type_ (Any): The type to force the value to.

        Raises:
            TypeError: If 'type_' is not a callable type.
            TypeError: If the value cannot be forced to the type.
            AttributeError: If the value is None.

        Example:
        ```Python
        unit = SuperUnit()
        unit.force_type(str)

        unit = SuperUnit("test").force_type(str)
        unit = SuperUnit("1234").force_type(int)
        unit = SuperUnit("test").force_type(int)  # Raises TypeError
        """

        # Check if 'type_' is a callable.
        # if not isinstance(type_, Callable or function or type):
        if not callable(type_):
            raise TypeError(f"Type {type_} is not a callable type.")

        if self.is_none() is False:
            try:
                if not self.has_type(type_):
                    self.value = type_(self.value)
            except Exception:
                raise TypeError(f"Cannot force type {type_} on value {self.value}.")
        else:
            raise AttributeError(f"Cannot force type {type_} on None value.")

    @staticmethod
    def get_none_list() -> list:
        """
        Get a list of values representing a NoneType.

        Returns:
            list: A list of values representing a NoneType.

        Example:
        ```Python
        SuperUnit.get_none_list()  # [None, "None", "", "null", "NULL", "none"]
        ```
        """
        return [
            None,
            "None",
            "none",
            "NONE",
            "",
            " ",
            "null",
            "Null",
            "NULL",
            "nil",
            "Nil",
            "NIL",
            str(""),
            str(" "),
            str("''"),
            str('""'),
            str(' ')
        ]

    @staticmethod
    def check_none(value: Any) -> bool:
        """
        Checks if the value is None or equal to any of the values on from the get_none_list() method.

        Args:
            value (Any): The value to check.

        Returns:
            bool: True if the value is None or equal to any of the values on from the get_none_list() method.
        """
        return value is None or value in SuperUnit.get_none_list()

    def is_none(self) -> bool:
        """
        Checks if the value is None or any of the following values representing a NoneType.

        Returns:
            bool: True if the value is None or any of the following values representing a NoneType.

        Example:
        ```Python
        unit = SuperUnit()
        unit.is_none()  # True

        unit = SuperUnit(None)
        unit.is_none()  # True

        unit = SuperUnit("None")
        unit.is_none()  # True
        """
        return SuperUnit.check_none(self.value)

    @staticmethod
    def random_value(type_: Optional[Any] = None) -> Any:
        """
        Create a random value based on the uuid4() function.

        Returns:
            str: A random value.
        """
        if type_ is int or type_ is float or type_ == "int":
            return int(uuid.uuid4().int)
        if type_ is bool or type_ == "bool":
            return bool(uuid.uuid4().int % 2)
        if type_ is str or type_ is None or type_ == "str":
            return str(uuid.uuid4().hex)

        return uuid.uuid4()

    def get_value_type(self) -> str:
        """
        Get the name of the value's type as defined by the type() function.

        Returns:
            str: The name of the value's type.
        """
        return type(self.value).__name__

    @staticmethod
    def from_dict(dictionary: Dict[str, Any]) -> "SuperUnit":
        """
        Returns a Super Unit from a dictionary.

        Args:
            dictionary (Dict[str, Any]): The dictionary to create the Super Unit from.

        Returns:
            SuperUnit: The Super Unit created from the dictionary.

        Example:
        ```Python
        unit = SuperUnit.from_dict({
            "value": "test"
        })
        unit.value  # "test"
        ```
        """
        return SuperUnit(
            value=dictionary["value"]
        )

    def __dict__(self) -> Dict[str, Any]:
        """
        Returns a dictionary from a Super Unit.
        """
        return {
            "value": self.value
        }

    @property
    def value(self) -> Any:
        """
        Returns the value of the Super Unit.
        * The value can be set to anything.
        * It is not type checked upon setting.
        * If the value is None, it will return None.


        Returns:
            Any: The value of the Super Unit.
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Sets the value.

        Args:
            value (Any): The value to set.

        Example:
        ```Python
        unit = SuperUnit()
        unit.value = "test"
        unit.value  # "test"
        ```
        """
        self._value = value

    @value.getter
    def value(self) -> Any:
        """
        'value' getter -> Gets the value.

        Returns:
            Any: The value of the Super Unit.

        Example:
        ```Python
        unit = SuperUnit()
        unit.value  # None

        unit = SuperUnit("test")
        unit.value  # "test"
        ```
        """
        return self._value

    @value.deleter
    def value(self) -> None:
        """
        Deletes the value.
        * Sets the value to None.
        * The value will have to be set again, if it is to be used.
        """
        self._value = None

    def __str__(self) -> str:
        """
        Returns the string representation of the value.
        """
        return str(self.value)


@dataclass(
    slots=True,
)
class SchemaEntry:
    """
    A Super Schema Entry class to control the system of grouping and validating values.
    
    Args:
        level (int): The level of the schema entry.
        schema (Dict[str, Any]): The schema of the included 'types' entry.
        types (Dict[str, Any]): The types of the schema entry.
        functions (Dict[str, Any]): The functions of the schema entry.
        overrides (Dict[str, Any]): The overrides of the schema entry.
    """
    level: int
    schema: Dict[str, Any] = field(default_factory=dict)
    types: Dict[str, Any] = field(default_factory=dict)
    functions: Dict[str, Any] = field(default_factory=dict)
    overrides: Dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        level: int,
        schema: Dict[str, Any],
        types: Dict[str, Any],
        functions: Dict[str, Any],
        overrides: Dict[str, Any],
    ) -> None:
        
        self.validate_level(level)
        self.validate_schema(schema)
        self.validate_types(types)
        self.functions = functions
        self.overrides = overrides

    def validate_level(self, level: int) -> None:
        """
        Validates the level of the schema entry.
        """
        if not SuperUnit.check_none(level):
            if not isinstance(level, int):
                raise TypeError(f"Level must be an integer, not {type(level).__name__}.")

            if level < 0:
                raise ValueError("Level must be greater than or equal to 0.")
            
            self.level = level
        else:
            raise TypeError("Level must not be None.")

    def validate_schema(self, schema: Dict[str, Any]) -> None:
        """
        Validates the schema of the schema entry.
        """
        if SuperUnit.check_none(schema):
            raise TypeError("Schema must not be None.")

        if not isinstance(schema, dict):
            raise TypeError(f"Schema must be a dictionary, not {type(schema).__name__}.")

        if len(schema) <= 0:
            raise ValueError("Schema must not be empty.")

        if not all(isinstance(key, str) for key in schema.keys()):
            raise TypeError("Schema keys must be strings.")

        if not all(isinstance(value, list) for value in schema.values()):
            raise TypeError("Schema values must be lists.")

        self.schema = schema

    def validate_types(self, types: Dict[str, Any]) -> None:
        """
        Validates the types of the schema entry.
        """
        if SuperUnit.check_none(types):
            raise TypeError("Types must not be None.")

        if not isinstance(types, dict):
            raise TypeError(f"Types must be a dictionary, not {type(types).__name__}.")

        if len(types) <= 0:
            raise ValueError("Types must not be empty.")

        if not all(isinstance(key, str) for key in types.keys()):
            raise TypeError("Types keys must be strings.")

        if not all(isinstance(value, list) for value in types.values()):
            raise TypeError("Types values must be lists.")

        if self.schema is not None:
            if not self.match_schema_and_types(self.schema, types):
                raise ValueError("Types must match the schema.")

        self.types = types

    def match_schema_and_types(self, schema: Dict[str, Any], types: Dict[str, Any]) -> bool:
        """
        Matches the schema and types of the schema entry.
        """
        if not SuperUnit.check_none(schema):
            if not SuperUnit.check_none(types):
                if len(schema) == len(types):
                    if all(key in types.keys() for key in schema.keys()):
                        if all(any(key in type_key for type_key in types.keys()) for key in schema.keys()):
                            return True
        return False



@dataclass(
    slots=True,
)
class Schema:
    """
    A Super Schema class to control the system of group objects and their units.
    """

    _schema: Optional[List[SchemaEntry]] = field(default_factory=List, init=True)

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
                "expected_system_types_schema": List[Any],
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
                "expected_super_types_schema": List[Any],
                # Any is a placeholder for the supported super types.
                "default_base_types_schema": {
                    "id_": List[Any],
                    "aliases": List[Any],
                    "super_type": [Any],
                    "accepts": List[Any],
                    "prefix": List[Any],
                    "suffix": List[Any],
                    "separator": List[Any],
                    "base_function": List[Any],
                }
            },
            types={
                "expected_super_types": ["__RESERVED__STR__", "__RESERVED__INT__", "__RESERVED__FLOAT__", "__RESERVED__BOOL__", "__RESERVED__LIST__", "__RESERVED__DICT__", "__RESERVED__TUPLE__", "__RESERVED__BYTES__"],
                "default_base_types": [
                    # The String Base Type Unit can accept any system type.
                    # Each __RESERVED__XXX__  super unit can only be used on a single base unit.
                    # Base Units cannot share super units.  But, base units can inherit super units from other base units by stacking them.
                    {"id_": ["str"], "aliases": ["string", "str"], "super_type": ["__RESERVED__STR__"], "accepts": ["*all_supported_super_types*"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["int"], "aliases": ["integer", "int"], "super_type": ["__RESERVED__INT__"], "accepts": ["__RESERVED__INT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["float"], "aliases": ["float"], "super_type": ["__RESERVED__FLOAT__"], "accepts": ["__RESERVED__FLOAT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["bool"], "aliases": ["boolean", "bool"], "super_type": ["__RESERVED__BOOL__"], "accepts": ["__RESERVED__BOOL__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["list"], "aliases": ["list"], "super_type": ["__RESERVED__LIST__"], "accepts": ["__RESERVED__LIST__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["dict"], "aliases": ["dictionary", "dict"], "super_type": ["__RESERVED__DICT__"], "accepts": ["__RESERVED__DICT__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["tuple"], "aliases": ["tuple"], "super_type": ["__RESERVED__TUPLE__"], "accepts": ["__RESERVED__TUPLE__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["bytes"], "aliases": ["bytes"], "super_type": ["__RESERVED__BYTES__"], "accepts": ["__RESERVED__BYTES__"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},

                    # Base Units can be stacked.
                    # Stacking a Base Unit ontop of another Base Unit will inherit the super_type of the Base Unit it is stacked ontop of.
                    # Accepted types can be defined for a stacked Base Unit, but the accepted types must be a subset of the accepted types of the Base Unit it is stacked ontop of.
                    # Lets declare a DID Base Type Unit.]
                    # The DID Base Type Unit stacks ontop of String Base Type Unit.
                    # This will be used to store a DID or VC starting with 'did:'
                    {"id_": ["did"], "aliases": ["did"], "super_type": ["str"], "accepts": ["str"], "prefix": ["did:"], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            },
            functions={
                "default_base_level_functions": [
                    {"prepare_base_types()": "Prepares the base types for use."},
                    {"create_base_type(id_, aliases, super_type, accepts, prefix, suffix, separator, base_function)": "Creates a base type."},
                    {"get_base_types()": "Returns a list of the *supported_base_types*."},
                    {"get_base_type(id_)": "Returns the base type for the given id_."},
                    {"get_base_type_by_alias(alias)": "Returns the base type for the given alias."},
                    {"get_base_type_by_super_type(super_type)": "Returns the base type for the given super base."},
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
                    {"id_": ["text"], "aliases": ["text"], "super_type": ["str"], "accepts": ["str"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["number"], "aliases": ["number"], "super_type": ["int", "float"], "accepts": ["int", "float"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            }
        )

        GROUP_SCHEMA = SchemaEntry(
            #
            # Group Schema
            #
            level=2,
            schema={
                "expected_base_types_schema": List[Any],
                # Inherits from the default base unit schema.
                "default_group_unit_types_schema": {
                    "id_": List[Any],
                    "aliases": List[Any],
                    "super_type": List[Any],
                    "accepts": List[Any],
                    "prefix": List[Any],
                    "suffix": List[Any],
                    "separator": List[Any],
                    "base_function": List[Any]
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
                "expected_base_types": ["str", "int", "float", "bool", "list", "dict", "tuple", "bytes", "did"],
                "default_group_unit_types": [
                    # If the group type has a super_type that contains a "prefix", "suffix", "separator", or "base_function", the "accepts" value defines the types that can be passed to the unit.
                    # For ex
                    {"id_": ["nonce"], "aliases": ["nonce"], "super_type": ["str", 'int'], "accepts": ["str, int"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["nonce_chain"], "aliases": ["nonce_chain"], "super_type": ["list"], "accepts": ["nonce"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["owner"], "aliases": ["owner"], "super_type": ["did"], "accepts": ["did"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["owners"], "aliases": ["owners"], "super_type": ["list"], "accepts": ["owner"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["credential"], "aliases": ["credential, cred"], "super_type": ["did"], "accepts": ["did"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["credentials"], "aliases": ["credentials, creds"], "super_type": ["list"], "accepts": ["credential"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["data_entry"], "aliases": ["data_entry", "data"], "super_type": ["*all_supported_base_types*"], "accepts": ["*all_supported_base_types"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["data"], "aliases": ["data"], "super_type": ["dict"], "accepts": ["data_entry"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["group_unit"], "aliases": ["group_unit, unit"], "super_type": ["dict"], "accepts": ["nonce_chain", "owners", "creds", "data"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["group"], "aliases": ["group"], "super_type": ["dict"], "accepts": ["group_unit"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
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
                    {"id_": ["my_custom_group_value"], "aliases": ["my_custom_group_value"], "super_type": ["str"], "accepts": ["str"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                    {"id_": ["custom_group_unit"], "aliases": ["custom_group_unit"], "super_type": ["group_unit"], "accepts": ["group_unit", "my_custom_group_value"], "prefix": [None], "suffix": [None], "separator": [None], "base_function": [None]},
                ]
            }
        )

        self._schema = [
            SUPER_SCHEMA,
            BASE_SCHEMA,
            GROUP_SCHEMA
        ]

    @property
    def schema(self) -> List[SchemaEntry]:
        return self._schema

    @schema.setter
    def schema(self, value: List[SchemaEntry]) -> None:
        self._schema = value

    @schema.deleter
    def schema(self) -> None:
        del self._schema

    def load_schema(self, schema: List[SchemaEntry]) -> None:
        """
        Loads a schema into the generator.
        """
        self.schema = schema

    def validate_schema(self) -> None:
        """
        Validates the schema.
        """
        try:
            self.order_schema_by_level()
        except Exception as e:
            raise Exception(f"Error ordering schema by level: {e}")

    def order_schema_by_level(self) -> None:
        """
        Orders the schema by level.
        """
        self.schema = sorted(self.schema, key=lambda x: x.level)


class Generator(Schema):
    """
    The Generator class is used to generate units of different types and levels.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the Generator class.
        """
        Schema.__init__(self, *args, **kwargs)
        self.__post_init__(*args, **kwargs)

    def __post_init__(self, *args, **kwargs):
        """
        Post-initializes the Generator class.
        """
        pass

    def create_super(self, *args, **kwargs) -> SuperUnit:
        """
        Creates a unit type from the loaded schema
        """
        pass

