import hashlib
from attrs import define, field, validators
import json
from typing import Any, Optional, Tuple

# from merkle_tree import MerkleTree

__DEFAULT_SYSTEM_TYPES_PATH__ = "src/groups"


@define(frozen=True, slots=True)
class UnitTypeRef:
    """A reference to a UnitType.

    Attributes:
        alias (str): The alias of the UnitType.
    """
    alias: str = field(default=None, validator=validators.instance_of(str))

    def __iter__(self):
        yield self.alias

    def __str__(self) -> str:
        return self.alias
    
    def __repr__(self) -> str:
        return f'UnitTypeRef(alias="{self.alias}")'
    
    def hash_256(self):
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


@define(frozen=True, slots=True)
class UnitTypeFunction:
    """A function that can be used to generate a Unit.

    Attributes:
        object (callable): The function that will be called to generate a Unit.
        args (tuple): The arguments that will be passed to the function.
    """
    object: callable = field(default=None)
    args: tuple = field(default=None)

    def call(self, input: Any = None) -> object:
        """Call the function with the given input.

        Args:
            input (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        if input is not None and self.args is not None:
            if len(self.args) > 0:
                new_args = list(self.args)
                new_args.insert(0, input)
                return self.object(*new_args)
        elif input is not None:
            return self.object(input)
        else:
            return self.object(*self.args)
        
    def __str__(self) -> str:
        return f"{self.object.__class__}({self.args})"
        
    def __repr__(self) -> str:
        return f"UnitTypeFunction(object={self.object.__class__}, args={self.args})"
    
    def hash_256(self):
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


@define(frozen=True, slots=True)
class UnitType:
    """A type of Unit.

    Attributes:
        aliases (list[UnitTypeRef]): The aliases of the UnitType.
        super_type (list[UnitTypeRef]): The super types of the UnitType.
        prefix (str): The prefix of the UnitType. Defaults to None.
        suffix (str): The suffix of the UnitType. Defaults to None.
        separator (str): The separator of the UnitType. Defaults to None.
        sys_function (UnitTypeFunction): The system function of the UnitType. Defaults to None.
    """
    aliases: Tuple[UnitTypeRef] = field(factory=tuple)
    super_type: Tuple[UnitTypeRef] = field(factory=tuple)
    prefix: Optional[str] = field(default=None, validator=validators.optional(validators.instance_of(str)))
    suffix: Optional[str] = field(default=None, validator=validators.optional(validators.instance_of(str)))
    separator: Optional[str] = field(default=None, validator=validators.optional(validators.instance_of(str)))
    sys_function: Optional[UnitTypeFunction] = field(default=None)

    def __aliases_repr__(self) -> str:
        aliases = ""
        for alias in self.aliases:
            aliases += alias.__repr__() + ", "
        return aliases[:-2]

    def __super_type_repr__(self) -> str:
        super_type = ""
        for type in self.super_type:
            super_type += type.__repr__() + ", "
        return super_type[:-2]
    
    def __repr__(self) -> str:
        return f"UnitType(aliases=[{self.__aliases_repr__()}], super_type=[{self.__super_type_repr__()}], prefix={self.prefix}, suffix={self.suffix}, separator={self.separator}, sys_function={self.sys_function.__repr__()})"
    
    def hash_256(self):
        return hashlib.sha256(self.__repr__().encode()).hexdigest()

@define(slots=True)
class UnitTypePool:
    """A pool of UnitTypes.

    Attributes:
        _frozen (bool): Whether the UnitTypePool is frozen.
        unit_types (list[UnitType]): The UnitTypes in the UnitTypePool.
    """
    _frozen: bool = field(default=False)
    unit_types: list[UnitType] | tuple[UnitType] = field(factory=list)

    def __init__(self, sys_types: bool = False, path: str = None):
        self._frozen = False
        self.unit_types = []

        if sys_types is True:
            self.set_types_from_json(path=path)

    def freeze_pool(self):
        """Freeze the UnitTypePool."""
        self.__setattr__("unit_types", tuple(self.unit_types))
        self.__setattr__("_frozen", True)

    @property
    def frozen(self) -> bool:
        """Whether the UnitTypePool is frozen."""
        return self._frozen

    @frozen.getter
    def frozen(self) -> bool:
        """Whether the UnitTypePool is frozen."""
        return self._frozen

    def get_type_from_alias(self, alias: str) -> UnitType | None:
        """Get a UnitType from an alias.

        Args:
            alias (str): The alias of the UnitType.

        Returns:
            UnitType | None: The UnitType with the given alias, or None if the UnitTypePool does not contain the alias.
        """
        for unit_type in self.unit_types:
            for aliases in unit_type.aliases:
                if aliases.alias == alias:
                    return unit_type
        return None

    def contains_alias(self, alias: str) -> bool:
        """Whether the UnitTypePool contains an alias.

        Args:
            alias (str): The alias to check.

        Returns:
            bool: Whether the UnitTypePool contains the alias.
        """
        return self.get_type_from_alias(alias) is not None

    def add_unit_type(self, unit_type: UnitType):
        """Add a UnitType to the UnitTypePool.

        Args:
            unit_type (UnitType): The UnitType to add.

        Raises: 
            ValueError: If the UnitTypePool already contains an alias of the UnitType.
        """
        for aliases in unit_type.aliases:
            if self.contains_alias(aliases.alias):
                raise ValueError("UnitTypePool already contains alias: " + aliases.alias)
        self.unit_types.append(unit_type)

    def add_unit_type_from_json(self, json: dict):
        """Add a UnitType from a JSON object.

        Args:
            json (dict): The JSON object to add.

        Raises:
            ValueError: If the UnitTypePool already contains an alias of the UnitType.
        """
        unit_type = UnitType(
            aliases=[UnitTypeRef(alias=alias) for alias in json["aliases"]],
            super_type=[UnitTypeRef(alias=alias) for alias in json["base_type"]],
            prefix=json["prefix"],
            suffix=json["suffix"],
            separator=json["separator"],
            sys_function=UnitTypeFunction(object=eval(json["sys_function"]["object"]), args=json["sys_function"]["args"]),
        )
        self.add_unit_type(unit_type)

    def set_types_from_json(self, path: str = None):
        """Set the system types of the UnitTypePool from a JSON file."""
        types_path = __DEFAULT_SYSTEM_TYPES_PATH__ + "/system_types.json"

        if path is not None:
            types_path = path

        with open(types_path, "r") as f:
            sys_types = json.load(f)
            for type_ in sys_types["system_types"]:
                self.add_unit_type_from_json(type_)

    def get_type_aliases(self) -> list[str]:
        """Get the aliases of all UnitTypes in the UnitTypePool.

        Returns:
            list[str]: The aliases of all UnitTypes in the UnitTypePool.
        """
        aliases = []
        for unit_type in self.unit_types:
            for alias in unit_type.aliases:
                aliases.append(alias.alias)
        return aliases


@define(frozen=True, slots=True)
class Unit:
    value: Any = field(default=None)
    type_ref: UnitTypeRef = field(default=None)


@define(slots=True)
class UnitGenerator:
    unit_type_pool: UnitTypePool = field(default=None)

    def __init__(self, unit_type_pool: UnitTypePool = None, freeze: bool = False, system_types_path: str = None, custom_types_path: str = None):
        self.unit_type_pool = UnitTypePool()
        self.unit_type_pool.set_types_from_json(path=system_types_path)

        if custom_types_path is not None:
            self.unit_type_pool.set_types_from_json(path=custom_types_path)

        if unit_type_pool is not None:
            for unit_type in unit_type_pool.unit_types:
                self.unit_type_pool.add_unit_type(unit_type)

        if freeze is True:
            self.__post_init__(freeze=True)

    def __post_init__(self, **kwargs):
        if kwargs.get("freeze", False) is True:
            self.unit_type_pool.freeze_pool()

    def check_frozen_pool(self) -> bool:
        return self.unit_type_pool.frozen

    def create_unit(self, alias: str, value: Any = None, force: bool = True) -> Unit:
        if not self.check_frozen_pool():
            raise Exception("UnitTypePool must be frozen before generating units.")

        unit_type: UnitType = self.unit_type_pool.get_type_from_alias(alias)

        if unit_type is None:
            raise ValueError("UnitTypePool does not contain alias: " + alias)

        if force is True:
            if unit_type.sys_function is None:
                return Unit(value=value, type_ref=UnitTypeRef(alias))
            else:
                return Unit(value=unit_type.sys_function.call(value), type_ref=UnitTypeRef(alias))

        return Unit(value=value, type_ref=UnitTypeRef(alias))

    def format_unit(self, unit: Unit) -> str:
        unit_type: UnitType = self.unit_type_pool.get_type_from_alias(unit.type_ref.alias)
        formatted_unit = ""

        if unit_type.prefix is not None:
            formatted_unit += unit_type.prefix

        if unit_type.separator is not None:
            if isinstance(unit.value, tuple | list):
                for value in unit.value:
                    formatted_unit += str(value) + unit_type.separator
                formatted_unit = formatted_unit[:-1]
            else:
                formatted_unit += str(unit.value)

        if unit_type.suffix is not None:
            formatted_unit += unit_type.suffix

        return formatted_unit
