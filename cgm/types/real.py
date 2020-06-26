
from decimal import Decimal

from cgm.enums import *

from .base import CGMBaseType
from .integer import _I, _E


class _REAL_MODE_E(_E):
    @property
    def enum_type(self):
        return REAL_MODE_ENUM


class _REAL_PRECISION(CGMBaseType):
    def extract(self):
        self.value = (
            _REAL_MODE_E(fp=self.fp, config=self.config),
            _I(fp=self.fp, config=self.config),
            _I(fp=self.fp, config=self.config),
        )


class _R(CGMBaseType):
    @property
    def precision(self):
        return self.config.REAL_PRECISION

    def convert(self, in_bytes):
        prec = self.precision
        return prec(in_bytes)

    def extract(self):
        self.param_len = self.precision.value // 8
        self.raw = self.fp.read(self.param_len)
        self.value = self.convert(self.raw)


# Floating point real
class _FP(_R):
    _default_real_prec_config = \
            REAL_PRECISION_CONFIG((REAL_MODE_ENUM.FLOATING, 9, 23))

    @property
    def precision(self):
        config_prec = self.config.REAL_PRECISION
        default_prec = self._default_real_prec_config

        if config_prec._mode != default_prec._mode:
            # If the current configured mode is not the same as the required 
            # mode (FLOATING), then use the default precision
            return default_prec
        else:
            # Otherwise use the precision from the config
            return config_prec


# Fixed point real
class _FX(_FP):
    _default_real_prec_config = \
            REAL_PRECISION_CONFIG((REAL_MODE_ENUM.FIXED, 16, 16))


__all__ = [
    '_REAL_MODE_E',
    '_REAL_PRECISION',
    '_R',
    '_FP',
    '_FX',
]
