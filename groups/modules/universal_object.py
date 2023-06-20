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
