from cgm.utils import SparseRange, OffsetList, OffsetStr


cgm_delimiter_elements = {
  0: {
    "element": "NO-OP",
    "id": 0,
    "type": "NOOP",
    "len": "n",
    "range": None
  },
  1: {
    "element": "BEGIN_METAFILE",
    "id": 1,
    "type": "SF",
    "len": "BS",
    "range": "SR"
  },
  2: {
    "element": "END_METAFILE",
    "id": 2,
    "type": None,
    "len": "0",
    "range": None
  },
  3: {
    "element": "BEGIN_PICTURE",
    "id": 3,
    "type": "SF",
    "len": "BS",
    "range": "SR"
  },
  4: {
    "element": "BEGIN_PICTURE_BODY",
    "id": 4,
    "type": None,
    "len": "0",
    "range": None
  },
  5: {
    "element": "END_PICTURE",
    "id": 5,
    "type": None,
    "len": "0",
    "range": None
  },
  6: {
    "element": "BEGIN_SEGMENT",
    "id": 6,
    "type": "N",
    "len": "BN",
    "range": "NR"
  },
  7: {
    "element": "END_SEGMENT",
    "id": 7,
    "type": None,
    "len": "0",
    "range": None
  },
  8: {
    "element": "BEGIN_FIGURE",
    "id": 8,
    "type": None,
    "len": "0",
    "range": None
  },
  9: {
    "element": "END_FIGURE",
    "id": 9,
    "type": None,
    "len": "0",
    "range": None
  },
  13: {
    "element": "BEGIN_PROTECTION_REGION",
    "id": 13,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  14: {
    "element": "END_PROTECTION_REGION",
    "id": 14,
    "type": None,
    "len": "0",
    "range": None
  },
  15: {
    "element": "BEGIN_COMPOUND_LINE",
    "id": 15,
    "type": None,
    "len": "0",
    "range": None
  },
  16: {
    "element": "END_COMPOUND_LINE",
    "id": 16,
    "type": None,
    "len": "0",
    "range": None
  },
  17: {
    "element": "BEGIN_COMPOUND_TEXT_PATH",
    "id": 17,
    "type": None,
    "len": "0",
    "range": None
  },
  18: {
    "element": "END_COMPOUND_TEXT_PATH",
    "id": 18,
    "type": None,
    "len": "0",
    "range": None
  },
  19: {
    "element": "BEGIN_TILE_ARRAY",
    "id": 19,
    "type": [
      "P",
      "2E",
      "4I",
      "2R",
      "2I",
      "2I"
    ],
    "len": [
      "BP",
      "2BE",
      "4BI",
      "2BR",
      "4BI"
    ],
    "range": [
      "VDCR",
      SparseRange((range(0, 4),)),
      SparseRange((0, 1)),
      "IR",
      "RR",
      "IR",
      "IR"
    ]
  },
  20: {
    "element": "END_TILE_ARRAY",
    "id": 20,
    "type": None,
    "len": "0",
    "range": None
  },
  21: {
    "element": "BEGIN_APPLICATION_STRUCTURE",
    "id": 21,
    "type": [
      "SF",
      "SF",
      "E"
    ],
    "len": [
      "2BS",
      "BE"
    ],
    "range": [
      "SR",
      "SR",
      SparseRange((0, 1))
    ]
  },
  22: {
    "element": "BEGIN_APPLICATION_STRUCTURE_BODY",
    "id": 22,
    "type": None,
    "len": "0",
    "range": None
  },
  23: {
    "element": "END_APPLICATION_STRUCTURE",
    "id": 23,
    "type": None,
    "len": "0",
    "range": None
  }
}

cgm_metafile_descriptor_elements = {
  1: {
    "element": "METAFILE_VERSION",
    "id": 1,
    "type": "I",
    "len": "BI",
    "range": [
      "IR",
      "1..n"
    ]
  },
  2: {
    "element": "METAFILE_DESCRIPTION",
    "id": 2,
    "type": "SF",
    "len": "BS",
    "range": "SR"
  },
  3: {
    "element": "VDC_TYPE",
    "id": 3,
    "type": "E",
    "len": "BE",
    "range": [
      "0",
      "1"
    ]
  },
  4: {
    "element": "INTEGER_PRECISION",
    "id": 4,
    "type": "I",
    "len": "BI",
    "range": [
      "8",
      "16",
      "24",
      "32"
    ]
  },
  5: {
    "element": "REAL_PRECISION",
    "id": 5,
    "type": [
      "E",
      "2I"
    ],
    "len": [
      "BE",
      "2BI"
    ],
    "range": [
      SparseRange((0, 1)),
      SparseRange((9, 12, 16, 32)),
      SparseRange((23, 52, 16, 32))
    ]
  },
  6: {
    "element": "INDEX_PRECISION",
    "id": 6,
    "type": "I",
    "len": "BI",
    "range": [
      "8",
      "16",
      "24",
      "32"
    ]
  },
  7: {
    "element": "COLOR_PRECISION",
    "id": 7,
    "type": "I",
    "len": "BI",
    "range": [
      "8",
      "16",
      "24",
      "32"
    ]
  },
  8: {
    "element": "COLOR_INDEX_PRECISION",
    "id": 8,
    "type": "I",
    "len": "BI",
    "range": [
      "8",
      "16",
      "24",
      "32"
    ]
  },
  9: {
    "element": "MAXIMUM_COLOR_INDEX",
    "id": 9,
    "type": "CI",
    "len": "BCI",
    "range": "CIR"
  },
  10: {
    "element": "COLOR_VALUE_EXTENT",
    "id": 10,
    "type": [
      "2CD",
      "or",
      "6R"
    ],
    "len": [
      "2BCD",
      "or",
      "6BR"
    ],
    "range": [
      "CCOR",
      "or",
      "RR"
    ]
  },
  11: {
    "element": "METAFILE_ELEMENT_LIST",
    "id": 11,
    "type": [
      "I",
      "2nIX"
    ],
    "len": [
      "BI",
      "2nBIX"
    ],
    "range": [
      "IR",
      "IXR"
    ]
  },
  12: {
    "element": "METAFILE_DEFAULTS_REPLACEMENT",
    "id": 12,
    "type": [
      "Metafile",
      "elements"
    ],
    "len": "variable",
    "range": [
      "Metafile",
      "elements"
    ]
  },
  13: {
    "element": "FONT_LIST",
    "id": 13,
    "type": "nSF",
    "len": "nBS",
    "range": "SR"
  },
  14: {
    "element": "CHARACTER_SET_LIST",
    "id": 14,
    "type": [
      "n",
      [
        "E",
        "SF"
      ]
    ],
    "len": [
      "n",
      [
        "BE",
        "BS"
      ]
    ],
    "range": [
      SparseRange((range(0, 5),)),
      "SR"
    ]
  },
  15: {
    "element": "CHARACTER_CODING_ANNOUNCER",
    "id": 15,
    "type": "E",
    "len": "BE",
    "range": [
      "0",
      "1",
      "2",
      "3"
    ]
  },
  16: {
    "element": "NAME_PRECISION",
    "id": 16,
    "type": "I",
    "len": "BI",
    "range": [
      "8",
      "16",
      "24",
      "32"
    ]
  },
  17: {
    "element": "MAXIMUM_VDC_EXTENT",
    "id": 17,
    "type": "2P",
    "len": "2BP",
    "range": "VDCR"
  },
  18: {
    "element": "SEGMENT_PRIORITY_EXTENT",
    "id": 18,
    "type": "2I",
    "len": "2BI",
    "range": "IR"
  },
  19: {
    "element": "COLOR_MODEL",
    "id": 19,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  20: {
    "element": "COLOR_CALIBRATION",
    "id": 20,
    "type": [
      "IX",
      "3R",
      "18R",
      "I",
      "6nCCO",
      "I",
      "mCD",
      "3mR"
    ],
    "len": [
      "BIX",
      "3BR",
      "18BR",
      "BI",
      "6nBCCO",
      "BI",
      "mBCD",
      "3mBR"
    ],
    "range": [
      "IXR",
      "RR",
      "RR",
      "IR",
      "CCOR",
      "IR",
      "CCOR",
      "RR"
    ]
  },
  21: {
    "element": "FONT_PROPERTIES",
    "id": 21,
    "type": [
      "n",
      OffsetList(['IX', 'I', 'SDR'])
    ],
    "len": [
      [
        "n",
        [
          "BIX",
          "BI"
        ]
      ],
      [
        "sum of",
        "BSDR"
      ]
    ],
    "range": None
  },
  22: {
    "element": "GLYPH_MAPPING",
    "id": 22,
    "type": [
      "IX",
      "E",
      "SF",
      "I",
      "IX",
      "SDR"
    ],
    "len": [
      "BIX",
      "BE",
      "BS",
      "BI",
      "BIX",
      "BSDR"
    ],
    "range": [
      "IXR",
      "ER",
      "SR",
      "IR",
      "IXR",
      "n/a"
    ]
  },
  23: {
    "element": "SYMBOL_LIBRARY_LIST",
    "id": 23,
    "type": "nSF",
    "len": "nBS",
    "range": "SR"
  },
  24: {
    "element": "PICTURE_DIRECTORY",
    "id": 24,
    "type": [
      "E",
      [
        "n",
        [
          "SF",
          [
            "2",
            OffsetStr('ldt')
          ]
        ]
      ]
    ],
    "len": [
      "BE",
      [
        "n",
        [
          "BS",
          [
            "2B",
            OffsetStr('ldt')
          ]
        ]
      ]
    ],
    "range": [
      SparseRange((0, 1, 2)),
      [
        "SR",
        [
          OffsetStr('ldt'),
          "R"
        ],
        [
          OffsetStr('ldt'),
          "R"
        ]
      ]
    ]
  }
}

cgm_picture_descriptor_elements = {
  1: {
    "element": "SCALING_MODE",
    "id": 1,
    "type": [
      "E",
      [
        "R ",
        "FP"
      ]
    ],
    "len": [
      "BE",
      "BFP"
    ],
    "range": [
      SparseRange((0, 1)),
      "FPR"
    ]
  },
  2: {
    "element": "COLOR_SELECTION_MODE",
    "id": 2,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1))
  },
  3: {
    "element": "LINE_WIDTH_SPECIFICATION_MODE",
    "id": 3,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 4),))
  },
  4: {
    "element": "MARKER_SIZE_SPECIFICATION_MODE",
    "id": 4,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 4),))
  },
  5: {
    "element": "EDGE_WIDTH_SPECIFICATION_MODE",
    "id": 5,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 4),))
  },
  6: {
    "element": "VDC_EXTENT",
    "id": 6,
    "type": "2P",
    "len": "2BP",
    "range": "VDCR"
  },
  7: {
    "element": "BACKGROUND_COLOR",
    "id": 7,
    "type": "CD",
    "len": "BCD",
    "range": "CCOR"
  },
  8: {
    "element": "DEVICE_VIEWPORT",
    "id": 8,
    "type": "2VP",
    "len": "2BVP",
    "range": "VCR"
  },
  9: {
    "element": "DEVICE_VIEWPORT_SPECIFICATION_MODE",
    "id": 9,
    "type": [
      "E",
      [
        "R",
        "FP"
      ]
    ],
    "len": [
      "BE",
      "BFP"
    ],
    "range": [
      SparseRange((0, 1, 2)),
      "FPR"
    ]
  },
  10: {
    "element": "DEVICE_VIEWPORT_MAPPING",
    "id": 10,
    "type": "3E",
    "len": "3BE",
    "range": [
      SparseRange((0, 1)),
      SparseRange((0, 1, 2)),
      SparseRange((0, 1, 2))
    ]
  },
  11: {
    "element": "LINE_REPRESENTATION",
    "id": 11,
    "type": [
      "2IX",
      "SS",
      "CO"
    ],
    "len": [
      "2BIX",
      "BSS",
      "BCO"
    ],
    "range": [
      "IXR",
      "IXR",
      "SSR",
      "COR"
    ]
  },
  12: {
    "element": "MARKER_REPRESENTATION",
    "id": 12,
    "type": [
      "2IX",
      "SS",
      "CO"
    ],
    "len": [
      "2BIX",
      "BSS",
      "BCO"
    ],
    "range": [
      "IXR",
      "IXR",
      "SSR",
      "COR"
    ]
  },
  13: {
    "element": "TEXT_REPRESENTATION",
    "id": 13,
    "type": [
      "2IX",
      "E",
      "2R",
      "CO"
    ],
    "len": [
      "2BIX",
      "BE",
      "2BR",
      "BCO"
    ],
    "range": [
      "IXR",
      SparseRange((0, 1, 2)),
      "RR",
      "RR",
      "COR"
    ]
  },
  14: {
    "element": "FILL_REPRESENTATION",
    "id": 14,
    "type": [
      "IX",
      "E",
      "CO",
      "2IX"
    ],
    "len": [
      "BIX",
      "BE",
      "BCO",
      "2BIX"
    ],
    "range": [
      "IXR",
      SparseRange((range(0, 7),)),
      "COR",
      "IXR",
      "IXR"
    ]
  },
  15: {
    "element": "EDGE_REPRESENTATION",
    "id": 15,
    "type": [
      "2IX",
      "SS",
      "CO"
    ],
    "len": [
      "2BIX",
      "BSS",
      "BCO"
    ],
    "range": [
      "IXR",
      "IXR",
      "SSR",
      "COR"
    ]
  },
  16: {
    "element": "INTERIOR_STYLE_SPECIFICATION_MODE",
    "id": 16,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 4),))
  },
  17: {
    "element": "LINE_AND_EDGE_TYPE_DEFINITION",
    "id": 17,
    "type": [
      "IX",
      "SS",
      "nI"
    ],
    "len": [
      "BIX",
      "BSS",
      "nBI"
    ],
    "range": [
      "IXR",
      "SSR",
      "IR"
    ]
  },
  18: {
    "element": "HATCH_STYLE_DEFINITION",
    "id": 18,
    "type": [
      "IX",
      "E",
      "4SS",
      "SS",
      "I",
      "nI",
      "nIX"
    ],
    "len": [
      "BIX",
      "BE",
      "4BSS",
      "BSS",
      "BI",
      "nBI",
      "nBIX"
    ],
    "range": [
      "IXR",
      SparseRange((0, 1)),
      "SSR",
      "SSR",
      "IR",
      "IR",
      "IXR"
    ]
  },
  19: {
    "element": "GEOMETRIC_PATTERN_DEFINITION",
    "id": 19,
    "type": [
      "IX",
      "N",
      "2P"
    ],
    "len": [
      "BIX",
      "BN",
      "2BP"
    ],
    "range": [
      "IXR",
      "NR",
      "VDCR"
    ]
  },
  20: {
    "element": "APPLICATION_STRUCTURE_DIRECTORY",
    "id": 20,
    "type": [
      "E",
      [
        "n",
        [
          "SF",
          OffsetStr('ldt')
        ]
      ]
    ],
    "len": [
      "BE",
      [
        "n",
        [
          "BS",
          [
            "B",
            OffsetStr('ldt')
          ]
        ]
      ]
    ],
    "range": [
      SparseRange((0, 1, 2)),
      [
        "SR",
        [
          OffsetStr('ldt'),
          "R"
        ],
        [
          OffsetStr('ldt'),
          "R"
        ]
      ]
    ]
  }
}

