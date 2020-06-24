from .base import *
from .noop import *
from .string import *
from .integer import *
from .real import *


cgm_delimiter_elements = [
  {
    'element': 'NO-OP',
    'id': 0,
    'type': '_',
    'len': 'n',
    'range': None
  },
  {
    'element': 'BEGIN_METAFILE',
    'id': 1,
    'type': 'SF',
    'len': 'BS',
    'range': 'SR'
  },
  {
    'element': 'END_METAFILE',
    'id': 2,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_PICTURE',
    'id': 3,
    'type': 'SF',
    'len': 'BS',
    'range': 'SR'
  },
  {
    'element': 'BEGIN_PICTURE_BODY',
    'id': 4,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'END_PICTURE',
    'id': 5,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_SEGMENT',
    'id': 6,
    'type': 'N',
    'len': 'BN',
    'range': 'NR'
  },
  {
    'element': 'END_SEGMENT',
    'id': 7,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_FIGURE',
    'id': 8,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'END_FIGURE',
    'id': 9,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_PROTECTION_REGION',
    'id': 13,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'END_PROTECTION_REGION',
    'id': 14,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_COMPOUND_LINE',
    'id': 15,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'END_COMPOUND_LINE',
    'id': 16,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_COMPOUND_TEXT_PATH',
    'id': 17,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'END_COMPOUND_TEXT_PATH',
    'id': 18,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_TILE_ARRAY',
    'id': 19,
    'type': 'P,2E,4I,2R,2I,2I'
    'len': [
      'BP+',
      '2BE+',
      '4BI+2BR+',
      '4BI'
    ],
    'range': [
      'VDCR',
      '{0..3},{0,1}',
      '+IR,+RR',
      '++IR,+IR'
    ]
  },
  {
    'element': 'END_TILE_ARRAY',
    'id': 20,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'BEGIN_APPLICATION_STRUCTURE',
    'id': 21,
    'type': 'SF,SF,E',
    'len': '2BS+BE',
    'range': 'SR,SR,{0,1}'
  },
  {
    'element': 'BEGIN_APPLICATION_STRUCTURE_BODY',
    'id': 22,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'END_APPLICATION_STRUCTURE',
    'id': 23,
    'type': None,
    'len': 0,
    'range': None
  }
]

