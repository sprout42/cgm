
from cgm.utils import word, signed, unsigned
from cgm.enums import *

from .base import CGMBaseType

class _I(CGMBaseType):
    def _word_align(self):
        pass

    @property
    def precision(self):
        return self.config.INTEGER_PRECISION

    def convert(self, in_bytes):
        return signed(int.from_bytes(in_bytes, 'big'), self.precision)

    def extract(self):
        self.param_len = self.precision // 8
        self.raw = self.fp.read(self.param_len)
        self.value = self.convert(self.raw)

_SI = _I


# Some specialized precision types
class _IF8(_I):
    @property
    def precision(self):
        return 8


class _IF16(_I):
    @property
    def precision(self):
        return 16


class _IF24(_I):
    @property
    def precision(self):
        return 24


class _IF32(_I):
    @property
    def precision(self):
        return 32

class _UI(_I):
    def convert(self, in_bytes):
        return unsigned(int.from_bytes(in_bytes, 'big'), self.precision)


# Some specialized precision types
class _UI8(_UI):
    @property
    def precision(self):
        return 8


class _UI16(_UI):
    @property
    def precision(self):
        return 16


class _UI24(_UI):
    @property
    def precision(self):
        return 24


class _UI32(_UI):
    @property
    def precision(self):
        return 32


# ENUMERATED
class _E(_UI16):
    @property
    def enum_type(self):
        raise NotImplementedError

    def extract(self):
        super().extract()
        # For enum types make the "value" be the enumerated value and the 
        # "intval" be the raw integer value
        self.intval = self.value
        self.value = self.enum_type(self.value)

    def __str__(self):
        return f'{self.__class__.__name__}({self.value.name}({self.intval}))'


class _BOOL_E(_E):
    @property
    def enum_type(self):
        return BOOL_ENUM


# NAME
class _N(_I):
    @property
    def precision(self):
        return self.config.NAME_PRECISION


# INDEX
class _IX(_I):
    @property
    def precision(self):
        return self.config.INDEX_PRECISION


__all__ = [
    '_I',
    '_SI',
    '_IF8',
    '_IF16',
    '_IF24',
    '_IF32',
    '_UI',
    '_UI8',
    '_UI16',
    '_UI24',
    '_UI32',
    '_E',
    '_BOOL_E',
    '_N',
    '_IX',
]
