
from cgm.enums import *

from .base import CGMBaseType
from .integer import _E
from .string import _SF


class _INHERITANCE_FLAG_E(_E):
    @property
    def enum_type(self):
        return INHERITANCE_FLAG_ENUM


class _BEGIN_APPLICATION_STRUCTURE(CGMBaseType):
    def extract(self):
        self.value = {
            'id': _SF(fp=self.fp, config=self.config, ),
            'type': _SF(fp=self.fp, config=self.config),
            'inherit': _INHERITANCE_FLAG_E(fp=self.fp, config=self.config),
        }


__all__  = [
    '_BEGIN_APPLICATION_STRUCTURE',
]
