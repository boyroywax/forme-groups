from typing import Optional


class Groups():
    """
    The Groups class manages a collection of Universal Objects.
    """

    def __init__(self, groups: Optional[list]) -> None:
        """
        Constructor for the Groups class.
        """
        self.groups: list = groups
