
from cgm.enums import *

from .base import CGMVariableType
from .string import _SF
from .integer import _E


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



__all__ = [
    '_CHARACTER_SET_TYPE',
    '_CHARACTER_CODING_ANNOUNCER',
    '_FONT_LIST',
    '_CHARACTER_SET_LIST',
    '_TEXT_PRECISION',
]
