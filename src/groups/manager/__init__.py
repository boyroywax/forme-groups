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

    def init_system(self) -> None:
        """
        Initializes the system.
        """
        self.system = System()

    def get_settings(self) -> Settings:
        """
        Returns the settings.
        """
        return self.settings
    
    def get_system(self) -> System:
        """
        Returns the system.
        """
        return self.system
    
    def set_settings(self, settings: Settings) -> None:
        """
        Sets the settings.
        """
        self.settings = settings

    def set_system(self, system: System) -> None:
        """
        Sets the system.
        """
        self.system = system

        


        