cgm_control_elements = {
  1: {
    "element": "VDC_INTEGER_PRECISION",
    "id": 1,
    "type": "I",
    "len": "BI",
    "range": [
      "16",
      "24",
      "32"
    ]
  },
  2: {
    "element": "VDC_REAL_PRECISION",
    "id": 2,
    "type": [
      "E",
      "2I"
    ],
    "len": [
      "BE",
      "2BI"
    ],
    "range": [
      SparseRange((0, 1)),
      SparseRange((9, 12, 16, 32)),
      SparseRange((23, 52, 16, 32))
    ]
  },
  3: {
    "element": "AUXILIARY_COLOR",
    "id": 3,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  4: {
    "element": "TRANSPARENCY",
    "id": 4,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1))
  },
  5: {
    "element": "CLIP_RECTANGLE",
    "id": 5,
    "type": "2P",
    "len": "2BP",
    "range": "VDCR"
  },
  6: {
    "element": "CLIP_INDICATOR",
    "id": 6,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1))
  },
  7: {
    "element": "LINE_CLIPPING_MODE",
    "id": 7,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1, 2))
  },
  8: {
    "element": "MARKER_CLIPPING_MODE",
    "id": 8,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1, 2))
  },
  9: {
    "element": "EDGE_CLIPPING_MODE",
    "id": 9,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1, 2))
  },
  10: {
    "element": "NEW_REGION",
    "id": 10,
    "type": None,
    "len": "0",
    "range": None
  },
  11: {
    "element": "SAVE_PRIMITIVE_CONTEXT",
    "id": 11,
    "type": "N",
    "len": "BN",
    "range": "NR"
  },
  12: {
    "element": "RESTORE_PRIMITIVE_CONTEXT",
    "id": 12,
    "type": "N",
    "len": "BN",
    "range": "NR"
  },
  17: {
    "element": "PROTECTION_REGION_INDICATOR",
    "id": 17,
    "type": "2IX",
    "len": "2BIX",
    "range": [
      "IXR",
      SparseRange((1, 2, 3))
    ]
  },
  18: {
    "element": "GENERALIZED_TEXT_PATH_MODE",
    "id": 18,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1, 2))
  },
  19: {
    "element": "MITRE_LIMIT",
    "id": 19,
    "type": "R",
    "len": "BR",
    "range": "RR"
  },
  20: {
    "element": "TRANSPARENT_CELL_COLOR",
    "id": 20,
    "type": [
      "E",
      "CO"
    ],
    "len": [
      "BE",
      "BCO"
    ],
    "range": [
      SparseRange((0, 1)),
      "COR"
    ]
  }
}

