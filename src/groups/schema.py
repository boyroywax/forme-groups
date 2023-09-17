from attrs import define, field


class Schema:
    """A Schema that defines the structure of the data in Data

    Example:
        Schema(
            profile={
                "Schema": {
                    "test": "str"
                }
            }
        )
    """
    profile: dict = field(factory=dict)
    verified: bool = field(default=False)

    def __init__(self, profile: dict = None, ):
        if profile is None:
            raise ValueError("Schema profile not provided.")
        
        self.profile = profile

    def get_schema_types(self, profile: dict) -> list[str]:
        schema_types = []
        for key, value in profile.items():
            if isinstance(value, dict) and key == "Schema":
                print(value)
                for key, value_ in value.items():
                    schema_types.append(value_)
        return schema_types

    def verify_schema_types(self, profile: dict = None, type_pool: UnitTypePool = None) -> bool:
        if type_pool is None:
            raise ValueError("UnitTypePool not provided.")

        if profile is None:
            raise ValueError("Schema not provided.")

        _schema_types = self.get_schema_types(profile=profile)

        for type_ in _schema_types:
            if type_pool.get_type_from_alias(type_) is None:
                return False
        return True

    def contains_sub_schema(self) -> bool:
        contains_subschema: bool = False
        for key, value in self.profile.items():
            if isinstance(value, dict) and "Schema" in key:
                if contains_subschema is False:
                    contains_subschema = True
                else:
                    raise ValueError("Multiple schemas found in Data.entries.")
        return False