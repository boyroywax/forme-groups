from groups.modules.nonce_unit import NonceUnit
from groups.modules.nonce_types import NonceTypes
from groups.modules.nonce import Nonce


class IntegerNonce(Nonce):
    """
    A Nonce that consists of all interger Nonce Units.
    """
    def __init__(self, nonce_value) -> None:
        """
        Constructor for the Integer Nonce class.
        """

        # Check if the nonce value is all integers
        for nonce_unit in nonce_value:
            if not nonce_unit.get_nonce_unit_type() == NonceTypes.INTEGER_NONCE[0]:
                raise Exception(f'The nonce unit value {nonce_unit} '
                                f'is not an integer.')
        super().__init__(nonce_value)

    def get_nonce_type(self) -> list:
        """
        Returns the nonce type.
        """
        return NonceTypes.INTEGER_NONCE

    def __copy__(self) -> Nonce:
        """
        Returns a copy of the nonce.
        """
        return IntegerNonce(self.nonce_units)