cgm_graphical_primitive_elements = {
  1: {
    "element": "POLYLINE",
    "id": 1,
    "type": "nP",
    "len": "nBP",
    "range": "VDCR"
  },
  2: {
    "element": "DISJOINT_POLYLINE",
    "id": 2,
    "type": "nP",
    "len": "nBP",
    "range": "VDCR"
  },
  3: {
    "element": "POLYMARKER",
    "id": 3,
    "type": "nP",
    "len": "NBP",
    "range": "VDCR"
  },
  4: {
    "element": "TEXT",
    "id": 4,
    "type": [
      "P",
      "E",
      "S"
    ],
    "len": [
      "BP",
      "BE",
      "BS"
    ],
    "range": [
      "VDCR",
      SparseRange((0, 1)),
      "SR"
    ]
  },
  5: {
    "element": "RESTRICTED_TEXT",
    "id": 5,
    "type": [
      "2VDC",
      "P",
      "E",
      "S"
    ],
    "len": [
      "2VDC",
      "BP",
      "BE",
      "BS"
    ],
    "range": [
      "VDCR",
      "VDCR",
      SparseRange((0, 1)),
      "SR"
    ]
  },
  6: {
    "element": "APPEND_TEXT",
    "id": 6,
    "type": [
      "E",
      "S"
    ],
    "len": [
      "BE",
      "BS"
    ],
    "range": [
      SparseRange((0, 1)),
      "SR"
    ]
  },
  7: {
    "element": "POLYGON",
    "id": 7,
    "type": "nP",
    "len": "nBP",
    "range": "VDCR"
  },
  8: {
    "element": "POLYGON_SET",
    "id": 8,
    "type": [
      "n",
      [
        "P",
        "E"
      ]
    ],
    "len": [
      "n",
      [
        "BP",
        "BE"
      ]
    ],
    "range": [
      "VDCR",
      SparseRange((range(0, 4),))
    ]
  },
  9: {
    "element": "CELL_ARRAY",
    "id": 9,
    "type": [
      "3P",
      "3I",
      "E",
      "CLIST"
    ],
    "len": [
      "3BP",
      "3BI",
      "BE",
      "nBCO"
    ],
    "range": [
      "VDCR",
      "IR",
      "IR",
      SparseRange((0, 1)),
      "COR"
    ]
  },
  10: {
    "element": "GENERALIZED_DRAWING_PRIMITIVE",
    "id": 10,
    "type": [
      "I",
      "I",
      "nP",
      "D"
    ],
    "len": [
      "2BI",
      "nBP",
      "BS"
    ],
    "range": [
      "IR",
      "IR",
      "VDCR",
      "SR"
    ]
  },
  11: {
    "element": "RECTANGLE",
    "id": 11,
    "type": "2P",
    "len": "2BP",
    "range": "VDCR"
  },
  12: {
    "element": "CIRCLE",
    "id": 12,
    "type": [
      "P",
      "VDC"
    ],
    "len": [
      "BP",
      "BVDC"
    ],
    "range": [
      "VDCR",
      "VDCR"
    ]
  },
  13: {
    "element": "CIRCULAR_ARC_POINT",
    "id": 13,
    "type": "3P",
    "len": "3BP",
    "range": "VDCR"
  },
  14: {
    "element": "CIRCULAR_ARC_3_POINT_CLOSE",
    "id": 14,
    "type": [
      "3P",
      "E"
    ],
    "len": [
      "3BP",
      "BE"
    ],
    "range": [
      "VDCR",
      SparseRange((0, 1))
    ]
  },
  15: {
    "element": "CIRCULAR_ARC_CENTER",
    "id": 15,
    "type": [
      "P",
      "4VDC",
      "VDC"
    ],
    "len": [
      "BP",
      "4BVDC",
      "BVDC"
    ],
    "range": [
      "VDCR",
      "VDCR",
      "VDCR"
    ]
  },
  16: {
    "element": "CIRCULAR_ARC_CENTER_CLOSE",
    "id": 16,
    "type": [
      "P",
      "4VDC",
      "VDC",
      "E"
    ],
    "len": [
      "BP",
      "4BVDC",
      "BVDC",
      "BE"
    ],
    "range": [
      "VDCR",
      "VDCR",
      "VDCR",
      SparseRange((0, 1))
    ]
  },
  17: {
    "element": "ELLIPSE",
    "id": 17,
    "type": "3P",
    "len": "3BP",
    "range": "VDCR"
  },
  18: {
    "element": "ELLIPTICAL_ARC",
    "id": 18,
    "type": [
      "3P",
      "4VDC"
    ],
    "len": [
      "3BP",
      "4BVDC"
    ],
    "range": [
      "VDCR",
      "VDCR"
    ]
  },
  19: {
    "element": "ELLIPTICAL_ARC_CLOSE",
    "id": 19,
    "type": [
      "3P",
      "4VDC",
      "E"
    ],
    "len": [
      "3BP",
      "4BVDC",
      "BE"
    ],
    "range": [
      "VDCR",
      "VDCR",
      SparseRange((0, 1))
    ]
  },
  20: {
    "element": "CIRCULAR_ARC_CENTER_REVERSED",
    "id": 20,
    "type": [
      "P",
      "4VDC",
      "VDC"
    ],
    "len": [
      "BP",
      "4BVDC",
      "BVDC"
    ],
    "range": [
      "VDCR",
      "VDCR",
      "VDCR"
    ]
  },
  21: {
    "element": "CONNECTING_EDGE",
    "id": 21,
    "type": None,
    "len": "0",
    "range": None
  },
  22: {
    "element": "HYPERBOLIC_ARC",
    "id": 22,
    "type": [
      "3P",
      "4VDC"
    ],
    "len": [
      "3BP",
      "4BVDC"
    ],
    "range": "VDCR"
  },
  23: {
    "element": "PARABOLIC_ARC",
    "id": 23,
    "type": "3P",
    "len": "3BP",
    "range": "VDCR"
  },
  24: {
    "element": "NON-UNIFORM_B-SPLINE",
    "id": 24,
    "type": [
      "2I",
      "nP",
      [
        [
          "n",
          "m"
        ],
        "R"
      ],
      "2R"
    ],
    "len": [
      "2BI",
      "nBP",
      [
        [
          "n",
          "m"
        ],
        "BR"
      ],
      "2BR"
    ],
    "range": [
      "IR",
      "VDCR",
      "RR",
      "RR"
    ]
  },
  25: {
    "element": "NON-UNIFORM_RATIONAL_B-SPLINE",
    "id": 25,
    "type": [
      "2I",
      "nP",
      [
        [
          "n",
          "m"
        ],
        "R"
      ],
      "2R",
      "nR"
    ],
    "len": [
      "2BI",
      "nBP",
      [
        [
          "n",
          "m"
        ],
        "BR"
      ],
      "2BR",
      "nBR"
    ],
    "range": [
      "IR",
      "VDCR",
      "RR",
      "RR",
      "RR"
    ]
  },
  26: {
    "element": "POLYBEZIER",
    "id": 26,
    "type": [
      "IX",
      [
        "4nP",
        "or"
      ],
      [
        [
          "3n",
          "1"
        ],
        "P"
      ]
    ],
    "len": [
      "BIX",
      [
        "4nBP",
        "or"
      ],
      "BIX",
      [
        [
          "3n",
          "1"
        ],
        "P"
      ]
    ],
    "range": [
      SparseRange((1, 2)),
      "VDCR"
    ]
  },
  27: {
    "element": "POLYSYMBOL",
    "id": 27,
    "type": [
      "IX",
      "nP"
    ],
    "len": [
      "BIX",
      "nBP"
    ],
    "range": [
      "IXR",
      "VDCR"
    ]
  },
  28: {
    "element": "BITONAL_TILE",
    "id": 28,
    "type": [
      "IX",
      "I",
      "2CO",
      "SDR",
      "BS"
    ],
    "len": [
      "BIX",
      "BIX",
      "2BCO",
      "BSDR",
      "BBS"
    ],
    "range": [
      "IXR",
      "IR",
      "COR",
      "n/a",
      "BSR"
    ]
  },
  29: {
    "element": "TILE",
    "id": 29,
    "type": [
      "IX",
      "I",
      "I",
      "SDR",
      "BS"
    ],
    "len": [
      "BIX",
      "BI",
      "BI",
      "BSDR",
      "BB",
      "S"
    ],
    "range": [
      "IXR",
      "IR",
      "IR",
      "n/a",
      "BSR"
    ]
  }
}