cgm_metafile_descriptor_elements = [
  {
    'element': 'METAFILE_DESCRIPTION',
    'id': 2,
    'type': 'SF',
    'len': 'BS',
    'range': 'SR'
  },
  {
    'element': 'VDC_TYPE',
    'id': 3,
    'type': 'E',
    'len': 'BE',
    'range': '0,1'
  },
  {
    'element': 'INTEGER_PRECISION',
    'id': 4,
    'type': 'I',
    'len': 'BI',
    'range': '8,16,24,32'
  },
  {
    'element': 'REAL_PRECISION',
    'id': 5,
    'type': 'E,2I',
    'len': 'BE+2BI',
    'range': '{0,1},{9,12,16,32},{23,52,16,32}'
  },
  {
    'element': 'INDEX_PRECISION',
    'id': 6,
    'type': 'I',
    'len': 'BI',
    'range': '8,16,24,32'
  },
  {
    'element': 'COLOUR_PRECISION',
    'id': 7,
    'type': 'I',
    'len': 'BI',
    'range': '8,16,24,32'
  },
  {
    'element': 'COLOUR_INDEX_PRECISION',
    'id': 8,
    'type': 'I',
    'len': 'BI',
    'range': '8,16,24,32'
  },
  {
    'element': 'MAXIMUM_COLOUR_INDEX',
    'id': 9,
    'type': 'CI',
    'len': 'BCI',
    'range': 'CIR'
  },
  {
    'element': 'COLOUR_VALUE_EXTENT',
    'id': 10,
    'type': [
      '2CD',
      '6R'
    ],
    'len': [
      '2BCD',
      '6BR'
    ],
    'range': [
      'CCOR',
      'RR'
    ]
  },
  {
    'element': 'METAFILE_ELEMENT_LIST',
    'id': 11,
    'type': 'I,2nIX',
    'len': 'BI,2nBIX',
    'range': '++IR,IXR'
  },
  {
    'element': 'METAFILE_DEFAULTS_REPLACEMENT',
    'id': 12,
    'type': 'METAFILE_ELEMENTS',
    'len': 'variable',
    'range': 'METAFILE_ELEMENTS',
  },
  {
    'element': 'FONT_LIST',
    'id': 13,
    'type': 'nSF',
    'len': 'nBS',
    'range': 'SR'
  },
  {
    'element': 'CHARACTER_SET_LIST',
    'id': 14,
    'type': 'n(E,SF)',
    'len': 'n(BE+BS)',
    'range': '{0..4},SR'
  },
  {
    'element': 'CHARACTER_CODING_ANNOUNCER',
    'id': 15,
    'type': 'E',
    'len': 'BE',
    'range': '0,1,2,3'
  },
  {
    'element': 'NAME_PRECISION',
    'id': 16,
    'type': 'I',
    'len': 'BI',
    'range': '8,16,24,32'
  },
  {
    'element': 'MAXIMUM_VDC_EXTENT',
    'id': 17,
    'type': '2P',
    'len': '2BP',
    'range': 'VDCR'
  },
  {
    'element': 'SEGMENT_PRIORITY_EXTENT',
    'id': 18,
    'type': '2I',
    'len': '2BI',
    'range': '++IR'
  },
  {
    'element': 'COLOUR_MODEL',
    'id': 19,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'COLOUR_CALIBRATION',
    'id': 20,
    'type': 'IX,3R,18R,I,6nCCO,I,mCD,3mR',
    'len': [
      'BIX+3BR+',
      '18BR+BI+',
      '6nBCCO+BI+',
      'mBCD+3mBR'
    ],
    'range': [
      '+IXR,RR',
      'RR,++IR',
      'CCOR,++IR',
      'CCOR,RR'
    ]
  },
  {
    'element': 'FONT_PROPERTIES',
    'id': 21,
    'type': 'n[IX,I,SDR]',
    'len': [
      'n(BIX+BI)+',
      '(sum of)BSDR'
    ],
    'range': None
  },
  {
    'element': 'GLYPH_MAPPING',
    'id': 22,
    'type': 'IX,E,SF,I,IX,SDR',
    'len': [
      'BIX+BE+',
      'BS+BI+',
      'BIX+BSDR'
    ],
    'range': [
      '+IXR,ER',
      'SR,+IR',
      'IXR,n/a'
    ]
  },
  {
    'element': 'SYMBOL_LIBRARY_LIST',
    'id': 23,
    'type': 'nSF',
    'len': 'nBS',
    'range': 'SR'
  },
  {
    'element': 'PICTURE_DIRECTORY',
    'id': 24,
    'type': 'E,n(SF,2[ldt])',
    'len': 'BE+n(BS+2B[ldt])',
    'range': [
      '{0,1,2}',
      '(SR,[ldt]R,[ldt]R)'
    ]
  }
]

