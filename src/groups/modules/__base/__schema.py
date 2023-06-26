from .__type import Type_

from typing import List, Optional, Dict, Any
from __type import Type_
from __unit import Unit_


class _Default_Schema():
    """
    """
    _types: List[Type_] = [Type_()]

    _schema_entry: Dict[str, Any] = {
        "entry": {  
            "type": "entry",
            "parent": ["dict"],
            "descriptors": ["entry"],
            "prefix": "entry:",
            "suffix": "",
            "separator": ",",
        }
    } 
    _schema_: Dict[str, Any] = {
        "schema": [
            {"entry": _schema_entry},
        ]
    }
    
    def __init__(
        self,
        types: Optional[List[Type_]] = None
    ) -> None:
        """
        Initializes the Schema class.
        """
        if types is not None:
            self.set_types(types)





class Schema_():
    """
    
    """

    _schema: Optional[List[]] = None
    _types: Optional[List[Type_]] = []

    def __init__(
        self,
        schema: Optional[List] = None,
        types: Optional[List[Type_]] = None
    ) -> None:
        """
        Initializes the Schema class.
        """
        
        if schemas is not None:
            self.set_schemas(schemas)

        if types is not None:
            self.set_types(types)

    def set_schemas(self, schemas: List) -> None:
        """
        Sets the schemas.
        """
        self._schemas = schemas

    def set_types(self, types: List[Type_]) -> None:
        """
        Sets the types.
        """
        self._types = types

    def get_schemas(self) -> List:
        """
        Returns the schemas.
        """
        return self._schemas
    
    def get_types(self) -> List[Type_]:
        """
        Returns the types.
        """
        return self._types
    

