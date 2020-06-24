
from .types import COLOR_MODEL


class CGMConfig(object):
    def __init__(self):
        # NOTE: VDC == Virtual Device Coordinates
        self._config = {
            'COLOR_MODEL': None,
            'COLOR_SELECTION_MODE': None,
            'REAL_PRECISION': (1, 16, 16),      # 1 == Fixed point
            'INTEGER_PRECISION': 16,
            'COLOR_PRECISION': 1,
            'COLOR_INDEX_PRECISION': 1,
            'INDEX_PRECISION': 16,
            'VDC_REAL_PRECISION': (1, 16, 16),  # 1 == Fixed point
            'VDC_INTEGER_PRECISION': 16,
            'NAME_PRECISION': 16
            'COLOR_VALUE_EXTENT': None,
        }

        # The COLOR_VALUE_EXTENT value depends on COLOR_MODEL
        self._cve = {
            COLOR_MODEL.RGB: ((0, 0, 0), (255, 255, 255)),
            COLOR_MODEL.CMYK: ((0, 0, 0, 0), (255, 255, 255, 255)),
            COLOR_MODEL.CIELUV: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            COLOR_MODEL.CIELAB: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            COLOR_MODEL.RGB_related: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        }

    def __getattr__(self, name):
        if name in self._config:
            return self._config[name]

        if 'COLOUR_' in name:
            # translate between COLOR and COLOUR
            name = name.replace('COLOUR_', 'COLOR_')

            if name in self._config:
                return self._config[name]

        return self.__getattribute__(name)

    def __setattr__(self, name, value):
        if name in self._config:
            self._config[name] = value
            if name == 'COLOR_MODEL':
                # also set the COLOR_VALUE_EXTENT
                self._config['COLOR_VALUE_EXTENT'] = self._cve[COLOR_MODEL(value)]
        else:
            sellf.__setattribute__(name, value)
