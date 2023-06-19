from typing import Dict, Optional
import numbers


class NonceTypes():
    """
    A class that holds the different types of nonce that can be used
    """
    
    INTEGER_NONCE = ["integer"]
    NUMERIC_NONCE = ["integer", "float", "decimal"]
    STRING_NONCE = ["string", "hexadecimal", "binary", "decimal"]

    def __init__(self, nonce_type: Optional[str] = None) -> None:
        """
        Initialize the nonce types.
        """
        self.nonce_types: Dict = {
            'string': 'string',
            'integer': 'integer',
            'float': 'float',
            'boolean': 'boolean',
            'list': 'list',
            'tuple': 'tuple',
            'dictionary': 'dictionary',
            'hexadecimal': 'hex',
            'binary': 'binary',
            'decimal': 'decimal',
            'unknown': 'unknown'
        }
        self.active_type: Optional[str] = None

        if nonce_type is not None:
            self.set_active_nonce_type(nonce_type)

    def get_nonce_types(self) -> dict:
        """
        Returns the nonce types.
        """
        return self.nonce_types
    
    def check_str_for_nonce_type(self, nonce_unit: str) -> str:
        """
        Check the nonce unit type.
        """
        if nonce_unit.startswith('0x'):
            return self.nonce_types['hexadecimal']
        elif nonce_unit.startswith('0b'):
            return self.nonce_types['binary']
        elif nonce_unit.startswith('0d'):
            return self.nonce_types['decimal']
        else:
            return self.nonce_types['string']

    def check_nonce_unit_type(self, nonce_unit) -> str:
        """
        Check the nonce unit type.
        """
        def is_int(val):
            try:
                if type(val) == int:
                    return True
            except AttributeError:
                return False

        if isinstance(nonce_unit, str):
            return self.check_str_for_nonce_type(nonce_unit)
        elif is_int(nonce_unit) and isinstance(nonce_unit, numbers.Integral):
            return self.nonce_types['integer']
        elif isinstance(nonce_unit, float):
            return self.nonce_types['float']
        elif isinstance(nonce_unit, bool):
            return self.nonce_types['boolean']
        elif isinstance(nonce_unit, list):
            return self.nonce_types['list']
        elif isinstance(nonce_unit, tuple):
            return self.nonce_types['tuple']
        elif isinstance(nonce_unit, dict):
            return self.nonce_types['dictionary']
        else:
            return self.nonce_types['unknown']

    def set_active_nonce_type(self, nonce_type: str) -> None:
        """
        Sets the active nonce type.
        """
        if nonce_type not in self.nonce_types:
            raise Exception(f'The nonce type {nonce_type} is not supported.')
        if nonce_type == 'unknown':
            raise Exception(f'The nonce type {nonce_type} is not supported.')
        self.active_type = nonce_type

    def get_active_nonce_type(self) -> Optional[str]:
        """
        Returns the active nonce type.
        """
        return self.active_type

    def __json__(self) -> dict:
        return {"active_nonce_type": self.active_type}

    def __str__(self) -> str:
        return f'{self.active_type}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'NonceTypes') -> bool:
        return self.__json__() == other

    def __ne__(self, other: 'NonceTypes') -> bool:
        return self.__json__() != other.__json__()
    
    def __hash__(self) -> int:
        return hash(str(self.__json__()))
