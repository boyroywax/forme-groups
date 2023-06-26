from typing import List, Optional, Dict, Any


class Checks():
    """
    Checks the system for any errors.
    """

    output: Dict[str, Any] = {}

    def __init__(
        self,
    ) -> None:
        """
        Initializes the SystemCheck class.
        """
        # self._system = system

    def check_system(
        self,
        process: List[str]
    ) -> List[str]:
        """
        Checks the system.
        """
        output: Dict[str] = {}
        if process is not None and "system_types" in process:
            self.output['supported_types'] = self.check_supported_system_types()
        else:
            self.output['supported_types'] = self.check_supported_system_types()

