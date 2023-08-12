from .logger import Log


class Base(object):
    """Base class for all classes in the project"""
    def __init__(self):
        super(Base, self).__init__()
        self.log = Log().logger
        # self.log.debug("Base class initialized")

    def __str__(self):
        return self.__class__.__name__
