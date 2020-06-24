
from .file import CGMFile
from .config import CGMConfig
from .types import CGMGenericType


class CGM(object):
    def __init__(self, filename):
        self.config = CGMConfig()
        self.fp = CGMFile(filename)

        self.values = None

    def parse(self):
        self.values = CGMGenericType.make(self.config, self.fp)


