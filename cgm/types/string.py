from cgm.utils import word
from .base import CGMBaseType


class _SF(CGMBaseType):
    def extract(self):
        self.raw = self.fp.read(1)
        self.param_len = ord(self.raw)

        if self.param_len == 255:
            self.raw = [self.raw] + self.fp.read(2)
            val = word(self.raw, 1)
            self.param_len = val & 0x7FFF
            # 0 means this is the "last" part of the string, 1 means it is "not 
            # last"
            self.complete = not bool(val & 0x8000)
            start_offset = 3
        else:
            self.complete = True
            start_offset = 1

        self.raw += self.fp.read(self.param_len)

        val = self.raw[start_offset:start_offset + self.param_len]
        self.value = val.decode('latin-1')

    def __str__(self):
        if self.complete:
            return f'{self.__class__.__name__}({self.value})'
        else:
            return f'{self.__class__.__name__} INCOMPLETE ({self.value})'


class _S(CGMBaseType):
    def extract(self):
        # Variable length string that is null terminated
        char = self.fp.read(1)
        self.raw = b''

        while char != 0:
            self.raw += char
            char = self.fp.read(1)
            print(type(char), char)

        self.value = self.raw.decode('latin-1')

#_D = _SF

__all__ = [
    '_SF',
    '_S',
    #'_D',
]
