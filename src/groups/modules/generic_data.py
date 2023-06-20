from datetime import datetime
from typing import Dict, Optional

from groups.modules.default_schema import DefaultSchema


class GenericData():
    """
    A generic data class used by the UniversalObject class.
    """

    def __init__(self, default_schema: Optional[DefaultSchema] = None) -> None:
        """
        Constructor for the GenericData class.
        """
        if default_schema is None:
            self.data: Dict = {}
        else:
            self.data: Dict = default_schema.get_entries()
        self.last_modified: datetime = datetime.now()

    def get_data(self) -> Dict:
        """
        Returns the data.
        """
        return self.data

    def set_data(self, data: Dict) -> None:
        """
        Sets the data.
        """
        self.data = data

    def get_last_modified(self) -> datetime:
        """
        Returns the last modified timestamp.
        """
        return self.last_modified

    def set_last_modified(self, last_modified: datetime) -> None:
        """
        Sets the last modified timestamp.
        """
        self.last_modified = last_modified

    def update_data(self, data: Dict) -> None:
        """
        Updates the data.
        """
        self.data.update(data)

    def update_last_modified(self) -> None:
        """
        Updates the last modified timestamp.
        """
        self.last_modified = datetime.now()

    def update_data_and_last_modified(self, data: Dict) -> None:
        """
        Updates the data and last modified timestamp.
        """
        self.update_data(data)
        self.update_last_modified()

    def clear_data(self) -> None:
        """
        Clears the data.
        """
        self.data = {}

    def clear_last_modified(self) -> None:
        """
        Clears the last modified timestamp.
        """
        self.last_modified = datetime.now()

    def clear_data_and_last_modified(self) -> None:
        """
        Clears the data and last modified timestamp.
        """
        self.clear_data()
        self.clear_last_modified()

    def __json__(self) -> Dict:
        """
        Returns the JSON representation of the GenericData object.
        """
        return {
            "data": self.data,
            "last_modified": self.last_modified
        }

    def __str__(self) -> str:
        """
        Returns the string representation of the GenericData object.
        """
        return str(self.__json__())

    def __repr__(self) -> str:
        """
        Returns the string representation of the GenericData object.
        """
        return str(self.__json__()) 

    def __eq__(self, other: object) -> bool:
        """
        Returns the equality of the GenericData object with another object.
        """
        if isinstance(other, GenericData):
            return self.data == other.data and self.last_modified == other.last_modified
        return False