from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable, Tuple, Iterable

__RESERVED_TYPES__ = ["__RESERVED_INT__", "__RESERVED_FLOAT__", "__RESERVED_STRING__", "__RESERVED_BOOLEAN__", "__RESERVED_LIST__", "__RESERVED_TUPLE__", "__RESERVED_DICT__", "__RESERVED_BYTES__", "__RESERVED_NONE__"]


@dataclass(slots=True, unsafe_hash=True)
class UnitTypeRef:
    type_ref: Any = field(default=None, repr=True, hash=True)


@dataclass(slots=True, unsafe_hash=True)
class UnitValue:
    value: Any = field(default=None, repr=True)


@dataclass(slots=True, unsafe_hash=True)
class UnitType:
    aliases: Optional[Tuple[UnitTypeRef]] = field(default_factory=tuple)
    super_type: Optional[UnitTypeRef] = field(default_factory=UnitTypeRef)
    prefix: Optional[str] = field(default_factory=str)
    suffix: Optional[str] = field(default_factory=str)
    separator: Optional[str] = field(default_factory=str)
    function_call: Optional[object] = field(default_factory=object)


@dataclass(slots=True, unsafe_hash=True)
class UnitTypePool:
    pool: Dict[str, UnitType] = field(default_factory=dict)

    def __post_init__(self, *args, **kwargs):
        self.pool = {}
        self.__SYSTEM_RESERVED__()
        if kwargs.get("pool") is not None and isinstance(kwargs.get("pool"), dict):
            for key, unit_type in kwargs.get("pool").items():
                print(unit_type + " name: " + key)
                self.add_type(unit_type, key)

    def __SYSTEM_RESERVED__(self):
        self.pool = {
            "integer": UnitType(
                aliases=(UnitTypeRef("integer"), UnitTypeRef("int")),
                super_type=UnitTypeRef("__RESERVED_INT__"),
                prefix=None,
                suffix=None,
                separator=None,
                function_call=int
            ),
            "float": UnitType(
                aliases=(UnitTypeRef("float"), UnitTypeRef("double"), UnitTypeRef("FLOAT"), UnitTypeRef("DOUBLE")),
                super_type=UnitTypeRef("__RESERVED_FLOAT__"),
                prefix=None,
                suffix=None,
                separator=None,
                function_call=float
            ),
            "string": UnitType(
                aliases=(UnitTypeRef("string"), UnitTypeRef("STRING")),
                super_type=UnitTypeRef("__RESERVED_STRING__"),
                prefix=None,
                suffix=None,
                separator=None,
                function_call=str
            ),
            "boolean": UnitType(
                aliases=(UnitTypeRef("boolean"), UnitTypeRef("BOOLEAN")),
                super_type=UnitTypeRef("__RESERVED_BOOLEAN__"),
                prefix=None,
                suffix=None,
                separator=None,
                function_call=bool
            ),
            "list": UnitType(
                aliases=(UnitTypeRef("list"), UnitTypeRef("LIST")),
                super_type=UnitTypeRef("__RESERVED_LIST__"),
                prefix="[",
                suffix="]",
                separator=",",
                function_call=list
            ),
            "tuple": UnitType(
                aliases=(UnitTypeRef("tuple"), UnitTypeRef("TUPLE")),
                super_type=UnitTypeRef("__RESERVED_TUPLE__"),
                prefix="(",
                suffix=")",
                separator=",",
                function_call=tuple
            ),
            "dict": UnitType(
                aliases=(UnitTypeRef("dict"), UnitTypeRef("DICT")),
                super_type=UnitTypeRef("__RESERVED_DICT__"),
                prefix="{",
                suffix="}",
                separator=",",
                function_call=dict
            ),
            "bytes": UnitType(
                aliases=(UnitTypeRef("bytes"), UnitTypeRef("BYTES")),
                super_type=UnitTypeRef("__RESERVED_BYTES__"),
                prefix="b'",
                suffix="'",
                separator=None,
                function_call=bytes
            ),
            "None": UnitType(
                aliases=(UnitTypeRef("None"), UnitTypeRef("NONE")),
                super_type=UnitTypeRef("__RESERVED_NONE__"),
                prefix=None,
                suffix=None,
                separator=None,
                function_call=type(None)
            )
        }

    def has_alias(self, alias: UnitTypeRef) -> str | None:
        for key, unit_type in self.pool.items():
            if alias in list(unit_type.aliases):
                return key
            if alias.type_ref == key:
                return key

    def has_prefix(self, prefix: str) -> str | None:
        for key, unit_type in self.pool.items():
            if unit_type.prefix == prefix:
                return key

    def has_suffix(self, suffix: str) -> str | None:
        for key, unit_type in self.pool.items():
            if unit_type.suffix == suffix:
                return key

    def has_separator(self, separator: str) -> str | None:
        for key, unit_type in self.pool.items():
            if unit_type.separator == separator:
                return key

    def add_type(self, unit_type: UnitType, name: Optional[str] = None) -> None:
        if name is None:
            name = unit_type.aliases[0].type_ref

        if unit_type.super_type is None or unit_type.super_type.type_ref is None:
            unit_type.super_type = UnitTypeRef("string")
            print(Exception("Super type not specified. Defaulting to string."))

        if unit_type.super_type not in self.pool.values() and unit_type.super_type.type_ref not in self.pool.keys():
            if unit_type.super_type.type_ref in __RESERVED_TYPES__:
                self.pool[unit_type.super_type.type_ref] = unit_type.super_type
                return

        for alias in unit_type.aliases:
            if alias.type_ref in self.pool.items():
                raise ValueError(f"Alias {alias.type_ref} already exists.")
            if self.has_alias(alias) is not None:
                raise ValueError(f"Alias {alias.type_ref} already exists.")

        if unit_type.prefix is not None:
            if self.has_prefix(unit_type.prefix) is not None:
                raise ValueError(f"Prefix {unit_type.prefix} already exists.")

        if unit_type.suffix is not None:
            if self.has_suffix(unit_type.suffix) is not None:
                raise ValueError(f"Suffix {unit_type.suffix} already exists.")

        if name in self.pool:
            raise ValueError(f"Unit type {name} already exists.")

        # TODO: Check for separator uniqueness.

        self.pool[name] = unit_type

    def get_type(self, *args, name: Optional[str] = None, alias: Optional[UnitTypeRef] = None) -> UnitType:

        print(args, name, alias)

        unit_type_ref = alias.type_ref if alias is not None else None
        type_name = name

        if len(args) > 1 and (name is not None and alias is not None):
            raise ValueError("Must provide either a single argument or a name, or an alias, not both.")

        if len(args) == 1:
            if isinstance(args[0], str):
                unit_type_ref = args[0]
            elif isinstance(args[0], UnitTypeRef):
                unit_type_ref = args[0].unit_type_ref

        if unit_type_ref is None and type_name is None:
            raise ValueError("Must provide either a name or an alias.")

        if unit_type_ref is not None and type_name is not None:
            raise ValueError("Must provide either a name or an alias, not both.")

        if unit_type_ref in self.pool.keys():
            type_name = unit_type_ref

        if unit_type_ref is not None and type_name is None:
            for key, unit_type in self.pool.items():
                if unit_type_ref in list(alias.type_ref for alias in unit_type.aliases):
                    type_name = key

        try:
            if type_name is None:
                type_name = unit_type_ref
            return self.pool[type_name]
        except KeyError:
            raise ValueError(f"Unit type {type_name} not found.")

    def remove_type(self, name: Optional[str] = None, alias: Optional[UnitTypeRef] = None) -> UnitType:
        if name is None and alias is None:
            raise ValueError("Must provide either a name or an alias.")
        if name is not None and alias is not None:
            raise ValueError("Must provide either a name or an alias, not both.")
        if name is not None:
            if name not in self.pool.keys():
                raise ValueError(f"Unit type {name} not found.")
            else:
                del self.pool[name]
        if alias is not None:
            for key, unit_type in self.pool.items():
                if alias in list(unit_type.aliases):
                    del self.pool[key]
                    return
            raise ValueError(f"Unit type {alias} not found.")

    def __iter__(self):
        return iter(self.pool.items())