cgm_picture_descriptor_elements = [
  {
    'element': 'SCALING_MODE',
    'id': 1,
    'type': 'E,R (FP)',
    'len': 'BE+BFP',
    'range': '{0,1},FPR'
  },
  {
    'element': 'COLOUR_SELECTION_MODE',
    'id': 2,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1}'
  },
  {
    'element': 'LINE_WIDTH_SPECIFICATION_MODE',
    'id': 3,
    'type': 'E',
    'len': 'BE',
    'range': '{0..3}'
  },
  {
    'element': 'MARKER_SIZE_SPECIFICATION_MODE',
    'id': 4,
    'type': 'E',
    'len': 'BE',
    'range': '{0..3}'
  },
  {
    'element': 'EDGE_WIDTH_SPECIFICATION_MODE',
    'id': 5,
    'type': 'E',
    'len': 'BE',
    'range': '{0..3}'
  },
  {
    'element': 'VDC_EXTENT',
    'id': 6,
    'type': '2P',
    'len': '2BP',
    'range': 'VDCR'
  },
  {
    'element': 'BACKGROUND_COLOUR',
    'id': 7,
    'type': 'CD',
    'len': 'BCD',
    'range': 'CCOR'
  },
  {
    'element': 'DEVICE_VIEWPORT',
    'id': 8,
    'type': '2VP',
    'len': '2BVP',
    'range': 'VCR'
  },
  {
    'element': 'DEVICE_VIEWPORT_SPECIFICATION_MODE',
    'id': 9,
    'type': 'E,R(FP)',
    'len': 'BE+BFP',
    'range': '{0,1,2},FPR'
  },
  {
    'element': 'DEVICE_VIEWPORT_MAPPING',
    'id': 10,
    'type': '3E',
    'len': '3BE',
    'range': [
      '{0,1}',
      '{0,1,2}',
      '{0,1,2}'
    ]
  },
  {
    'element': 'LINE_REPRESENTATION',
    'id': 11,
    'type': '2IX,SS,CO',
    'len': [
      '2BIX+',
      'BSS+BCO'
    ],
    'range': [
      '+IXR,IXR',
      '+SSR,COR'
    ]
  },
  {
    'element': 'MARKER_REPRESENTATION',
    'id': 12,
    'type': '2IX,SS,CO',
    'len': [
      '2BIX+',
      'BSS+BCO'
    ],
    'range': [
      '+IXR,IXR',
      '++SSR,COR'
    ]
  },
  {
    'element': 'TEXT_REPRESENTATION',
    'id': 13,
    'type': '2IX,E,2R,CO',
    'len': [
      '2BIX+',
      'BE+',
      '2BR+BCO'
    ],
    'range': [
      '+IXR',
      '{0,1,2}',
      'RR,++RR,COR'
    ]
  },
  {
    'element': 'FILL_REPRESENTATION',
    'id': 14,
    'type': 'IX,E,CO,2IX',
    'len': [
      'BIX+',
      'BE+BCO+',
      '2BIX'
    ],
    'range': [
      '+IXR',
      '{0..6},COR',
      'IXR,+IXR'
    ]
  },
  {
    'element': 'EDGE_REPRESENTATION',
    'id': 15,
    'type': '2IX,SS,CO',
    'len': [
      '2BIX',
      'BSS+BCO'
    ],
    'range': [
      'IXR,+IXR',
      '++SSR,COR'
    ]
  },
  {
    'element': 'INTERIOR_STYLE_SPECIFICATION_MODE',
    'id': 16,
    'type': 'E',
    'len': 'BE',
    'range': '{0..3}'
  },
  {
    'element': 'LINE_AND_EDGE_TYPE_DEFINITION',
    'id': 17,
    'type': 'IX,SS,nI',
    'len': 'BIX+BSS+nBI',
    'range': [
      '-',
      'IXR,+SSR,++IR'
    ]
  },
  {
    'element': 'HATCH_STYLE_DEFINITION',
    'id': 18,
    'type': 'IX,E,4SS,SS,I,nI,nIX',
    'len': [
      'BIX+BE+',
      '4BSS+BSS+',
      'BI+nBI+',
      'nBIX'
    ],
    'range': [
      '-IXR,{0,1}',
      '++SSR,+SSR',
      '+IR,++IR',
      'IXR'
    ]
  },
  {
    'element': 'GEOMETRIC_PATTERN_DEFINITION',
    'id': 19,
    'type': 'IX,N,2P',
    'len': [
      'BIX+BN+',
      '2BP'
    ],
    'range': [
      '+IXR,NR',
      'VDCR'
    ]
  },
  {
    'element': 'APPLICATION_STRUCTURE_DIRECTORY',
    'id': 20,
    'type': 'E,n(SF,[ldt])',
    'len': 'BE+n(BS+B[ldt])',
    'range': [
      '{0,1,2}',
      '(SR,[ldt]R,[ldt]R)'
    ]
  }
]

