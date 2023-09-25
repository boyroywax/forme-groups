
from attrs import define, field, validators
from typing import List, Any, Optional, Dict, Callable

from .utils.hash import hash_sha256


class Base:
    _base_value_type: Any = field(default=str, validator=validators.instance_of(type))

    class Hashable_:
        def __hash__(self) -> str:
            return hash_sha256(self.__repr__())

    @define(frozen=True, slots=True, weakref_slot=False)
    class Value_(Hashable_):
        _value: Any

        def __str__(self) -> str:
            return f"{self._value}"
        
        def __repr__(self) -> str:
            return f"{self._value}"
        
        def __hash__(self) -> str:
            return super().__hash__()
        
    @define(frozen=True, slots=True, weakref_slot=False)
    class Callable_(Hashable_):
        _function: object = field(validator=validators.instance_of(object))
        _args: List['Base.Value_'] = field(factory=list)

        def __call__(self, _input: 'Base.Value_') -> 'Base.Value_':
            if len(self._args) == 0:
                return Base.Value_(self._function(_input._value))
            else:
                return Base.Value_(self._function(_input._value, *self._args))

    @define(frozen=True, slots=True, weakref_slot=False)
    class Function_(Hashable_):
        _object: Optional['Base.Callable_'] = field(default=None, validator=validators.optional(validators.instance_of('Base.Callable_')))

        def __call__(self, _input: 'Base.Value_') -> 'Base.Value_':
            return self._object.call(_input._value)

    @define(frozen=True, slots=True)
    class Container_:
        _prefix: 'Base.Value_'
        _suffix: 'Base.Value_'
        _separator: 'Base.Value_'

    @define(frozen=True, slots=True)
    class Type_:
        _aliases: List['Base.Value_']
        _super_type: 'Base.Type_'
        _is_container: bool
        _container: Optional['Base.Container_']
        _function: Optional['Base.Function_']

        @define(frozen=True, slots=True)
        class Reference_:
            _alias: 'Base.Value_'

        @property
        def ref(self) -> 'Base.Type_.Reference_':
            return self.Reference_(self._aliases[0])

    @define(frozen=True, slots=True)
    class Schema_:
        _pattern: Dict['Base.Value_', 'Base.Type_.Reference_']

    @define(frozen=True, slots=True)
    class Unit_:
        _value: 'Base.Value_'
        _type_ref: 'Base.Type_.Reference_'

    @define(frozen=True, slots=True)
    class Type_Pool_:
        _types: List['Base.Type_']

        def get(self, alias: 'Base.Type_.Reference_') -> Optional['Base.Type_']:
            for typ in self._types:
                if alias in typ._aliases:
                    return typ
            return None

    class Unit_Pool_:
        _units: List['Base.Unit_']

    class Group_:
        _type_pool: 'Base.Type_Pool_'
        _unit_pool: 'Base.Unit_Pool_'
