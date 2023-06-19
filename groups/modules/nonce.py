from typing import List, Optional

from groups.modules.nonce_unit import NonceUnit


class Nonce():
    """
    An Item's complete nonce
    Comprises of a list of nonce units
    """
    nonce_units: List

    def __init__(self, nonce_list: Optional[List]) -> None:
        """
        Constructor for the Nonce class.
        """
        if nonce_list is None:
            self.nonce_units: List = []
        else:
            self.nonce_units: List = nonce_list

    def get_nonce_units(self) -> List:
        """
        Returns the nonce units.
        """
        return self.nonce_units

    def get_nonce_unit(self, nonce_unit_index: int) -> NonceUnit:
        """
        Returns the nonce unit at the given index.
        """
        return self.nonce_units[nonce_unit_index]

    def get_nonce_unit_value(self, nonce_unit_index: int) -> str:
        """
        Returns the nonce unit value at the given index.
        """
        return self.nonce_units[nonce_unit_index].get_nonce_unit_value()

    def get_nonce_unit_type(self, nonce_unit_index: int) -> str:
        """
        Returns the nonce unit type at the given index.
        """
        return self.nonce_units[nonce_unit_index].get_nonce_unit_type()

    def set_nonce_unit(self, nonce_unit_index: int, nonce_unit: NonceUnit) -> None:
        """
        Sets the nonce unit at the given index.
        """
        self.nonce_units[nonce_unit_index] = nonce_unit
