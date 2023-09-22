import hashlib
from attrs import define, field, validators
from typing import Any, Optional, Tuple


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
        return f"{self.object.__str__}({self.args})"

    def __repr__(self) -> str:
        return f"UnitTypeFunction(object={str(self.object)}, args={self.args})"

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