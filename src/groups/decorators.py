def check_frozen(cls):
    """
    Check if the class is frozen.
    """
    def wrapper(self, *args, **kwargs):
        if self._frozen:
            raise Exception("Cannot modify frozen class.")
        return cls(self, *args, **kwargs)
    return wrapper