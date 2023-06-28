import json
import os

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .type import Type as TypeClass


@dataclass
class Defined():
    """
    Manages the defined of the group object.
    """
    _defined: Optional[List[TypeClass]] = None

    def __post_init__(self):
        """
        Post initialisation hook.
        """
        self._defined = self._load()

    def _load(self) -> List[TypeClass]:
        """
        Load the defined types from the JSON file.
        """
        defined = []

        with open(os.path.join(os.path.dirname(__file__), "defined.json")) as f:
            data = json.load(f)

            for d in data:
                defined.append(TypeClass(**d))

        return defined
    
    def _load_from_list(self, data: List[TypeClass]) -> List[TypeClass]:
        """
        Load the defined types from the dictionary.
        """
        defined = []

        for d in data:
            defined.append(TypeClass(d))

        return defined
    
    def get_defined(self) -> List[TypeClass]:
        """
        Gets the defined types.
        """
        return self._defined

    def get(self, id: str) -> Optional[TypeClass]:
        """
        Get the defined type by ID.
        """
        for defined in self._defined:
            if defined.id == id:
                return defined

        return None

    def get_by_alias(self, alias: str) -> Optional[TypeClass]:
        """
        Get the defined type by alias.
        """
        for defined in self._defined:
            if alias in defined.aliases:
                return defined

        return None
    
    def set_defined(self, data: List[TypeClass]) -> None:
        """
        Sets the defined types.
        """
        self._defined = self._load_from_list(data)
