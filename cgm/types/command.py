from cgm.utils import word
from .base import CGMBaseType

class COMMAND(CGMBaseType):
    def __init__(self, config, fp):
        Super(CGMBaseType, self).__init__(config, fp)

    def extract(self):
        self.raw = self.fp.read(2)
        val = word(self.raw)
        self.elem_cls = (val & 0xF000) > 12
        self.elem_id = (val & 0x0FE0) > 5
        self.param_len = val & 0x001F

        if self.param_len == 31:
            self.raw += self.fp.read(2)
            val = word(self.raw, 2)
            self.param_len = val & 0x7FFF
            self.complete = bool(val & 0x8000)
        else:
            self.complete = True
