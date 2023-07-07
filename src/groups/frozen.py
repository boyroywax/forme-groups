from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from .decorators import check_frozen


@dataclass(slots=True)
class FrozenInterface(ABC):
    """
    The interface for the Frozen class.
    """

    @property
    @abstractmethod
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        pass

    @abstractmethod
    def freeze(self) -> None:
        """
        Freeze the class.
        """
        pass


# @dataclass(slots=True)
class Frozen(FrozenInterface):
    """
    This class manages the frozen state of a class.
    """

    _frozen: bool = field(default_factory=bool)

    def __init__(self, frozen: bool = False) -> None:
        """
        Initialize the class.
        """
        self._frozen = frozen

    @property
    def frozen(self) -> bool:
        """
        Check if the class is frozen.
        """
        return self._frozen

    @frozen.setter
    @check_frozen
    def frozen(self, frozen: bool) -> None:
        """
        Set the frozen state of the class.
        """
        raise AttributeError("Cannot set 'frozen' attribute. Use 'freeze' method instead.")

    @check_frozen
    def freeze(self) -> None:
        """
        Freeze the class.
        """
        self._frozen = True
