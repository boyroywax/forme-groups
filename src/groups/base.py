
from attrs import define, field, validators
from typing import List, Any, Optional, Dict


class Base:
    _base_value_type: Any = field(default=str, validator=validators.instance_of(type))

    @define(frozen=True, slots=True)
    class Value_:
        _value: Any

    @define(frozen=True, slots=True)
    class Function_:
        _object: 'Base.Value_'
        _args: List['Base.Value_']

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
    
    class Unit_Pool_:
        _units: List['Base.Unit_']

    class Group_:
        _type_pool: 'Base.Type_Pool_'
        _unit_pool: 'Base.Unit_Pool_'


    

