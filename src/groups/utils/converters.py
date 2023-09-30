from typing import Any, Optional, Tuple, List
# from ..unit_type import UnitTypeRef
# from ..unit import Unit, Value


# def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
#     if isinstance(type_ref, UnitTypeRef):
#         return type_ref
#     elif isinstance(type_ref, str):
#         return UnitTypeRef(alias=type_ref)
#     else:
#         raise ValueError(f"Invalid type_ref {type_ref}.")


# def _value_converter(value: Any) -> Value:
#     if isinstance(value, Value):
#         return value
#     elif isinstance(value, str) or isinstance(value, int) or isinstance(value, float) or isinstance(value, bool) or isinstance(value, dict) or isinstance(value, list) or isinstance(value, tuple) or isinstance(value, bytes) or value is None:
#         return Value(value)
#     else:
#         raise ValueError(f"Invalid value {value}.")


def _convert_list_to_tuple(items: List[Any] | Tuple[Any]) -> Tuple[Any]:
    if isinstance(items, tuple):
        return items
    elif isinstance(items, list):
        return tuple(items)
    else:
        raise ValueError(f"Invalid items {items}.")
