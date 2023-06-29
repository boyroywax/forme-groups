from dataclasses import dataclass, field, fields
from typing import Any, Dict, List, Optional

from ..type import Type_ as BaseType
from ..type._unit import Unit_ as SuperUnit


@dataclass(
    # slots=True,
)
class BaseUnit(SuperUnit):
    """
    This is the base class for all units.
    All units are dataclasses.
    All units are initialized with a 'value' and a 'base_type'.
    """
    # _base_type: Optional[BaseType] = field(default_factory=BaseType)
    _base_type: Optional[BaseType] = None

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseUnit class.
        * Receives 'args' and 'kwargs'.

        :param args: The arguments to initialize the BaseUnit class.
        :type args: Tuple[Any]
        :info: The first argument is the 'value'. The second argument is the 'base_type'.

        :param kwargs: The keyword arguments to initialize the BaseUnit class.
        :type kwargs: Dict[str, Any]
        :info: The 'value' can be provided as a keyword argument.
        :info: The 'base_type' can be provided as a keyword argument.

        """
        SuperUnit.__init__(self, *args, **kwargs)
        self.__post__init__(*args, **kwargs)

    def __post__init__(self, *args, **kwargs):
        """
        Post Initializes the BaseUnit class.
        * Receives 'args' and 'kwargs'.
        """
        self._base_type: Optional[BaseType] = None
        print(f'args - {args}')
        if (
            len(args) > 0 and
            args[1] is not None and
            isinstance(args[1], BaseType) and
            'base_type' not in kwargs
            # self.base_type is None
        ):
            print(f"Post Init - args - {args}")
            self.base_type = args[1]
        elif (
            'base_type' in kwargs and
            isinstance(kwargs['base_type'], BaseType)
            # self.base_type is None
        ):
            self.base_type = kwargs["base_type"]
        else:
            self.base_type = BaseType()

        

        print("Post Init complete")
        print(self._base_type)

    # @property
    # def value(self) -> Any:
    #     """
    #     The value of the base object.
    #     """
    #     return self.super().value
    
    # @property
    # def _base_type(self) -> Optional[BaseType]:
    #     """
    #     The base type of the base object.
    #     """
    #     return self._base_type

    @property
    def base_type(self) -> Optional[BaseType]:
        """
        The base type of the base object.
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base: BaseType) -> None:
        """
        Sets the base type of the base object.
        """
        self._base_type = base

    @base_type.getter
    def base_type(self) -> BaseType:
        """
        Gets the base type of the base object.
        """
        return self._base_type

    @property
    def id_(self) -> BaseType:
        """
        The id of the base object.
        """
        return self._base_type.id_
        # return fields(BaseType)[0].default_factory(BaseType).value

    @id_.setter
    def id_(self, id: Any) -> None:
        """
        Sets the id of the base object.
        """
        self._base_type.id.value = id

    @id_.getter
    def id_(self) -> Any:
        """
        Gets the id of the base object.
        """
        return self._base_type.id_.value
        fields(BaseType)[0].init
        # return fields(BaseType)[0].default_factory(BaseType).value

    @property
    def alias(self) -> Any:
        """
        The alias of the group object.
        """
        return self._base_type.alias.value
        # return fields(BaseType)[1].default_factory(BaseType).value

    @property
    def super_(self) -> Any:
        """
        The super of the group object.
        """
        return self._base_type.super_.value

    @property
    def prefix(self) -> Any:
        """
        The prefix of the group object.
        """
        return self._base_type.prefix.value

    @property
    def suffix(self) -> Any:
        """
        The suffix of the group object.
        """
        return self._base_type.suffix.value

    @property
    def separator(self) -> Any:
        """
        The separator of the group object.
        """
        return self._base_type.separator.value

    @property
    def function_(self) -> Any:
        """
        The function of the group object.
        """
        # return fields(BaseType)[6].default_factory(BaseType).value
        return self._base_type.function_.value

    # def to_dict(self) -> Dict[str, Any]:
    #     """
    #     Converts the base object to a dictionary.
    #     """
    #     return self.base_type.to_dict()

    # @property
    # def value(self) -> Any:
    #     """
    #     The value of the base object.
    #     """
    #     return SuperUnit().value
    
    # @value.setter
    # def value(self, value: Any) -> None:
    #     """
    #     Sets the value of the base object.
    #     """
    #     self.super().value = value

    # @value.getter
    # def value(self) -> Any:
    #     """
    #     Gets the value of the base object.
    #     """
    #     return self.super().value
    
    # def __repr__(self) -> str:
    #     """
    #     Returns the representation of the base object.
    #     """
    #     return 'BaseUnit(value={value}, base_type={base_type})'.format(
    #         value=self.value,
    #         base_type=self._base_type
    #     )