cgm_control_elements = [
  {
    'element': 'VDC_INTEGER_PRECISION',
    'id': 1,
    'type': 'I',
    'len': 'BI',
    'range': '16,24,32'
  },
  {
    'element': 'VDC_REAL_PRECISION',
    'id': 2,
    'type': 'E,2I',
    'len': 'BE+2BI',
    'range': [
      '{0,1}',
      '{9,12,16,32}',
      '{23,52,16,32}'
    ]
  },
  {
    'element': 'AUXILIARY_COLOUR',
    'id': 3,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'TRANSPARENCY',
    'id': 4,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1}'
  },
  {
    'element': 'CLIP_RECTANGLE',
    'id': 5,
    'type': '2P',
    'len': '2BP',
    'range': 'VDCR'
  },
  {
    'element': 'CLIP_INDICATOR',
    'id': 6,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1}'
  },
  {
    'element': 'LINE_CLIPPING_MODE',
    'id': 7,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1,2}'
  },
  {
    'element': 'MARKER_CLIPPING_MODE',
    'id': 8,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1,2}'
  },
  {
    'element': 'EDGE_CLIPPING_MODE',
    'id': 9,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1,2}'
  },
  {
    'element': 'NEW_REGION',
    'id': 10,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'SAVE_PRIMITIVE_CONTEXT',
    'id': 11,
    'type': 'N',
    'len': 'BN',
    'range': 'NR'
  },
  {
    'element': 'RESTORE_PRIMITIVE_CONTEXT',
    'id': 12,
    'type': 'N',
    'len': 'BN',
    'range': 'NR'
  },
  {
    'element': 'PROTECTION_REGION_INDICATOR',
    'id': 17,
    'type': '2IX',
    'len': '2BIX',
    'range': '+IXR,{1,2,3}'
  },
  {
    'element': 'GENERALIZED_TEXT_PATH_MODE',
    'id': 18,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1,2}'
  },
  {
    'element': 'MITRE_LIMIT',
    'id': 19,
    'type': 'R',
    'len': 'BR',
    'range': '++RR'
  },
  {
    'element': 'TRANSPARENT_CELL_COLOUR',
    'id': 20,
    'type': 'E,CO',
    'len': 'BE+BCO',
    'range': '{0,1},COR'
  }
]

