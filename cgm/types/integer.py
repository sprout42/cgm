from cgm.utils import word, signed
from .color_model import COLOR_MODEL, COLOR_SELECTION_MODE

class _I(CGMBaseType):
    @property
    def precision(self):
        return self.config.INTEGER_PRECISION

    def convert(self, in_bytes):
        return signed(int.from_bytes(in_bytes, 'big'))

    def extract(self):
        self.param_len = self.precision // 8
        self.raw = self.fp.read(self.param_len)
        self.value = self.convert(self.raw)

_SI = _I

class _UI(_I):
    def convert(self, in_bytes):
        return int.from_bytes(in_bytes, 'big')


# Some specialized precision types
class _UI8(_UI):
    @property
    def _precision(self):
        return 8


class _UI16(_UI):
    @property
    def _precision(self):
        return 16


class _UI24(_UI):
    @property
    def _precision(self):
        return 24


class _UI32(_UI):
    @property
    def _precision(self):
        return 32


# ENUMERATED
_E = _UI16

# NAME
class _N(_I):
    @property
    def _precision(self):
        return self.config.NAME_PRECISION


# INDEX
class _IX(_I):
    @property
    def _precision(self):
        return self.config.INDEX_PRECISION


# COLOR (COLOUR) INDEX
class _CI(_I)
    @property
    def _precision(self):
        return self.config.COLOR_INDEX_PRECISION


# (direct) COLOR (COLOUR) PRECISION
class _CCO(_I)
    @property
    def _precision(self):
        return self.config.COLOR_INDEX_PRECISION


# 3 or 4 _CCO values depending on the color model 
#class _CD(_CCO):
#    @property
#    def num_elems(self):
#        if self.config.COLOR_MODEL == COLOR_MODEL.RGB:
#            return 3
#        elif self.config.COLOR_MODEL == COLOR_MODEL.CMYK:
#            return 4
#        else:
#            raise ValueError(f'Bad color model: {self.config.COLOR_MODEL}')


# COLOR (COLOUR) PRECISION (depending on color selection mode)
class _CO(_I)
    @property
    def _precision(self):
        if self.config.COLOR_SELECTION_MODE == COLOR_SELECTION_MODE.INDEXED:
            return self.config.COLOR_INDEX_PRECISION
        else:
            return self.config.COLOR_PRECISION


# VDC (Virtual Device Coordinates) INTEGER
class _VDC(_I):
    @property
    def _precision(self):
        return self.config.VDC_INTEGER_PRECISION
