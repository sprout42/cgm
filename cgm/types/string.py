from cgm.utils import word
from .base import CGMBaseType, CGMLengthType


class _SF(CGMLengthType):
    def extract_item(self):
        data = self.fp.read(self.param_len)
        self.value = data.decode('latin-1')


class _S(CGMBaseType):
    def extract(self):
        # Variable length string that is null terminated
        self.raw = b''
        char = self.fp.read(1)
        while char != b'\x00':
            self.raw += char
            char = self.fp.read(1)
        self.value = self.raw.decode('latin-1')


class _D(CGMLengthType):
    def extract_item(self):
        self.raw = self.fp.read(self.param_len)

        # Make the "value" to be a printing/json-izable friendly value
        self.value = self.raw.hex()

    def __str__(self):
        if self.complete:
            return f'{self.__class__.__name__}({self.value.hex()})'
        else:
            return f'{self.__class__.__name__} INCOMPLETE ({self.value.hex()})'


__all__ = [
    '_SF',
    '_S',
    '_D',
]
