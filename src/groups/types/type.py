from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable


@dataclass
class Type():
    """
    Manages the type of the group object.
    """
    id: Optional[str] = None
    aliases: Optional[List[str]] = None
    super_type: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    separator: Optional[str] = None
    system_function: Optional[Callable] = None

    def get_id(self) -> str:
        """
        Gets the ID.
        """
        return self.id
    
    def get_aliases(self) -> List[str]:
        """
        Gets the aliases.
        """
        return self.aliases
    
    def get(self, id: str) -> Optional[Any]:
        """
        Get the type by ID.
        """
        if self.id == id:
            return self
        
        return None 
    
