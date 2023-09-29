
from .unit_type import UnitTypeRef


def _type_ref_converter(type_ref: UnitTypeRef | str) -> UnitTypeRef:
    if isinstance(type_ref, UnitTypeRef):
        return type_ref
    elif isinstance(type_ref, str):
        return UnitTypeRef(alias=type_ref)
    else:
        raise ValueError(f"Invalid type_ref {type_ref}.")