cgm_graphical_primitive_elements = [
  {
    'element': 'POLYLINE',
    'id': 1,
    'type': 'nP',
    'len': 'nBP',
    'range': 'VDCR'
  },
  {
    'element': 'DISJOINT_POLYLINE',
    'id': 2,
    'type': 'nP',
    'len': 'nBP',
    'range': 'VDCR'
  },
  {
    'element': 'POLYMARKER',
    'id': 3,
    'type': 'nP',
    'len': 'NBP',
    'range': 'VDCR'
  },
  {
    'element': 'TEXT',
    'id': 4,
    'type': 'P,E,S',
    'len': [
      'BP+BE+',
      'BS'
    ],
    'range': [
      'VDCR,{0,1}',
      'SR'
    ]
  },
  {
    'element': 'RESTRICTED_TEXT',
    'id': 5,
    'type': '2VDC,P,E,S',
    'len': [
      '2VDC+BP+',
      'BE+BS'
    ],
    'range': [
      '++VDCR,VDCR',
      '{0,1},SR'
    ]
  },
  {
    'element': 'APPEND_TEXT',
    'id': 6,
    'type': 'E,S',
    'len': 'BE+BS',
    'range': '{0,1},SR'
  },
  {
    'element': 'POLYGON',
    'id': 7,
    'type': 'nP',
    'len': 'nBP',
    'range': 'VDCR'
  },
  {
    'element': 'POLYGON_SET',
    'id': 8,
    'type': 'n(P,E)',
    'len': 'n(BP+BE)',
    'range': 'VDCR,{0..3}'
  },
  {
    'element': 'CELL_ARRAY',
    'id': 9,
    'type': '3P,3I,E,CLIST',
    'len': [
      '3BP+3BI+',
      'BE+nBCO'
    ],
    'range': [
      'VDCR,+IR,++IR',
      '{0,1},COR'
    ]
  },
  {
    'element': 'GENERALIZED_DRAWING_PRIMITIVE',
    'id': 10,
    'type': 'I,I,nP,D',
    'len': [
      '2BI+nBP+',
      'BS'
    ],
    'range': [
      'IR,++IR',
      'VDCR,SR'
    ]
  },
  {
    'element': 'RECTANGLE',
    'id': 11,
    'type': '2P',
    'len': '2BP',
    'range': 'VDCR'
  },
  {
    'element': 'CIRCLE',
    'id': 12,
    'type': 'P,VDC',
    'len': 'BP+BVDC',
    'range': [
      'VDCR',
      '++VDCR'
    ]
  },
  {
    'element': 'CIRCULAR_ARC_POINT',
    'id': 13,
    'type': '3P',
    'len': '3BP',
    'range': 'VDCR'
  },
  {
    'element': 'CIRCULAR_ARC_3_POINT_CLOSE',
    'id': 14,
    'type': '3P,E',
    'len': '3BP+BE',
    'range': 'VDCR,{0,1}'
  },
  {
    'element': 'CIRCULAR_ARC_CENTRE',
    'id': 15,
    'type': 'P,4VDC,VDC',
    'len': [
      'BP+4BVDC+',
      'BVDC'
    ],
    'range': [
      'VDCR,VDCR',
      '++VDCR'
    ]
  },
  {
    'element': 'CIRCULAR_ARC_CENTRE_CLOSE',
    'id': 16,
    'type': 'P,4VDC,VDC,E',
    'len': [
      'BP+4BVDC+',
      'BVDC+BE'
    ],
    'range': [
      'VDCR,VDCR',
      '++VDCR,{0,1}'
    ]
  },
  {
    'element': 'ELLIPSE',
    'id': 17,
    'type': '3P',
    'len': '3BP',
    'range': 'VDCR'
  },
  {
    'element': 'ELLIPTICAL_ARC',
    'id': 18,
    'type': '3P,4VDC',
    'len': '3BP+4BVDC',
    'range': 'VDCR,VDCR'
  },
  {
    'element': 'ELLIPTICAL_ARC_CLOSE',
    'id': 19,
    'type': '3P,4VDC,E',
    'len': [
      '3BP+4BVDC+',
      'BE'
    ],
    'range': [
      'VDCR,VDCR',
      '{0,1}'
    ]
  },
  {
    'element': 'CIRCULAR_ARC_CENTRE_REVERSED',
    'id': 20,
    'type': 'P,4VDC,VDC',
    'len': [
      'BP+4BVDC+',
      'BVDC'
    ],
    'range': [
      'VDCR,VDCR',
      '++VDCR'
    ]
  },
  {
    'element': 'CONNECTING_EDGE',
    'id': 21,
    'type': None,
    'len': 0,
    'range': None
  },
  {
    'element': 'HYPERBOLIC_ARC',
    'id': 22,
    'type': '3P,4VDC',
    'len': '3BP+4BVDC',
    'range': 'VDCR'
  },
  {
    'element': 'PARABOLIC_ARC',
    'id': 23,
    'type': '3P',
    'len': '3BP',
    'range': 'VDCR'
  },
  {
    'element': 'NON-UNIFORM_B-SPLINE',
    'id': 24,
    'type': '2I,nP,(n+m)R,2R',
    'len': [
      '2BI+nBP+',
      '(n+m)BR+',
      '2BR'
    ],
    'range': [
      '+IR,VDCR',
      '++RR',
      '++RR'
    ]
  },
  {
    'element': 'NON-UNIFORM_RATIONAL_B-SPLINE',
    'id': 25,
    'type': '2I,nP,(n+m)R,2R,nR'
    'len': [
      '2BI+nBP+',
      '(n+m)BR+',
      '2BR+',
      'nBR'
    ],
    'range': [
      '+IR,VDCR',
      '++RR',
      '++RR',
      '++RR'
    ]
  },
  {
    'element': 'POLYBEZIER',
    'id': 26,
    'type': 'IX,4nP(or),(3n+1)P',
    'len': [
      'BIX+4nBP(or)',
      'BIX+(3n+1)P'
    ],
    'range': [
      '{1,2}',
      'VDCR'
    ]
  },
  {
    'element': 'POLYSYMBOL',
    'id': 27,
    'type': 'IX,nP',
    'len': 'BIX+nBP',
    'range': '+IXR,VDCR'
  },
  {
    'element': 'BITONAL_TILE',
    'id': 28,
    'type': 'IX,I,2CO,SDR,BS',
    'len': [
      'BIX+BIX+',
      '2BCO+',
      'BSDR,BBS'
    ],
    'range': [
      '++IXR,++IR',
      'COR',
      'n/a,BSR'
    ]
  },
  {
    'element': 'TILE',
    'id': 29,
    'type': 'IX,I,I,SDR,BS',
    'len': [
      'BIX+BI+',
      'BI+BSDR+BB',
      'S'
    ],
    'range': [
      '++IXR,++IR',
      '++IR,n/a,BSR'
    ]
  }
]

