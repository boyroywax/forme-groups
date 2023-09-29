'''
The Unit Type 



'''




import hashlib
from abc import ABCMeta, abstractmethod
from attrs import define, field, validators
from typing import Any, Optional, Tuple, Callable

from .merkle_tree import MerkleTree


__DEFAULT_UNIT_TYPE_REF__ = "str"

@define(slots=True, weakref_slot=False)
class ReferenceInterface(metaclass=ABCMeta):
    
    def __str__(self) -> str:
        slots = self.__slots__
        output = ""
        for slot in slots:
            output += f"{getattr(self, slot)}, "
        return output[:-2]
    
    def __repr__(self) -> str:
        slots = self.__slots__
        output = ""
        for slot in slots:
            output += f"{getattr(self, slot)}, "
        return f"{self.__class__.__name__}({output[:-2]})"
    
    def __iter__(self):
        slots = self.__slots__
        for slot in slots:
            yield getattr(self, slot)

    def hash_256(self) -> str:
        return hashlib.sha256(self.__repr__().encode()).hexdigest()
    
    def hash_tree(self) -> MerkleTree:
        slots = self.__slots__
        return MerkleTree(hashed_data=[getattr(self, slot).hash_256() for slot in slots])



@define(frozen=True, slots=True, weakref_slot=False)
class UnitTypeRef(ReferenceInterface):
    """A reference to a UnitType.

    Attributes:
        alias (str): The alias of the UnitType.
    """
    # pass
    alias: str = field(default=__DEFAULT_UNIT_TYPE_REF__, validator=validators.instance_of(str))

    # def __pre_init__(self, alias: str = __DEFAULT_UNIT_TYPE_REF__) -> None:
    #     self.alias = alias

    # def __iter__(self):
    #     yield self.alias

    # def __str__(self) -> str:
    #     return self.alias

    # def __repr__(self) -> str:
    #     return f'UnitTypeRef(alias={self.alias})'

    # def hash_256(self) -> str:
    #     return hashlib.sha256(self.__repr__().encode()).hexdigest()



@define(frozen=True, slots=True, weakref_slot=False)
class UnitTypeFunction:
    """A function that can be used to generate a Unit.

    Attributes:
        function_object (Callable): The function that will be called to generate a Unit.
        args (tuple): The arguments that will be passed to the function.
    """
    function_object: Callable = field(default=None)
    args: tuple = field(default=None)

    def call(self, input_: Any = None) -> Any:
        """Call the function with the given input.

        Args:
            input_ (Any): The input to the function.

        Returns:
            object: The result of the function call.
        """
        # print(self.function_object)
        # print(str(self.args))

        if str(self.function_object) == "<class 'str'>":
            return str(input_)
        if str(self.function_object) == "<class 'int'>":
            return int(input_)
        if str(self.function_object) == "<class 'float'>":
            return float(input_)
        if str(self.function_object) == "<class 'bool'>":
            return bool(input_)
        if str(self.function_object) == "<class 'dict'>":
            return dict(input_)
        if str(self.function_object) == "<class 'list'>":
            return list(input_)
        if str(self.function_object) == "<class 'tuple'>":
            return tuple(input_)
        if str(self.function_object) == "<class 'bytes'>":
            return bytes(input_)

        if input_ is not None and self.args is not None and len(self.args) > 0:
            if len(self.args) > 0:
                new_args = list(self.args)
                new_args.insert(0, input_)
                return self.function_object(*new_args)

        if input_ is not None and self.function_object is None:
            return input_
        if input_ is not None and self.function_object is not None and self.args is None:
            return self.function_object(input_)

        return self.function_object(*self.args)
    
    @property
    def function_object_str(self) -> str:
        return f"<class '{self.function_object.__class__.__name__}'>"
    
    @property
    def args_str(self) -> str:
        output_str = ""
        for arg in self.args:
            output_str += str(arg) + ", "
        return output_str[:-2]

    def __str__(self) -> str:
        return f"{self.function_object_str}({self.args_str})"

    def __repr__(self) -> str:
        return f"UnitTypeFunction(function_object={self.function_object_str}, args=[{self.args_str}])"

    def hash_256(self):
        return hashlib.sha256(self.__repr__().encode()).hexdigest()


@define(frozen=True, slots=True, weakref_slot=False)
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

    def hash_tree(self) -> MerkleTree:
        aliases_hash_tree = MerkleTree(hashed_data=[alias.hash_256() for alias in self.aliases])
        super_type_hash_tree = MerkleTree(hashed_data=[type.hash_256() for type in self.super_type])
        prefix_hash = hashlib.sha256(self.prefix.encode()).hexdigest()
        suffix_hash = hashlib.sha256(self.suffix.encode()).hexdigest()
        separator_hash = hashlib.sha256(self.separator.encode()).hexdigest()
        return MerkleTree(hashed_data=[aliases_hash_tree.root(), super_type_hash_tree.root(), prefix_hash, suffix_hash, separator_hash, self.sys_function.hash_256()])
