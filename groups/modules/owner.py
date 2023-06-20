from decentralized_id import DecentralizedId


class Owner():
    """
    The Owner class manages an owner of a Universal Object.
    """

    def __init__(self, did: DecentralizedId) -> None:
        """
        Constructor for the Owner class.
        """
        self.did: DecentralizedId = did

