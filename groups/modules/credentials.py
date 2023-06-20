from typing import List, Optional

class Credentials():
    """
    This class is used to create and manage a user's credentials.
    """
    def __init__(self, verified_credentials: Optional[List] = None) -> None:
        """
        Constructor for the Credentials class.
        """
        self.verified_credentials: List = []