cgm_attribute_elements = {
  1: {
    "element": "LINE_BUNDLE_INDEX",
    "id": 1,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  2: {
    "element": "LINE_TYPE",
    "id": 2,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  3: {
    "element": "LINE_WIDTH",
    "id": 3,
    "type": "SS",
    "len": "BSS",
    "range": "SSR"
  },
  4: {
    "element": "LINE_COLOR",
    "id": 4,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  5: {
    "element": "MARKER_BUNDLE_INDEX",
    "id": 5,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  6: {
    "element": "MARKER_TYPE",
    "id": 6,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  7: {
    "element": "MARKER_SIZE",
    "id": 7,
    "type": "SS",
    "len": "BSS",
    "range": "SSR"
  },
  8: {
    "element": "MARKER_COLOR",
    "id": 8,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  9: {
    "element": "TEXT_BUNDLE_INDEX",
    "id": 9,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  10: {
    "element": "TEXT_FONT_INDEX",
    "id": 10,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  11: {
    "element": "TEXT_PRECISION",
    "id": 11,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 3),))
  },
  12: {
    "element": "CHARACTER_EXPANSION_FACTOR",
    "id": 12,
    "type": "R",
    "len": "BR",
    "range": "RR"
  },
  13: {
    "element": "CHARACTER_SPACING",
    "id": 13,
    "type": "R",
    "len": "BR",
    "range": "RR"
  },
  14: {
    "element": "TEXT_COLOR",
    "id": 14,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  15: {
    "element": "CHARACTER_HEIGHT",
    "id": 15,
    "type": "VDC",
    "len": "BVDC",
    "range": "VDCR"
  },
  16: {
    "element": "CHARACTER_ORIENTATION",
    "id": 16,
    "type": "4VDC",
    "len": "4BVDC",
    "range": "VDCR"
  },
  17: {
    "element": "TEXT_PATH",
    "id": 17,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 4),))
  },
  18: {
    "element": "TEXT_ALIGNMENT",
    "id": 18,
    "type": [
      "2E",
      "R",
      "R"
    ],
    "len": [
      "2BE",
      "2BR"
    ],
    "range": [
      SparseRange((range(0, 5),)),
      SparseRange((range(0, 7),)),
      "2RR"
    ]
  },
  19: {
    "element": "CHARACTER_SET_INDEX",
    "id": 19,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  20: {
    "element": "ALTERNATE_CHARACTER_SET_INDEX",
    "id": 20,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  21: {
    "element": "FILL_BUNDLE_INDEX",
    "id": 21,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  22: {
    "element": "INTERIOR_STYLE",
    "id": 22,
    "type": "E",
    "len": "BE",
    "range": SparseRange((range(0, 7),))
  },
  23: {
    "element": "FILL_COLOR",
    "id": 23,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  24: {
    "element": "HATCH_INDEX",
    "id": 24,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  25: {
    "element": "PATTERN_INDEX",
    "id": 25,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  26: {
    "element": "EDGE_BUNDLE_INDEX",
    "id": 26,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  27: {
    "element": "EDGE_TYPE",
    "id": 27,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  # 28 was manually added because the PDF is missing it?
  28: {
    "element": "EDGE_WIDTH",
    "id": 28,
    "type": "SS",
    "len": "BSS",
    "range": "SSR"
  },
  29: {
    "element": "EDGE_COLOR",
    "id": 29,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  30: {
    "element": "EDGE_VISIBILITY",
    "id": 30,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1))
  },
  31: {
    "element": "FILL_REFERENCE_POINT",
    "id": 31,
    "type": "P",
    "len": "BP",
    "range": "VDCR"
  },
  32: {
    "element": "PATTERN_TABLE",
    "id": 32,
    "type": [
      "IX",
      "3I",
      "nx*nyCO"
    ],
    "len": [
      "BIX",
      "3BI",
      "nx*nyBCO"
    ],
    "range": [
      "IXR",
      "IR",
      "IR",
      "COR"
    ]
  },
  33: {
    "element": "PATTERN_SIZE",
    "id": 33,
    "type": "4SS",
    "len": "4BSS",
    "range": "SSR"
  },
  34: {
    "element": "COLOR_TABLE",
    "id": 34,
    "type": [
      "CI",
      "nCD"
    ],
    "len": [
      "BCI",
      "nBCD"
    ],
    "range": [
      "CIR",
      "CCOR"
    ]
  },
  35: {
    "element": "ASPECT_SOURCE_FLAGS",
    "id": 35,
    "type": [
      "n",
      [
        "E",
        "E"
      ]
    ],
    "len": [
      "n",
      "2BE"
    ],
    "range": [
      SparseRange((range(0, 18),)),
      SparseRange((0, 1))
    ]
  },
  36: {
    "element": "PICK_IDENTIFIER",
    "id": 36,
    "type": "N",
    "len": "BN",
    "range": "NR"
  },
  37: {
    "element": "LINE_CAP",
    "id": 37,
    "type": [
      "IX",
      "IX"
    ],
    "len": "2BIX",
    "range": "IXR"
  },
  38: {
    "element": "LINE_JOIN",
    "id": 38,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  39: {
    "element": "LINE_TYPE_CONTINUATION",
    "id": 39,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  40: {
    "element": "LINE_TYPE_INITIAL_OFFSET",
    "id": 40,
    "type": "R",
    "len": "BR",
    "range": "RR"
  },
  41: {
    "element": "TEXT_SCORE_TYPE",
    "id": 41,
    "type": [
      "n",
      [
        "IX",
        "E"
      ]
    ],
    "len": [
      "nBIX",
      "nBE"
    ],
    "range": [
      "IXR",
      SparseRange((0, 1))
    ]
  },
  42: {
    "element": "RESTRICTED_TEXT_TYPE",
    "id": 42,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  43: {
    "element": "INTERPOLATED_INTERIOR",
    "id": 43,
    "type": [
      "IX",
      "2nSS",
      "I",
      "mR",
      "kCO"
    ],
    "len": [
      "2BIX",
      "2nBSS",
      "BI",
      "mBR",
      "kBCO"
    ],
    "range": [
      SparseRange((range(1, 4),)),
      "SSR",
      "IR",
      "RR",
      "COR"
    ]
  },
  44: {
    "element": "EDGE_CAP",
    "id": 44,
    "type": [
      "IX",
      "IX"
    ],
    "len": "2BIX",
    "range": "IXR"
  },
  45: {
    "element": "EDGE_JOIN",
    "id": 45,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  46: {
    "element": "EDGE_TYPE_CONTINUATION",
    "id": 46,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  47: {
    "element": "EDGE_TYPE_INITIAL_OFFSET",
    "id": 47,
    "type": "R",
    "len": "BR",
    "range": "RR"
  },
  48: {
    "element": "SYMBOL_LIBRARY_INDEX",
    "id": 48,
    "type": "IX",
    "len": "BIX",
    "range": "IXR"
  },
  49: {
    "element": "SYMBOL_COLOR",
    "id": 49,
    "type": "CO",
    "len": "BCO",
    "range": "COR"
  },
  50: {
    "element": "SYMBOL_SIZE",
    "id": 50,
    "type": [
      "E",
      "2VDC"
    ],
    "len": [
      "BE",
      "2BVDC"
    ],
    "range": [
      SparseRange((range(0, 3),)),
      "VDCR"
    ]
  },
  51: {
    "element": "SYMBOL_ORIENTATION",
    "id": 51,
    "type": "4VDC",
    "len": "4BVDC",
    "range": "VDCR"
  }
}

cgm_escape_elements = {
  1: {
    "element": "ESCAPE",
    "id": 1,
    "type": [
      "I",
      "D"
    ],
    "len": [
      "BI",
      "BS"
    ],
    "range": [
      "IR",
      "SR"
    ]
  }
}

cgm_external_elements = {
  1: {
    "element": "MESSAGE",
    "id": 1,
    "type": [
      "E",
      "SF"
    ],
    "len": [
      "BE",
      "BS"
    ],
    "range": [
      SparseRange((0, 1)),
      "SR"
    ]
  },
  2: {
    "element": "APPLICATION_DATA",
    "id": 2,
    "type": [
      "I",
      "D"
    ],
    "len": [
      "BI",
      "BS"
    ],
    "range": [
      "IR",
      "SR"
    ]
  }
}

cgm_segment_elements = {
  1: {
    "element": "COPY_SEGMENT",
    "id": 1,
    "type": [
      "N",
      "4R",
      "2VDC",
      "E"
    ],
    "len": [
      "BN",
      "4BR",
      "2BVDC ",
      "BE"
    ],
    "range": [
      "NR",
      "RR",
      "VDCR",
      SparseRange((0, 1))
    ]
  },
  2: {
    "element": "INHERITANCE_FILTER",
    "id": 2,
    "type": [
      "nE",
      "E"
    ],
    "len": [
      [
        "n",
        "1"
      ],
      "BE"
    ],
    "range": [
      SparseRange((range(0, 87),)),
      SparseRange((0, 1))
    ]
  },
  3: {
    "element": "CLIP_INHERITANCE",
    "id": 3,
    "type": "E",
    "len": "BE",
    "range": SparseRange((0, 1))
  },
  4: {
    "element": "SEGMENT_TRANSFORMATION",
    "id": 4,
    "type": [
      "N",
      "4R",
      "2VDC"
    ],
    "len": [
      "BN",
      "4BR",
      "2BVDC"
    ],
    "range": [
      "NR",
      "RR",
      "VDCR"
    ]
  },
  5: {
    "element": "SEGMENT_HIGHLIGHTING",
    "id": 5,
    "type": [
      "N",
      "E"
    ],
    "len": [
      "BN",
      "BE"
    ],
    "range": [
      "NR",
      SparseRange((0, 1))
    ]
  },
  6: {
    "element": "SEGMENT_DISPLAY_PRIORITY",
    "id": 6,
    "type": [
      "N",
      "I"
    ],
    "len": [
      "BN",
      "BI"
    ],
    "range": [
      "NR",
      "IR"
    ]
  },
  7: {
    "element": "SEGMENT_PICK_PRIORITY",
    "id": 7,
    "type": [
      "N",
      "I"
    ],
    "len": [
      "BN",
      "BI"
    ],
    "range": [
      "NR",
      "IR"
    ]
  }
}

cgm_application_elements = {
  1: {
    "element": "APPLICATION_STRUCTURE_ATTRIBUTE",
    "id": 1,
    "type": [
      "SF",
      "SDR"
    ],
    "len": [
      "BS",
      "BS"
    ],
    "range": [
      "SR",
      "SR"
    ]
  }
}

cgm_class_codes = {
  0: cgm_delimiter_elements,
  1: cgm_metafile_descriptor_elements,
  2: cgm_picture_descriptor_elements,
  3: cgm_control_elements,
  4: cgm_graphical_primitive_elements,
  5: cgm_attribute_elements,
  6: cgm_escape_elements,
  7: cgm_external_elements,
  8: cgm_segment_elements,
  9: cgm_application_elements,
}
