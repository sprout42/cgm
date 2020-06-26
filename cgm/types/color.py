
from cgm.enums import *

from .base import CGMBaseType
from .integer import _UI, _E
from .real import _R


class _COLOR_SELECTION_MODE(_E):
    @property
    def enum_type(self):
        return COLOR_SELECTION_MODE_ENUM


_COLOUR_SELECTION_MODE = _COLOR_SELECTION_MODE


# COLOR (COLOUR) INDEX
class _CI(_UI):
    @property
    def precision(self):
        return self.config.COLOR_INDEX_PRECISION


# (direct) COLOR (COLOUR) PRECISION
class _CCO(_UI):
    @property
    def precision(self):
        return self.config.COLOR_PRECISION


class _CD(CGMBaseType):
    def _word_align(self):
        pass

    def extract(self):
        cm = self.config.COLOR_MODEL
        if cm == COLOR_MODEL_ENUM.RGB:
            # Extract 3 CCO elements
            self.value = (
                _CCO(fp=self.fp, config=self.config),
                _CCO(fp=self.fp, config=self.config),
                _CCO(fp=self.fp, config=self.config),
            )
        elif cm == COLOR_MODEL_ENUM.CMYK:
            # Extract 4 CCO elements
            self.value = (
                _CCO(fp=self.fp, config=self.config),
                _CCO(fp=self.fp, config=self.config),
                _CCO(fp=self.fp, config=self.config),
                _CCO(fp=self.fp, config=self.config),
            )
        else:
            raise ValueError(f'Bad COLOR_MODEL for {self.__class__}: {cm}')


# COLOR (COLOUR) PRECISION (depending on color selection mode)
class _CO(CGMBaseType):
    def extract(self):
        csm = self.config.COLOR_SELECTION_MODE
        if csm == COLOR_SELECTION_MODE_ENUM.INDEXED:
            self.value = _CI(fp=self.fp, config=self.config)
        elif csm == COLOR_SELECTION_MODE_ENUM.DIRECT:
            self.value = _CD(fp=self.fp, config=self.config)
        else:
            raise ValueError(f'Bad COLOR_SELECTION_MODE_ENUM: {csm})')


class _COLOR_VALUE_EXTENT(CGMBaseType):
    def extract(self):
        cm = self.config.COLOR_MODEL
        if cm in [COLOR_MODEL_ENUM.RGB, COLOR_MODEL_ENUM.CMYK]:
            # If COLOR_MODEL is RGB or CMYK extract 2 "DIRECT COLOR" values, 
            # first one is "min" second one is "max"
            self.value = {
                'min': _CD(fp=self.fp, config=self.config),
                'max': _CD(fp=self.fp, config=self.config),
            }
        elif cm in [COLOR_MODEL_ENUM.CIELAB, COLOR_MODEL_ENUM.CIELUV, COLOR_MODEL_ENUM.RGB_related]:
            self.value = {
                'scale': [],
                'offset': [],
            }

            # Otherwise extract 3 pairs of "real" values
            self.value['scale'].append(_R(fp=self.fp, config=self.config))
            self.value['offset'].append(_R(fp=self.fp, config=self.config))
            self.value['scale'].append(_R(fp=self.fp, config=self.config))
            self.value['offset'].append(_R(fp=self.fp, config=self.config))
            self.value['scale'].append(_R(fp=self.fp, config=self.config))
            self.value['offset'].append(_R(fp=self.fp, config=self.config))
        else:
            raise ValueError(f'Bad COLOR_MODEL_ENUM: {cm})')

        # This type is a top-level type so make sure the file is word aligned at 
        # the end
        self.fp.next()


_COLOUR_VALUE_EXTENT = _COLOR_VALUE_EXTENT


__all__ = [
    '_COLOUR_SELECTION_MODE',
    '_COLOR_SELECTION_MODE',
    '_CI',
    '_CCO',
    '_CO',
    '_CD',
    '_COLOR_VALUE_EXTENT',
    '_COLOUR_VALUE_EXTENT',
]