cgm_attribute_elements = [
  {
    'element': 'LINE_BUNDLE_INDEX',
    'id': 1,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'LINE_TYPE',
    'id': 2,
    'type': 'IX',
    'len': 'BIX',
    'range': 'IXR'
  },
  {
    'element': 'LINE_WIDTH',
    'id': 3,
    'type': 'SS',
    'len': 'BSS',
    'range': '++SSR'
  },
  {
    'element': 'LINE_COLOUR',
    'id': 4,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'MARKER_BUNDLE_INDEX',
    'id': 5,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'MARKER_TYPE',
    'id': 6,
    'type': 'IX',
    'len': 'BIX',
    'range': 'IXR'
  },
  {
    'element': 'MARKER_SIZE',
    'id': 7,
    'type': 'SS',
    'len': 'BSS',
    'range': '++SSR'
  },
  {
    'element': 'MARKER_COLOUR',
    'id': 8,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'TEXT_BUNDLE_INDEX',
    'id': 9,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'TEXT_FONT_INDEX',
    'id': 10,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'TEXT_PRECISION',
    'id': 11,
    'type': 'E',
    'len': 'BE',
    'range': '{0..2}'
  },
  {
    'element': 'CHARACTER_EXPANSION_FACTOR',
    'id': 12,
    'type': 'R',
    'len': 'BR',
    'range': '++RR'
  },
  {
    'element': 'CHARACTER_SPACING',
    'id': 13,
    'type': 'R',
    'len': 'BR',
    'range': 'RR'
  },
  {
    'element': 'TEXT_COLOUR',
    'id': 14,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'CHARACTER_HEIGHT',
    'id': 15,
    'type': 'VDC',
    'len': 'BVDC',
    'range': '++VDCR'
  },
  {
    'element': 'CHARACTER_ORIENTATION',
    'id': 16,
    'type': '4VDC',
    'len': '4BVDC',
    'range': 'VDCR'
  },
  {
    'element': 'TEXT_PATH',
    'id': 17,
    'type': 'E',
    'len': 'BE',
    'range': '{0..3}'
  },
  {
    'element': 'TEXT_ALIGNMENT',
    'id': 18,
    'type': '2E,R,R',
    'len': [
      '2BE+',
      '2BR'
    ],
    'range': [
      '{0..4}, {0..6}',
      '2RR'
    ]
  },
  {
    'element': 'CHARACTER_SET_INDEX',
    'id': 19,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'ALTERNATE_CHARACTER_SET_INDEX',
    'id': 20,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'FILL_BUNDLE_INDEX',
    'id': 21,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'INTERIOR_STYLE',
    'id': 22,
    'type': 'E',
    'len': 'BE',
    'range': '{0..6}'
  },
  {
    'element': 'FILL_COLOUR',
    'id': 23,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'HATCH_INDEX',
    'id': 24,
    'type': 'IX',
    'len': 'BIX',
    'range': 'IXR'
  },
  {
    'element': 'PATTERN_INDEX',
    'id': 25,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'EDGE_BUNDLE_INDEX',
    'id': 26,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'EDGE_TYPE',
    'id': 27,
    'type': 'IX',
    'len': 'BIX',
    'range': 'IXR'
  },
  {
    'element': 'EDGE_COLOUR',
    'id': 29,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'EDGE_VISIBILITY',
    'id': 30,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1}'
  },
  {
    'element': 'FILL_REFERENCE_POINT',
    'id': 31,
    'type': 'P',
    'len': 'BP',
    'range': 'VDCR'
  },
  {
    'element': 'PATTERN_TABLE',
    'id': 32,
    'type': 'IX,3I,nx*nyCO',
    'len': [
      'BIX+3BI+',
      'nx*nyBCO'
    ],
    'range': [
      '+IXR,+IR',
      '++IR,COR'
    ]
  },
  {
    'element': 'PATTERN_SIZE',
    'id': 33,
    'type': '4SS',
    'len': '4BSS',
    'range': 'SSR'
  },
  {
    'element': 'COLOUR_TABLE',
    'id': 34,
    'type': 'CI,nCD',
    'len': 'BCI+nBCD',
    'range': 'CIR,CCOR'
  },
  {
    'element': 'ASPECT_SOURCE_FLAGS',
    'id': 35,
    'type': 'n(E,E)',
    'len': 'n(2BE)',
    'range': '{0..17},{0,1}'
  },
  {
    'element': 'PICK_IDENTIFIER',
    'id': 36,
    'type': 'N',
    'len': 'BN',
    'range': 'NR'
  },
  {
    'element': 'LINE_CAP',
    'id': 37,
    'type': 'IX,IX',
    'len': '2BIX',
    'range': '+IXR'
  },
  {
    'element': 'LINE_JOIN',
    'id': 38,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'LINE_TYPE_CONTINUATION',
    'id': 39,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'LINE_TYPE_INITIAL_OFFSET',
    'id': 40,
    'type': 'R',
    'len': 'BR',
    'range': '++RR'
  },
  {
    'element': 'TEXT_SCORE_TYPE',
    'id': 41,
    'type': 'n(IX,E)',
    'len': 'nBIX+nBE',
    'range': 'IXR,{0,1}'
  },
  {
    'element': 'RESTRICTED_TEXT_TYPE',
    'id': 42,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'INTERPOLATED_INTERIOR',
    'id': 43,
    'type': 'IX,2nSS,I,mR,kCO',
    'len': [
      '2BIX+2nBSS+',
      'BI+mBR+kBCO'
    ],
    'range': [
      '{1..3},SSR',
      '+IR,RR,COR'
    ]
  },
  {
    'element': 'EDGE_CAP',
    'id': 44,
    'type': 'IX,IX',
    'len': '2BIX',
    'range': '+IXR'
  },
  {
    'element': 'EDGE_JOIN',
    'id': 45,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'EDGE_TYPE_CONTINUATION',
    'id': 46,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'EDGE_TYPE_INITIAL_OFFSET',
    'id': 47,
    'type': 'R',
    'len': 'BR',
    'range': '++RR'
  },
  {
    'element': 'SYMBOL_LIBRARY_INDEX',
    'id': 48,
    'type': 'IX',
    'len': 'BIX',
    'range': '+IXR'
  },
  {
    'element': 'SYMBOL_COLOUR',
    'id': 49,
    'type': 'CO',
    'len': 'BCO',
    'range': 'COR'
  },
  {
    'element': 'SYMBOL_SIZE',
    'id': 50,
    'type': 'E,2VDC',
    'len': 'BE+2BVDC',
    'range': '{0..2},VDCR'
  },
  {
    'element': 'SYMBOL_ORIENTATION',
    'id': 51,
    'type': '4VDC',
    'len': '4BVDC',
    'range': 'VDCR'
  }
]

