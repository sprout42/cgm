
from .enums import *


class CGMConfig(object):
    def __init__(self):
        # NOTE: VDC == Virtual Device Coordinates
        self._config = {
            'COLOR_MODEL':                       {'type': COLOR_MODEL_ENUM, 'default': 1},
            'COLOR_SELECTION_MODE':              {'type': COLOR_SELECTION_MODE_ENUM},
            'VDC_TYPE':                          {'type': VDC_TYPE_ENUM},
            'LINE_WIDTH_SPECIFICATION_MODE':     {'type': WIDTH_SPECIFICATION_MODE_ENUM},
            'MARKER_SIZE_SPECIFICATION_MODE':    {'type': WIDTH_SPECIFICATION_MODE_ENUM},
            'EDGE_WIDTH_SPECIFICATION_MODE':     {'type': WIDTH_SPECIFICATION_MODE_ENUM},
            'INTERIOR_STYLE_SPECIFICATION_MODE': {'type': WIDTH_SPECIFICATION_MODE_ENUM},
            'INTERIOR_STYLE':                    {'type': INTERIOR_STYLE_ENUM},
            'TEXT_PRECISION':                    {'type': TEXT_PRECISION_ENUM},
            'REAL_PRECISION':                    {'type': REAL_PRECISION_CONFIG, 'default': (REAL_MODE_ENUM.FIXED, 16, 16)},
            'INTEGER_PRECISION':                 {'type': None, 'default': 16},
            'COLOR_PRECISION':                   {'type': None, 'default': 16},
            'COLOR_INDEX_PRECISION':             {'type': None, 'default': 16},
            'INDEX_PRECISION':                   {'type': None, 'default': 16},
            'VDC_REAL_PRECISION':                {'type': REAL_PRECISION_CONFIG, 'default': (REAL_MODE_ENUM.FIXED, 16, 16)},
            'VDC_INTEGER_PRECISION':             {'type': None, 'default': 16},
            'NAME_PRECISION':                    {'type': None, 'default': 16},
        }

        for key in self._config:
            if 'default' in self._config[key] and \
                    self._config[key]['default'] is not None:
                self.set(key, self._config[key]['default'])
            else:
                # Skip the setter and just set the value to None
                self._config[key]['value'] = None

    def __repr__(self):
        return str(self._config)

    def __iter__(self):
        for key in self._config:
            yield key

    def _fixkey(self, key):
        if 'COLOUR_' in key:
            key = key.replace('COLOUR_','COLOR_')
        return key

    def __contains__(self, key):
        key = self._fixkey(key)
        if key in self._config:
            return True
        return False

    def get(self, key):
        key = self._fixkey(key)
        value = self._config[key]['value']
        return self._config[key]['value']

    def set(self, key, value):
        key = self._fixkey(key)
        try:
            value = value.unwrap()
        except AttributeError:
            pass

        val_type = self._config[key]['type']
        if val_type:
            if 'value' in self._config[key]: print(f'CHANGING {key} from {self._config[key]["value"]} to {val_type(value)}')
            self._config[key]['value'] = val_type(value)
        else:
            if 'value' in self._config[key]: print(f'CHANGING {key} from {self._config[key]["value"]} to {value}')
            self._config[key]['value'] = value

    def __getattr__(self, key):
        key = self._fixkey(key)
        if key[0] != '_' and key in self._config:
            return self.get(key)

        return self.__getattribute__(key)

    def __setattr__(self, key, value):
        key = self._fixkey(key)
        if key[0] != '_' and key in self._config:
            self.set(key, value)

        super().__setattr__(key, value)

