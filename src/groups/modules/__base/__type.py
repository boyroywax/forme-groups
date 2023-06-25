from typing import Optional

from .__value import Value_


class Type_():
    """
    The Type class is used to represent a unit's type.

    """
    _parent_type: Optional['Type_'] = None
    _type: Optional[Value_] = None
    _descriptors: Optional[list[Value_]] = None
    _prefix: Optional[Value_] = None
    _suffix: Optional[Value_] = None
    _seperator: Optional[Value_] = None
    _attrs: Optional[dict[str, Value_]] = None

    def __init__(
        self,
        parent_type: Optional['Type_'] = None,
        type: Optional[Value_] = None,
        descriptors: Optional[list[Value_]] = None,
        prefix: Optional[Value_] = None,
        suffix: Optional[Value_] = None,
        seperator: Optional[Value_] = None,
        attrs: Optional[dict[str, Value_]] = None
    ) -> None:
        """
        Initializes the BaseType class.
        """
        if parent_type is not None:
            self.set_parent_type(parent_type)

        if type is not None:
            self.set_type(type)

        if descriptors is not None:
            self.set_descriptors(descriptors)

        if prefix is not None:
            self.set_prefix(prefix)

        if suffix is not None:
            self.set_suffix(suffix)

        if seperator is not None:
            self.set_seperator(seperator)

        if attrs is not None:
            self.set_attrs(attrs)