cgm_escape_elements = [
  {
    'element': 'ESCAPE',
    'id': 1,
    'type': 'I,D',
    'len': 'BI+BS',
    'range': 'IR,SR'
  }
]

cgm_external_elements = [
  {
    'element': 'MESSAGE',
    'id': 1,
    'type': 'E,SF',
    'len': 'BE+BS',
    'range': '{0,1},SR'
  },
  {
    'element': 'APPLICATION_DATA',
    'id': 2,
    'type': 'I,D',
    'len': 'BI+BS',
    'range': 'IR,SR'
  }
]

cgm_segment_elements = [
  {
    'element': 'COPY_SEGMENT',
    'id': 1,
    'type': 'N,4R,2VDC,E',
    'len': [
      'BN+4BR+',
      '2BVDC +',
      'BE'
    ],
    'range': [
      'NR,RR',
      'VDCR',
      '{0,1}'
    ]
  },
  {
    'element': 'INHERITANCE_FILTER',
    'id': 2,
    'type': 'nE,E',
    'len': '(n+1)BE',
    'range': '{0..86},{0,1}'
  },
  {
    'element': 'CLIP_INHERITANCE',
    'id': 3,
    'type': 'E',
    'len': 'BE',
    'range': '{0,1}'
  },
  {
    'element': 'SEGMENT_TRANSFORMATION',
    'id': 4,
    'type': 'N,4R,2VDC',
    'len': [
      'BN+4BR+',
      '2BVDC'
    ],
    'range': [
      'NR,RR',
      'VDCR'
    ]
  },
  {
    'element': 'SEGMENT_HIGHLIGHTING',
    'id': 5,
    'type': 'N,E',
    'len': 'BN+BE',
    'range': 'NR,{0,1}'
  },
  {
    'element': 'SEGMENT_DISPLAY_PRIORITY',
    'id': 6,
    'type': 'N,I',
    'len': 'BN+BI',
    'range': 'NR,++IR'
  },
  {
    'element': 'SEGMENT_PICK_PRIORITY',
    'id': 7,
    'type': 'N,I',
    'len': 'BN+BI',
    'range': 'NR,++IR'
  }
]

