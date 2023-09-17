from attrs import define, field
from typing import Any, List, Dict

from .unit import Unit, UnitGenerator, UnitTypeRef, UnitTypePool

__DEFAULT_NONCE_UNIT_TYPE_ALIAS__: str = "int"
__DEFAULT_NONCE_UNIT_TYPE_DIVIDER__: str = "."
__DEFAULT_NONCE_UNIT_ALLOWED_TYPES__: tuple = ("int", "integer")


@define(frozen=True, slots=True)
class Data:
    entries: tuple[Unit] = field(factory=tuple)

    def __attrs_init__(self, data: tuple[Unit] = None, ):
        if data is None:
            self.entries = None
        else:
            self.entries = data

    def get_schema(self) -> Schema | None:
        found_schema: Schema = None
        for entry in self.entries:
            if entry.type_ref.alias == "dict":
                if str(entry.value).lower() == "schema":
                    if found_schema is None:
                        found_schema: Schema = entry
                    else:
                        raise ValueError("Multiple schemas found in Data.entries.")
                elif "schema" in str(entry.value).lower():
                    if found_schema is None:
                        found_schema: Schema = entry
                    else:
                        raise ValueError("Multiple schemas found in Data.entries.")
        return found_schema