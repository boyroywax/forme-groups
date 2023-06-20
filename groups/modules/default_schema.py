from typing import List, Optional, Dict
import uuid

_POSTFIX = "_DEFAULT_SCHEMA"

_DEFAULT_SCHEMA = {
    "title": uuid.uuid4().hex + _POSTFIX,
    "entries": {
        "link": [],
        "schema": {},
    }
}


class DefaultSchema():
    """
    Default schema for all data models used in the Universal Object.
    """

    def __init__(
            self,
            entries: Optional[Dict],
            title: Optional[str] = None
    ) -> None:
        """
        Constructor for the DefaultSchema class.
        """
        if title is None:
            self.title: str = _DEFAULT_SCHEMA["title"]
        else:
            self.title: str = title

        if entries is None:
            self.entries: Dict = _DEFAULT_SCHEMA["entries"]
        else:
            self.entries: Dict = entries

    def get_title(self) -> str:
        """
        Returns the title.
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        Sets the title.
        """
        self.title = title

    def get_entries(self) -> Dict:
        """
        Returns the entries.
        """
        return self.entries

    def set_entries(self, entries: Dict) -> None:
        """
        Sets the entries.
        """
        self.entries = entries

    def get_entry_value(self, key: str) -> Optional[List]:
        """
        Returns the entry value.
        """
        if key not in self.entries:
            return None
        return self.entries[key]

    def set_entry_value(self, key: str, value: List) -> None:
        """
        Sets the entry value.
        """
        self.entries[key] = value

    def check_for_link(self) -> bool:
        """
        Checks if the schema has a link.
        """
        return len(self.entries["link"]) > 0

    def check_for_schema(self) -> bool:
        """
        Checks if the schema has a schema.
        """
        return len(self.entries["schema"]) > 0

    def __json__(self) -> Dict:
        """
        Returns the JSON representation of the DefaultSchema object.
        """
        return {
            "title": self.title,
            "entries": self.entries,
        }

    def __str__(self) -> str:
        """
        Returns the string representation of the DefaultSchema object.
        """
        return str(self.__json__())

    def __repr__(self) -> str:
        """
        Returns the string representation of the DefaultSchema object.
        """
        return self.__str__()
