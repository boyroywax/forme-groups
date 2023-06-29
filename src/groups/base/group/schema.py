from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(
    slots=True,
)
class Schema(BaseType):
    """
    Manages the schema of the base units that comprise the group object.
    """
    # END: abpxx6d04wxr

    def __init__(self, *args, **kwargs):
        """
        Initializes the Schema class.

        :param args: Tuple[Any]
            The arguments to initialize the Schema class.
            The first argument is the 'value'.
            The second argument is the 'base_type'.

        :param kwargs: Dict[str, Any]
            The keyword arguments to initialize the Schema class.
            The 'value' can be provided as a keyword argument.
            The 'base_type' can be provided as a keyword argument.
        """
        BaseType.__init__(self, *args, **kwargs)
        self.__post__init__(*args, **kwargs)
