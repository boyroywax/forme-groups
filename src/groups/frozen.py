from abc import ABC, abstractmethod

from .decorators import check_frozen


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


class Frozen(FrozenInterface):
    """
    This class manages the frozen state of a class.
    """

    _frozen: bool

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
