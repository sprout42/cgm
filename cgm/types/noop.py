from .base import CGMBaseType


class NOOP(CGMBaseType):
    def __init__(self, config, fp, param_len):
        self.param_len = param_len
        Super(CGMBaseType, self).__init__(config, fp)

    def extract(self):
        # Consume the required number of bytes
        self.raw = self.fp.read(self.param_len)
