import json
from typing import Optional


class DecentralizedId():
    """
    This class is used to create and manage a decentralized ID for the user.
    """

    def __init__(self, did: str) -> None:
        """
        Constructor for the DecentralizedId class.
        """
        if did is None:
            raise ValueError("DID cannot be None.")
        else:
            self.did: Optional[str] = did

    def get_did(self) -> Optional[str]:
        """
        Returns the DID.
        """
        return self.did

    def set_did(self, did: str) -> None:
        """
        Sets the DID.
        """
        self.did = did

    def __str__(self) -> str:
        """
        Returns the string representation of the DecentralizedId object.
        """
        return self.did

    def __json__(self) -> dict:
        """
        Returns the JSON representation of the DecentralizedId object.
        """
        return json.dumps({ "did": self.did })