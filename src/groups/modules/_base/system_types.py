
from typing import Optional

from .type import Type

_SUPER_TYPE: str = "string"


class SystemTypes():
    """
    SystemTypes
    """
    _super: Optional[Type] = None

    def __init__(
        self,


    class String(Type):
        """
        String
        """

        def __init__(self):
            super().__init__(
                parent=[_SUPER_TYPE],
                type="string",
                descriptors=["str", "string"],
                prefix="",
                suffix="",
                separator="",
                generator=Generator.String()
            )

    class Integer(Type):
        """
        Integer
        """

        def __init__(self):
            super().__init__()

    class Float(Type):
        """
        Float
        """

        def __init__(self):
            super().__init__()

    class Boolean(Type):
        """
        Boolean
        """

        def __init__(self):
            super().__init__()
