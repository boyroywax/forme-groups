from typing import Optional

from groups.modules.nonce_unit import NonceUnit
from groups.modules.nonce_types import NonceTypes
from groups.modules.nonce import Nonce


class IntegerNonce(Nonce):
    """
    A Nonce that consists of all interger Nonce Units.
    """
    def __init__(self, nonce_value, active_index: Optional[int] = None) -> None:
        """
        Constructor for the Integer Nonce class.
        """

        # Check if the nonce value is all integers
        for nonce_unit in nonce_value:
            if not nonce_unit.get_nonce_unit_type() == NonceTypes.INTEGER_NONCE[0]:
                raise Exception(f'The nonce unit value {nonce_unit} '
                                f'is not an integer.')
        super().__init__(nonce_value)
        self.active_nonce_unit = self.nonce_units[active_index] if active_index else self.nonce_units[0]

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

    def set_active_nonce_unit(self, nonce_unit_index) -> None:
        """
        Sets the active nonce unit.
        """
        if nonce_unit_index < 0:
            raise Exception(f'The nonce unit index {nonce_unit_index} '
                            f'is less than 0.')
        if nonce_unit_index > len(self.nonce_units):
            raise Exception(f'The nonce unit index {nonce_unit_index} '
                            f'is greater than the nonce length {len(self.nonce_units)}.')
        self.active_nonce_unit = self.nonce_units[nonce_unit_index]

    def get_active_nonce_unit(self) -> NonceUnit:
        """
        Returns the active nonce unit.
        """
        return self.active_nonce_unit

    def get_active_nonce_unit_index(self) -> int:
        """
        Returns the active nonce unit index.
        """
        return self.nonce_units.index(self.active_nonce_unit)

    def get_active_nonce_unit_value(self) -> int:
        """
        Returns the active nonce unit value.
        """
        return self.active_nonce_unit.get_nonce_unit_value()

    def get_active_nonce_unit_type(self) -> str:
        """
        Returns the active nonce unit type.
        """
        return self.active_nonce_unit.get_nonce_unit_type()

    def check_if_index_in_range(self, nonce_unit_index: int) -> bool:
        """
        Checks if the nonce unit index is in range.
        """
        return nonce_unit_index < len(self.nonce_units)

    def next_nonce_unit(self) -> None:
        """
        Sets the next nonce unit as the active nonce unit.
        """
        if self.check_if_index_in_range(self.get_active_nonce_unit_index() + 1) is False:
            raise Exception(f'The nonce unit index {self.get_active_nonce_unit_index() + 1} '
                            f'is greater than the nonce length {len(self.nonce_units)}.')
        self.active_nonce_unit = self.nonce_units[self.get_active_nonce_unit_index() + 1]

    def previous_nonce_unit(self) -> None:
        """
        Sets the previous nonce unit as the active nonce unit.
        """
        if self.check_if_index_in_range(self.get_active_nonce_unit_index() - 1) is False:
            raise Exception(f'The nonce unit index {self.get_active_nonce_unit_index() - 1} '
                            f'is less than 0.')
        self.active_nonce_unit = self.nonce_units[self.get_active_nonce_unit_index() - 1]

    def increment_active_nonce_unit(self) -> None:
        """
        Increments the active nonce unit.
        """
        self.active_nonce_unit.set_nonce_unit(self.get_active_nonce_unit_value() + 1)

    def decrement_active_nonce_unit(self) -> None:
        """
        Decrements the active nonce unit.
        """
        self.active_nonce_unit.set_nonce_unit(self.get_active_nonce_unit_value() - 1)
