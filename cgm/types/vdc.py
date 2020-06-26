
from cgm.enums import *

from .base import CGMBaseType
from .integer import _I, _E
from .real import _R, _REAL_MODE_E


class _VDC_TYPE(_E):
    @property
    def enum_type(self):
        return VDC_TYPE_ENUM

class _VDC_SI(_I):
    @property
    def precision(self):
        return self.config.VDC_INTEGER_PRECISION


class _VDC_R(_R):
    @property
    def precision(self):
        return self.config.VDC_REAL_PRECISION


# VDC (Virtual Device Coordinates) INTEGER
class _VDC(CGMBaseType):
    def extract(self):
        vdct = self.config.VDC_TYPE
        if vdct == VDC_TYPE_ENUM.INTEGER:
            self.value = _VDC_SI(fp=self.fp, config=self.config)
        elif vdct == VDC_TYPE_ENUM.REAL:
            self.value = _VDC_R(fp=self.fp, config=self.config)
        else:
            raise ValueError(f'Bad VDC_TYPE_ENUM: {vdct})')


class _P(CGMBaseType):
    def extract(self):
        self.value = (
            _VDC(fp=self.fp, config=self.config),
            _VDC(fp=self.fp, config=self.config),
        )


class _VDC_REAL_PRECISION(CGMBaseType):
    def extract(self):
        self.value = (
            _REAL_MODE_E(fp=self.fp, config=self.config),
            _I(fp=self.fp, config=self.config),
            _I(fp=self.fp, config=self.config),
        )


# _VDC_SI and _VDC_R are only used internally to the VDC types so they are not 
# exported
__all__ = [
    '_VDC_TYPE',
    '_VDC',
    '_P',
    '_VDC_REAL_PRECISION',
]
