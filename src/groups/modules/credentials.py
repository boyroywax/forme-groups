import json
from typing import List, Optional

class Credentials():
    """
    This class is used to create and manage a user's credentials.
    """
    def __init__(self, verified_credentials: Optional[List] = None) -> None:
        """
        Constructor for the Credentials class.
        """
        if verified_credentials is None:
            self.verified_credentials: List = []
        else:
            self.verified_credentials: List = verified_credentials

    def get_verified_credentials(self) -> List:
        """
        Returns the verified credentials.
        """
        return self.verified_credentials

    def set_verified_credentials(self, verified_credentials: List) -> None:
        """
        Sets the verified credentials.
        """
        self.verified_credentials = verified_credentials

    def add_verified_credential(self, verified_credential: str) -> None:
        """
        Adds a verified credential.
        """
        self.verified_credentials.append(verified_credential)

    def remove_verified_credential(self, verified_credential_index: int) -> None:
        """
        Removes a verified credential.
        """
        del self.verified_credentials[verified_credential_index]

    def get_verified_credential(self, verified_credential_index: int) -> str:
        """
        Returns a verified credential.
        """
        return self.verified_credentials[verified_credential_index]

    def get_verified_credential_length(self) -> int:
        """
        Returns the length of the verified credentials.
        """
        return len(self.verified_credentials)

    def get_verified_credential_index(self, verified_credential: str) -> int:
        """
        Returns the index of a verified credential.
        """
        return self.verified_credentials.index(verified_credential)

    def __json__(self) -> dict:
        """
        Returns the JSON representation of a Credentials object.
        """
        return {
            "verified_credentials": self.verified_credentials
        }

    def __str__(self) -> str:
        """
        Returns the string representation of a Credentials object.
        """
        return json.dumps({
            "verified_credentials": self.verified_credentials
        })
