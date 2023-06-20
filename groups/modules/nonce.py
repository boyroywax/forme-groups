from typing import List, Optional

from groups.modules.nonce_unit import NonceUnit


class Nonce():
    """
    An Item's complete nonce
    Comprises of a list of nonce units
    """
    nonce_units: List

    def __init__(self, nonce_list: Optional[List] = None) -> None:
        """
        Constructor for the Nonce class.
        """
        if nonce_list is None:
            self.nonce_units: List = []
        else:
            self.nonce_units: List[NonceUnit] = nonce_list

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

    def get_nonce_length(self) -> int:
        """
        Returns the length of the nonce.
        """
        return len(self.nonce_units)

    def add_nonce_unit(self, nonce_unit: NonceUnit) -> None:
        """
        Adds a nonce unit to the nonce.
        """
        self.nonce_units.append(nonce_unit)

    def remove_nonce_unit(self, nonce_unit_index: int) -> None:
        """
        Removes a nonce unit from the nonce.
        """
        del self.nonce_units[nonce_unit_index]

    def __str__(self) -> str:
        """
        Returns the string representation of the nonce.
        """
        nonce_string: str = ""
        i: int = 0
        for nonce_unit in self.nonce_units:
            if i != 0:
                nonce_string += "."
            nonce_string += str(nonce_unit.get_nonce_unit_value())
            i += 1
        return nonce_string
    
    def __json__(self) -> dict:
        """
        Returns the JSON representation of the nonce.
        """
        nonce_strings_json: dict = {}
        i: int = 0
        for nonce_unit in self.nonce_units:
            nonce_strings_json[i] = nonce_unit.__json__()
            i += 1

        return nonce_strings_json