@dataclass(slots=True)
class Unit:
    value: UnitValue = None
    type_ref: UnitTypeRef = None


#
# FROZEN DECORATOR
#
def frozen(cls):
    """
    Decorator that makes a class immutable (i.e. frozen).
    """

    def freeze(cls, *args, **kwargs):
        if getattr(cls, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        return cls

    cls.__setattr__ = freeze
    cls.__delattr__ = freeze

    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(cls, *args, **kwargs)
        cls._frozen = True
        # for obj in cls.__dict__.values():
        #     print(obj)

    cls.__init__ = new_init

    return type("Frozen" + cls.__name__, (cls,), {})


@dataclass(slots=True, unsafe_hash=True)
class Frozen(UnitTypeRef or UnitValue or UnitType or UnitTypePool or Unit):
    _frozen: bool = field(default=False, repr=True, hash=True)

    def __init__(self, *args, **kwargs):
        super(Frozen, self).__init__(*args, **kwargs)
        self.__setattr__("_frozen", False)
        self.__class__.__name__ = "Frozen" + type(args[0]).__name__

    def __setattr__(self, name, value):
        if getattr(self, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if getattr(self, "_frozen", False):
            raise AttributeError("Cannot modify frozen class.")
        object.__delattr__(self, name)

    def freeze(self):
        object.__setattr__(self, "_frozen", True)


@dataclass(slots=True)
class Generator:
    unit_type_pool: UnitTypePool = None

    def __init__(self, unit_type_pool: UnitTypePool = None):
        if unit_type_pool is None:
            self.unit_type_pool = UnitTypePool()
        else:
            self.unit_type_pool = unit_type_pool

    def generate_unit(self, unit_type: UnitTypeRef, value: UnitValue) -> Unit:
        return Unit(value=value, type_ref=unit_type)

    def generate_unit_type(self, super_type: UnitTypeRef, aliases: list[UnitTypeRef], prefix: str, suffix: str, separator: str) -> UnitType:
        return UnitType(super_type=super_type, aliases=aliases, prefix=prefix, suffix=suffix, separator=separator)

    def generate_unit_type_pool(self, pool: UnitTypePool ) -> UnitTypePool:
        return UnitTypePool(pool=pool)

    def generate_unit_value(self, value: str) -> UnitValue:
        return UnitValue(value=value)

    def generate_unit_type_ref(self, type_ref: str) -> UnitTypeRef:
        return UnitTypeRef(type_ref=type_ref)

    def check_pool_for_type(self, unit_type_ref: UnitTypeRef) -> bool:
        if unit_type_ref.type_ref in self.unit_type_pool.pool.keys():
            return True
        else:
            for key, unit_type in self.unit_type_pool.pool.items():
                if unit_type_ref in list(unit_type.aliases):
                    return True
        return False
