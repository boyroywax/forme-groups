import hashlib
from attrs import define, field, validators
from typing import Any, Optional, Tuple, Callable


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
    function_object: Callable = field(default=None)
    args: tuple = field(default=None)

    def call(self, input_: Any = None) -> Any:
        """Call the function with the given input.

        Args:
            input (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        print(self.function_object)
        print(str(self.args))
        if str(self.function_object) == "<class 'str'>":
            return str(input_)
        if str(self.function_object) == "<class 'dict'>":
            return dict(input_)
        # class_name = str(self.function_object).strip("<class '").strip("'>")
        # print(class_name)
        # class_ = eval(class_name)
        # class_ = eval(self.function_object)
        if input_ is not None and self.args is not None and len(self.args) > 0:
            if len(self.args) > 0:
                new_args = list(self.args)
                new_args.insert(0, input_)
                return self.function_object(*new_args)
            
        # return self.function_object(input_)

        if input is not None and self.function_object is None:
            return input_
        if input is not None and self.function_object is not None and self.args is None:
            return self.function_object(input_)

        return self.function_object(*self.args)

    def __str__(self) -> str:
        return f"{self.function_object.__str__}({self.args})"

    def __repr__(self) -> str:
        return f"UnitTypeFunction(object={str(self.function_object)}, args={self.args})"

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