from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ...units.base.super import Super__

_STATUSES: List[str] = [
    "running",
    "success",
    "failure",
    "error",
    "warning",
    "info",
    "debug",
    "critical",
    "unknown"
]

@dataclass
class Setup():

    _job: Optional[Dict[str, Any]] = None
    _status: Optional[str] = None

    def __init__(
        self,
        _job: Optional[Dict[str, Any]] = None,
        _status: Optional[str] = None
    ) -> None:
        """
        Initializes the Setup class.
        """
        self.set_job({_JOBS[0]})
        self.set_status(_STATUSES[0])

    def set_job(self, _job: Dict[str, Any]) -> None:
        """
        Sets the job of the setup object.
        """
        self._job = _job

    def get_job(self) -> Dict[str, Any]:
        """
        Gets the job of the setup object.
        """
        return self._job

    def set_status(self, _status: str) -> None:
        """
        Sets the status of the setup object.
        """
        self._status = _status

    def get_status(self) -> str:
        """
        Gets the status of the setup object.
        """
        return self._status
