from typing import Any, Callable


class Checks():
    """
    Checks the system and data values for any errors.
    """

    @staticmethod
    def check_value_for_empty(value: Any) -> bool:
        """
        Checks if the value is empty or contains an empty construct.
        """
        if value is None:
            return True

        if (
            value is None or
            value == "" or
            value == "{}" or
            value == "[]" or
            value == "()" or
            value == "''" or
            value == '""' or
            value == "``" or
            value == "'''" or
            value == '"""' or
            str(value).lower() is None or
            str(value).lower() == "none" or
            str(value).lower() == "null" or
            str(value).lower() == "{}" or
            str(value).lower() == "[]" or
            str(value).lower() == "()" or
            str(value).lower() == str("") or
            str(value).lower() == str('') or
            str(value).lower() == str("''") or
            str(value).lower() == '""' or
            str(value).lower() == "``" or
            str(value).lower() == "'''"
        ):
            return True
        else:
            return False

    # @staticmethod
    # def check_supported_types(types: List[BaseType]) -> List[BaseType]:
    #     """
    #     Checks the supported system types.
    #     """
    #     supported_types: List[str] = []
    #     for type_ in types:
    #         if Checks.check_supported_system_type(type_):
    #             supported_types.append(type_)
    #     return supported_types

    @staticmethod
    def check_supported_system_type(system_function: Callable) -> bool:
        """
        Checks the supported system types.
        """
        if system_function == 'type':
            print(f'Found type: {system_function}')
        print(system_function.__name__)
        match system_function.__name__:
            case 'str':
                return True
            case 'int':
                return True
            case 'float':
                return True
            case 'bool':
                return True
            case 'list':
                return True
            case 'dict':
                return True
            case 'bytes':
                return True
            case _:
                return False

