
import enum
import struct


# A basic enumerated type
class BOOL_ENUM(enum.IntEnum):
    OFF = 0
    ON = 1


class REAL_MODE_ENUM(enum.IntEnum):
    FLOATING = 0
    FIXED = 1


# Not really an enum, but fulfills a similar purpose
class REAL_PRECISION_CONFIG(object):
    def __init__(self, *args):
        if len(args) == 1:
            mode, exp, frac = args[0]
        else:
            mode = args[0]
            exp = args[1]
            frac = args[2]

        self._mode = REAL_MODE_ENUM(mode)
        self._exp = exp
        self._frac = frac
        self._precision = exp + frac

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'({self._mode}, {self._exp}, {self._frac})'

    @property
    def value(self):
        return self._precision

    def _convert_float(self, raw):
        if self._precision == 32:
            return struct.unpack('>f', raw)[0]
        elif self._precision == 64:
            return struct.unpack('>d', raw)[0]
        else:
            raise ValueError(f'Bad REAL_PRECISION_CONFIG: {self._precision} ({self._exp}+{self._frac})')

    def _convert_fixed(self, raw):
        if self._precision == 32:
            exp, frac = struct.unpack('>hH', raw)
        elif self._precision == 64:
            exp, frac = struct.unpack('>lL', raw)
        else:
            raise ValueError(f'Bad REAL_PRECISION_CONFIG: {self._precision} ({self._exp}+{self._frac})')

        value = Decimal(exp) + Decimal(frac / (2 ** self._frac))
        return value

    def __call__(self, raw):
        if self._mode == REAL_MODE_ENUM.FLOATING:
            return self._convert_float(raw)
        elif self._mode == REAL_MODE_ENUM.FIXED:
            return self._convert_fixed(raw)
        else:
            raise ValueError(f'Bad REAL_MODE_ENUM: {self._mode}')


class VDC_TYPE_ENUM(enum.IntEnum):
    INTEGER = 0
    REAL = 1


class COLOR_MODEL_ENUM(enum.IntEnum):
    RGB = 1
    CIELAB = 2
    CIELUV = 3
    CMYK = 4
    RGB_related = 5


class COLOR_SELECTION_MODE_ENUM(enum.IntEnum):
    INDEXED = 0
    DIRECT = 1


# Because the CGM standard can't spell (yes I know it's a valid alternate 
# spelling depending on what country you are in)
COLOUR_MODEL_ENUM = COLOR_MODEL_ENUM
COLOUR_SELECTION_MODE_ENUM = COLOR_SELECTION_MODE_ENUM


class CHARACTER_SET_TYPE_ENUM(enum.IntEnum):
    SET_94_CHARACTER = 0
    SET_96_CHARACTER = 1
    SET_94_CHARACTER_MULTIBYTE = 2
    SET_96_CHARACTER_MULTIBYTE = 3
    COMPLETE_CODE = 4


class CHARACTER_CODING_ENUM(enum.IntEnum):
    BASIC_7_BIT = 0
    BASIC_8_BIT = 1
    EXTENDED_7_BIT = 2
    EXTENDED_8_BIT = 3


class TEXT_PRECISION_ENUM(enum.IntEnum):
    STRING = 0
    CHARACTER = 1
    STROKE = 2


class SCALING_MODE_ENUM(enum.IntEnum):
    ABSTRACT = 0
    METRIC = 1


class WIDTH_SPECIFICATION_MODE_ENUM(enum.IntEnum):
    ABSOLUTE = 0
    SCALED = 1
    FRACTIONAL = 2
    MM = 3


class INTERIOR_STYLE_ENUM(enum.IntEnum):
    HOLLOW = 0
    SOLID = 1
    PATTERN = 2
    HATCH = 3
    EMPTY = 4
    GEOMETRIC_PATTERN = 5
    INTERPOLATED = 6


class INHERITANCE_FLAG_ENUM(enum.IntEnum):
    STATE_LIST = 0
    APPLICATION_STRUCTURE = 1
