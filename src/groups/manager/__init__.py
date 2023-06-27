from typing import Optional

from .settings import Settings
from .system import System


class Manager():
    """
    This class is responsible for managing groups.
    """

    settings: Optional[Settings] = None
    system: Optional[System] = System()

    def __init__(self) -> None:
        """
        Initializes the Manager class.
        """
        pass

    def __post__init__(self) -> None:
        """
        Post initializes the Manager class.
        """
        pass

    def init_settings(self) -> None:
        """
        Initializes the settings.
        """
        self.settings = Settings()

        

