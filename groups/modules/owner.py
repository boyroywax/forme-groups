import json

from groups.modules.decentralized_id import DecentralizedId


class Owner():
    """
    The Owner class manages an owner of a Universal Object.
    """

    def __init__(self, did: DecentralizedId) -> None:
        """
        Constructor for the Owner class.
        """
        self.did: DecentralizedId = did

    def get_did(self) -> DecentralizedId:
        """
        Returns the DID of the owner.
        """
        return self.did

    def set_did(self, did: DecentralizedId) -> None:
        """
        Sets the DID of the owner.
        """
        self.did = did

    def __json__(self) -> str:
        """
        Returns the JSON representation of the Owner object.
        """
        return {
            "did": self.did.__str__()
        }

    def __str__(self) -> str:
        """
        Returns the string representation of the Owner object.
        """
        return json.dumps({
            "did": self.did.__str__()
        })
