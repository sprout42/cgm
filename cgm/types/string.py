from cgm.utils import word
from .base import CGMBaseType


class _SF(CGMBaseType):
    def extract(self):
        self.raw = self.fp.read(1)
        self.param_len = self.raw

        if self.value_len == 255:
            self.raw = [self.raw] + self.fp.read(2)
            val = word(self.raw, 1)
            self.param_len = val & 0x7FFF
            self.complete = bool(val & 0x8000)
            start_offset = 3
        else:
            self.complete = True
            start_offset = 1


        self.raw += self.fp.read(self.param_len)
        self.value = self.raw[start_offset:start_offset + self.param_len]
