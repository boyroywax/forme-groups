from typing import Dict, List, Optional

_JOBS: List[Dict[str, str]] = [
    {"init": "Initializing the setup."},
    {"install": "Installing the setup."},
    {"update": "Updating the setup."},
    {"uninstall": "Uninstalling the setup."},
    {"remove": "Removing the setup."},
    {"delete": "Deleting the setup."},
    {"clean": "Cleaning the setup."},
    {"build": "Building the setup."},
    {"rebuild": "Rebuilding the setup."},
    {"test": "Testing the setup."},
    {"run": "Running the setup."},
    {"start": "Starting the setup."},
    {"stop": "Stopping the setup."},
    {"restart": "Restarting the setup."},
    {"pause": "Pausing the setup."},
    {"resume": "Resuming the setup."},
    {"kill": "Killing the setup."},
    {"execute": "Executing the setup."},
    {"execute_async": "Executing the setup asynchronously."},
]


class Jobs():
    """
    Manages the jobs of the setup object.
    """

    _jobs: Optional[List[Dict[str, str]]] = None

    def __init__(
        self,
        _jobs: Optional[List[Dict[str, str]]] = None
    ) -> None:
        """
        Initializes the Jobs class.
        """
        self.set_jobs(_jobs)

    def set_jobs(self, _jobs: List[Dict[str, str]]) -> None:
        """
        Sets the jobs of the setup object.
        """
        self._jobs = _jobs

    def get_jobs(self) -> List[Dict[str, str]]:
        """
        Gets the jobs of the setup object.
        """
        return self._jobs

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the jobs object to a dictionary.
        """
        return {
            "jobs": self._jobs
        }