cgm_application_elements = [
  {
    'element': 'APPLICATION_STRUCTURE_ATTRIBUTE',
    'id': 1,
    'type': 'SF, SDR',
    'len': 'BS+BS',
    'range': 'SR, SR'
  }
]

cgm_class_codes = [
  { 'class': 0, 'type': cgm_delimiter_elements },
  { 'class': 1, 'type': cgm_metafile_descriptor_elements },
  { 'class': 2, 'type': cgm_picture_descriptor_elements },
  { 'class': 3, 'type': cgm_control_elements },
  { 'class': 4, 'type': cgm_graphical_primitive_elements },
  { 'class': 5, 'type': cgm_attribute_elements },
  { 'class': 6, 'type': cgm_escape_elements },
  { 'class': 7, 'type': cgm_external_elements },
  { 'class': 8, 'type': cgm_segment_elements },
  { 'class': 9, 'type': cgm_application_elements },
]



class CGMGenericType(CGMBaseType):
    def __init__(self, config, fp, types):
        self.types = types
        self.num_elems = num_elems
        Super(CGMBaseType, self).__init__(config, fp)

    def extract(self):
        values = []
        for typ in self.types:
            values.append(typ(self.config, self.fp))
        self.value = tuple(values)

    @classmethod
    def make(config, fp, value):
        elements = re.findall(r'([0-9]+)([^, ]+)', value)
        types = []
        for elem in elements:
            num, class_str = elem
            types.extend([globals()[class_str]] * num)
        return cls(config, fp, types)

    @classmethod
    def discover(config, fp):
        # parses
        elements = re.findall(r'([0-9]+)([^, ]+)', value)
        types = []
        for elem in elements:
            num, class_str = elem
            types.extend([globals()[class_str]] * num)
        return cls(config, fp, types)

