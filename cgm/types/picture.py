
from cgm.enums import *

from .base import CGMBaseType, CGMVariableType
from .integer import _I, _IX, _E, _BOOL_E
from .real import _FP
from .vdc import _VDC, _P
from .color import _CO


class _SCALING_MODE_E(_E):
    @property
    def enum_type(self):
        return SCALING_MODE_ENUM


class _SCALING_MODE(CGMBaseType):
    def extract(self):
        mode = _SCALING_MODE_E(fp=self.fp, config=self.config)
        mode_val = mode.unwrap()

        if mode_val == SCALING_MODE_ENUM.METRIC:
            self.value = (
                mode,
                _FP(fp=self.fp, config=self.config),
            )
        else:
            self.value = mode


class _SS(CGMBaseType):
    @property
    def mode(self):
        raise NotImplementedError

    def extract(self):
        size_mode = self.mode

        real_modes = [
            WIDTH_SPECIFICATION_MODE_ENUM.SCALED,
            WIDTH_SPECIFICATION_MODE_ENUM.FRACTIONAL,
            WIDTH_SPECIFICATION_MODE_ENUM.MM,
        ]

        if size_mode == WIDTH_SPECIFICATION_MODE_ENUM.ABSOLUTE:
            self.value = _VDC(fp=self.fp, config=self.config)
        elif size_mode in real_modes:
            self.value = _R(fp=self.fp, config=self.config)
        else:
            raise ValueError(f'Bad WIDTH_SPECIFICATION_MODE_ENUM: {size_mode})')


class _LINE_WIDTH_SPECIFICATION_MODE(_E):
    @property
    def enum_type(self):
        return WIDTH_SPECIFICATION_MODE_ENUM


_MARKER_SIZE_SPECIFICATION_MODE = _LINE_WIDTH_SPECIFICATION_MODE
_EDGE_WIDTH_SPECIFICATION_MODE = _LINE_WIDTH_SPECIFICATION_MODE
_INTERIOR_STYLE_SPECIFICATION_MODE = _LINE_WIDTH_SPECIFICATION_MODE

_CLIP_INDICATOR = _BOOL_E
_EDGE_VISIBILITY = _BOOL_E


class _LINE_WIDTH(_SS):
    @property
    def mode(self):
        return self.config.LINE_WIDTH_SPECIFICATION_MODE


_LINE_REPRESENTATION = _LINE_WIDTH
_LINE_AND_EDGE_TYPE_DEFINITION = _LINE_WIDTH


class _MARKER_SIZE(_SS):
    @property
    def mode(self):
        return self.config.MARKER_SIZE_SPECIFICATION_MODE


_MARKER_REPRESENTATION = _MARKER_SIZE


class _EDGE_WIDTH(_SS):
    @property
    def mode(self):
        return self.config.EDGE_WIDTH_SPECIFICATION_MODE


_EDGE_REPRESENTATION = _EDGE_WIDTH


class _PATTERN_SIZE(_SS):
    @property
    def mode(self):
        return self.config.INTERIOR_STYLE_SPECIFICATION_MODE


_HATCH_STYLE_DEFINITION = _PATTERN_SIZE
_INTERPOLATED_INTERIOR = _PATTERN_SIZE



class _INTERIOR_STYLE(_E):
    @property
    def enum_type(self):
        return INTERIOR_STYLE_ENUM


class _POLYLINE(CGMVariableType):
    def extract_items(self):
        return _P(fp=self.fp, config=self.config)


class _POLYGON(CGMVariableType):
    def extract_items(self):
        return _P(fp=self.fp, config=self.config)


class _PATTERN_TABLE(CGMBaseType):
    def extract(self):
        args = {
            'fp': self.fp,
            'config': self.config,
        }
        self.value = {
            'index': _IX(**args),
            'nx': _I(**args),
            'ny': _I(**args),
            'color_precision': _I(**args),
        }

        # temporarily override color precision
        nx = self.value['nx'].unwrap()
        ny = self.value['ny'].unwrap()
        local_precision = self.value['color_precision'].unwrap()
        orig_precision = self.config.COLOR_PRECISION
        self.config.COLOR_PRECISION = local_precision

        patdef = []
        for i in range(nx):
            row = []
            for j in range(ny):
                row.append(_CO(**args))
            patdef.append(tuple(row))

        self.value['pattern'] = tuple(patdef)

        # Restore the global color precision setting
        self.config.COLOR_PRECISION = orig_precision


__all__ = [
    '_SCALING_MODE',
    '_SS',
    '_LINE_WIDTH_SPECIFICATION_MODE',
    '_MARKER_SIZE_SPECIFICATION_MODE',
    '_EDGE_WIDTH_SPECIFICATION_MODE',
    '_INTERIOR_STYLE_SPECIFICATION_MODE',
    '_CLIP_INDICATOR',
    '_EDGE_VISIBILITY',
    '_LINE_WIDTH',
    '_LINE_REPRESENTATION',
    '_LINE_AND_EDGE_TYPE_DEFINITION',
    '_MARKER_SIZE',
    '_MARKER_REPRESENTATION',
    '_EDGE_WIDTH',
    '_EDGE_REPRESENTATION',
    '_PATTERN_SIZE',
    '_HATCH_STYLE_DEFINITION',
    '_INTERPOLATED_INTERIOR',
    '_INTERIOR_STYLE',
    '_POLYLINE',
    '_POLYGON',
    '_PATTERN_TABLE',
]
