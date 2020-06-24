
class CGMBaseType(object):
    def __init__(self, config, fp):
        self.config = config
        self.fp = fp
        self.offset = fp.tell()

        self.extract()

    def extract(self):
        raise NotImplementedError

    def __str__(self):
        return str(self.value)
