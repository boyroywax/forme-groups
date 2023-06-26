from typing import Any, Dict, List, Optional
import uuid

# from .units import Units as SystemUnits
from .config import Config as SystemConfig
from .generator import Generator as SystemGenerator


class System():
    """
    The system class.
    """

    id: Optional[str] = uuid.uuid4().hex
    config: Optional[SystemConfig] = None
    generator: Optional[SystemGenerator] = None

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the system class.
        """

        if "id" in kwargs and kwargs["id"] is not None:
            self.id = kwargs["id"]
        if "config" in kwargs and kwargs["config"] is not None:
            self.config = kwargs["config"]
        if "generator" in kwargs and kwargs["generator"] is not None:
            self.generator = kwargs["generator"]

    def set_config(
        self,
        override_defaults: Optional[bool] = False,
        overrides: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initializes the system class.
        """
        self.config = SystemConfig(
            self,
            override_defaults=override_defaults,
            overrides=overrides
        )
