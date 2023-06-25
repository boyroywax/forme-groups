import json

from src.groups.modules.__base.__type import Type_
from src.groups.modules.__base.__value import Value_

_SUPER_SYSTEM_TYPE: str = "string"


class Generator_(Type_):
    """
    
    """
    _active_generator: Optional[Generator] = None

    def __init__(self, type: str = "str") -> None:
        """
        Initializes the Generator class.
        """
        super().__init__(type=type)

    def create_value
