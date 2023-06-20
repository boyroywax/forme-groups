import json
from typing import Dict

from groups.modules.nonce import Nonce
from groups.modules.owner import Owner
from groups.modules.credentials import Credentials
from groups.modules.generic_data import GenericData


class UniversalObject():
    """
    Universal serializable object
    """

    def __init__(
            self,
            nonce: Nonce,
            data: GenericData,
            owner: Owner,
            creds: Credentials
    ) -> None:
        """
        Constructor for the UniversalObject class.
        """
        self.name: str = "UniversalObject"
        self.description: str = "Universal serializable object"
        self.owner: Owner = owner
        self.nonce: Nonce = nonce
        self.data: GenericData = data
        self.creds: Credentials = creds

    def get_name(self) -> str:
        """
        Returns the name of the object.
        """
        return self.name

    def get_description(self) -> str:
        """
        Returns the description of the object.
        """
        return self.description

    def get_owner(self) -> Owner:
        """
        Returns the owner of the object.
        """
        return self.owner

    def get_nonce(self) -> Nonce:
        """
        Returns the nonce of the object.
        """
        return self.nonce

    def get_data(self) -> GenericData:
        """
        Returns the data of the object.
        """
        return self.data

    def get_creds(self) -> Credentials:
        """
        Returns the credentials of the object.
        """
        return self.creds

    def set_name(self, name: str) -> None:
        """
        Sets the name of the object.
        """
        self.name = name

    def set_description(self, description: str) -> None:
        """
        Sets the description of the object.
        """
        self.description = description

    def set_owner(self, owner: Owner) -> None:
        """
        Sets the owner of the object.
        """
        self.owner = owner

    def set_nonce(self, nonce: Nonce) -> None:
        """
        Sets the nonce of the object.
        """
        self.nonce = nonce

    def set_data(self, data: GenericData) -> None:
        """
        Sets the data of the object.
        """
        self.data = data

    def set_creds(self, creds: Credentials) -> None:
        """
        Sets the credentials of the object.
        """
        self.creds = creds

    def __json__(self) -> Dict:
        """
        Returns the JSON representation of the object.
        """
        return {
            "name": self.name,
            "description": self.description,
            "owner": self.owner.__str__(),
            "nonce": self.nonce.__str__(),
            "data": self.data.__str__(),
            "creds": self.creds.__str__()
        }

    def __str__(self) -> str:
        """
        Returns the string representation of the object.
        """
        return json.dumps(self.__json__(), indent=4, sort_keys=True)
