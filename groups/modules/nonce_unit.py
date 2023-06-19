from groups.modules.nonce_types import NonceTypes


class NonceUnit():
    """
    This class manages a Nonce Unit.
    """

    def __init__(self, nonce_unit_value, nonce_unit_type) -> None:
        """
        Constructor for the Nonce Unit class.
        Checks the nonce unit type to make sure it is valid.
        """
        if not self.validate_nonce_unit_type(nonce_unit_value, nonce_unit_type):
            raise Exception(f'The nonce unit type {nonce_unit_type} '
                            f'is not valid for the nonce unit value '
                            f'{nonce_unit_value}.')

        nonce_unit_type = NonceTypes(nonce_unit_type)

        if nonce_unit_type.get_active_nonce_type() == 'unknown':
            raise Exception(f'The nonce unit type {nonce_unit_type} '
                            f'is not supported.')

        self.nonce_unit_value = nonce_unit_value
        self.nonce_unit_type: NonceTypes = nonce_unit_type

    def get_nonce_unit_value(self) -> str:
        """
        Returns the nonce unit value.
        """
        return self.nonce_unit_value

    def get_nonce_unit_type(self) -> str:
        """
        Returns the nonce unit type.
        """
        return self.nonce_unit_type.get_active_nonce_type()

    def set_nonce_unit(self, nonce_unit_value):
        """
        Sets the nonce.
        """
        self.nonce_unit_value = nonce_unit_value

    def set_nonce_unit_type(self, nonce_unit_type) -> None:
        """
        Sets the nonce type.
        """
        self.nonce_unit_type = nonce_unit_type

    def validate_nonce_unit_type(self, nonce_unit_value, nonce_unit_type) -> bool:
        """
        Validates the nonce unit type.
        """
        nonce_unit_type = NonceTypes(nonce_unit_type)

        if nonce_unit_type.get_active_nonce_type() == 'unknown':
            raise Exception(f'The nonce unit type {nonce_unit_type} '
                            f'is not supported.')

        match nonce_unit_type.get_active_nonce_type():
            case 'string':
                return isinstance(nonce_unit_value, str)
            case 'integer':
                return isinstance(nonce_unit_value, int)
            case 'float':
                return isinstance(nonce_unit_value, float)
            case 'boolean':
                return isinstance(nonce_unit_value, bool)
            case 'list':
                return isinstance(nonce_unit_value, list)
            case 'tuple':
                return isinstance(nonce_unit_value, tuple)
            case 'dictionary':
                return isinstance(nonce_unit_value, dict)
            case _:
                return False

    def __str__(self) -> str:
        """
        Returns the nonce unit as a string.
        """
        match self.nonce_unit_type:
            case 'string':
                return f'{self.nonce_unit}'
            case 'integer':
                return f'{self.nonce_unit}'
            case 'float':
                return f'{self.nonce_unit}'
            case 'boolean':
                return f'{self.nonce_unit}'
            case 'list':
                return f'{self.nonce_unit}'
            case 'tuple':
                return f'{self.nonce_unit}'
            case 'dictionary':
                return f'{self.nonce_unit}'

    def __repr__(self) -> str:
        return self.__str__()

    def __json__(self) -> dict:
        return {
            'nonce_unit': self.nonce_unit,
            'nonce_unit_type': self.nonce_unit_type
        }

    def __eq__(self, other: 'NonceUnit') -> bool:
        return self.__json__() == other.__json__()

    def __hash__(self) -> int:
        return hash(str(self.__json__()))

    def __copy__(self) -> 'NonceUnit':
        return NonceUnit(self.nonce_unit, self.nonce_unit_type)
