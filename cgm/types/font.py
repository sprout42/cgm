
from cgm.enums import *

from .base import CGMBaseType, CGMVariableType
from .string import _SF, _S
from .integer import _E
from .real import _R
from .vdc import _P, _VDC


class _CHARACTER_SET_TYPE(_E):
    @property
    def enum_type(self):
        return CHARACTER_SET_TYPE_ENUM


class _CHARACTER_CODING_ANNOUNCER(_E):
    @property
    def enum_type(self):
        return CHARACTER_CODING_ENUM


class _FONT_LIST(CGMVariableType):
    def extract_items(self):
        return _SF(fp=self.fp, config=self.config)


class _CHARACTER_SET_LIST(CGMVariableType):
    def extract_items(self):
        item = {
            'type': _CHARACTER_SET_TYPE(fp=self.fp, config=self.config),
            'set': _SF(fp=self.fp, config=self.config),
        }
        return item


class _TEXT_PRECISION(_E):
    @property
    def enum_type(self):
        return TEXT_PRECISION_ENUM


class _TEXT_HORIZONTAL_ALIGNMENT_ENUM(_E):
    @property
    def enum_type(self):
        return HORIZONTAL_ALIGNMENT_ENUM


class _TEXT_VERTICAL_ALIGNMENT_ENUM(_E):
    @property
    def enum_type(self):
        return VERTICAL_ALIGNMENT_ENUM


class _TEXT_ALIGNMENT(CGMBaseType):
    def extract(self):
        args = {
            'fp': self.fp,
            'config': self.config,
        }
        self.value = {
            'horizontal_alignment': _TEXT_HORIZONTAL_ALIGNMENT_ENUM(**args),
            'vertical_alignment': _TEXT_VERTICAL_ALIGNMENT_ENUM(**args),
            'continuous_horizontal_alignment': _R(**args),
            'continuous_vertical_alignment': _R(**args),
        }


class _RESTRICTED_TEXT_TYPE(_E):
    @property
    def enum_type(self):
        return RESTRICTED_TEXT_TYPE_ENUM


class _FINAL_FLAG(_E):
    @property
    def enum_type(self):
        return FINAL_FLAG_ENUM


class _RESTRICTED_TEXT(CGMBaseType):
    def extract(self):
        args = {
            'fp': self.fp,
            'config': self.config,
        }
        self.value = {
            'delta_width': _VDC(**args),
            'delta_height': _VDC(**args),
            'text_position': _P(**args),
            'flag': _FINAL_FLAG(**args),
            'text': _SF(**args),
        }


__all__ = [
    '_CHARACTER_SET_TYPE',
    '_CHARACTER_CODING_ANNOUNCER',
    '_FONT_LIST',
    '_CHARACTER_SET_LIST',
    '_TEXT_PRECISION',
    '_TEXT_ALIGNMENT',
    '_RESTRICTED_TEXT_TYPE',
    '_FINAL_FLAG',
    '_RESTRICTED_TEXT',
]
