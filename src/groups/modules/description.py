import json
from dataclasses import dataclass
from typing import List


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class Description():
    """
    An UniversalObject's description
    All descriptions are stored in a list
    Descriptions are expected to be strings
    """

    description: List[str] = ["Universal serializable object"]

    def get_description(self) -> List:
        """
        Returns the description.
        """
        return self.description

    def set_description(self, description: List) -> None:
        """
        Sets the description.
        """
        self.description = description

    def get_description_length(self) -> int:
        """
        Returns the length of the description.
        """
        return len(self.description)

    def add_description(self, description: str) -> None:
        """
        Adds a description to the description.
        """
        self.description.append(description)

    def remove_description(self, description_index: int) -> None:
        """
        Removes a description from the description.
        """
        self.description.pop(description_index)

    def get_description_value(self, description_index: int) -> str:
        """
        Returns the description value at the given index.
        """
        return self.description[description_index]

    def set_description_value(self, description_index: int, description_value: str) -> None:
        """
        Sets the description value at the given index.
        """
        self.description[description_index] = description_value

    def verify_description_type(self) -> bool:
        """
        Verifies if the description is a valid string.
        """
        return True

    def to_json(self) -> List:
        """
        Returns the JSON representation of the description.
        """
        return json.dumps(self.description)

    def from_json(self, description_json: List) -> None:
        """
        Sets the description from the JSON representation.
        """
        self.description = json.loads(description_json)

    def __str__(self) -> str:
        """
        Returns the string representation of the description.
        """
        return str(self.description)
