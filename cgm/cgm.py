
import json

from .file import CGMFile
from .config import CGMConfig
from .types import CGMTopLevelType, CGMBaseType

non_metadata_elements = [
    'POLYGON',
    'POLYLINE',
    'TEXT_COLOUR',
    'FILL_COLOUR',
    'CHARACTER_EXPANSION_FACTOR',
    'RESTRICTED_TEXT',
    'CIRCULAR_ARC_CENTRE',
    'CIRCULAR_ARC_POINT',
    'ELLIPSE',
    'EDGE_VISIBILITY',
    'INTERIOR_STYLE',
    'MITRE_LIMIT',
    'LINE_CAP',
    'RECTANGLE',
    'EDGE_WIDTH',
    'CLIP_RECTANGLE',
    'EDGE_WIDTH',
    'EDGE_COLOUR',
    'CLIP_INDICATOR',
    'COLOUR_VALUE_EXTENT',
    'COLOUR_PRECISION',
    'VDC_TYPE',
    'INDEX_PRECISION',
    'COLOUR_INDEX_PRECISION',
    'MAXIMUM_COLOUR_INDEX',
    'CHARACTER_CODING_ANNOUNCER',
    'METAFILE_DEFAULTS_REPLACEMENT',
    'REAL_PRECISION',
    'MAXIMUM_VDC_EXTENT',
    'FONT_LIST',
    'CHARACTER_SET_LIST',
    'NO-OP',
    'INTEGER_PRECISION',
    'SCALING_MODE',
    'COLOUR_SELECTION_MODE',
    'LINE_WIDTH_SPECIFICATION_MODE',
    'MARKER_WIDTH_SPECIFICATION_MODE',
    'EDGE_WIDTH_SPECIFICATION_MODE',
    'BACKGROUND_COLOUR',
    'LINE_WIDTH',
    'EDGE_CAP',
    'LINE_COLOUR',
    'INTERIOR_STYLE_SPECIFICATION_MODE',
    'VDC_EXTENT',
    'MARKER_SIZE_SPECIFICATION_MODE',
    'TEXT_PRECISION',
    'MARKER_SIZE',
    'EDGE_JOIN',
    'CHARACTER_SET_INDEX',
    'ALTERNATE_CHARACTER_SET_INDEX',
    'CHARACTER_ORIENTATION',
    'CHARACTER_HEIGHT',
    'MARKER_COLOUR',
    'RESTRICTED_TEXT_TYPE',
]

class CGM(CGMBaseType):
    def __init__(self, filename):
        fp = CGMFile(filename)
        config = CGMConfig()
        super().__init__(fp=fp, config=config)

    def extract(self):
        values = []
        try:
            while True:
                obj = CGMTopLevelType(fp=self.fp, config=self.config)
                values.append(obj)
        except EOFError:
            pass

        self.values = tuple(values)

    def _print_val(self, cmd, data=None):
        if data is not None:
            print(f'{cmd}: {data}')
        else:
            print(cmd)

    def _unwrap_val_for_print(self, value):
        unwrapped_data = value.unwrap()
        if isinstance(unwrapped_data, str):
            cmd = unwrapped_data
            rest = None
        else:
            cmd = unwrapped_data[0]
            rest = json.dumps(unwrapped_data[1:], indent=4)

        return (cmd, rest)


    def print(self, exclude=None):
        for val in self.values:
            cmd, rest = self._unwrap_val_for_print(val)
            if exclude is None or cmd not in exclude:
                self._print_val(cmd, rest)
