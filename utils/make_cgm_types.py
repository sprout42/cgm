#!/usr/bin/env python
#
# pip install tabula-py

import re
import json
import tabula
import argparse

# This is silly but I'll do it for a util script
import os.path
parent_dir = os.path.join(os.path.dirname(__file__), '..')
import sys
sys.path.append(parent_dir)

from cgm.utils import SparseRange, OffsetList, OffsetStr

# Wrapper types for SparseRange and Offset to make it easier to serialize them
class OffsetWrapper(object):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            self._obj = OffsetStr(*args)
        else:
            self._obj = OffsetList(*args)

    def __repr__(self):
        return repr(self._obj)

    def __str__(self):
        return repr(self._obj)


class SparseRangeWrapper(object):
    def __init__(self, *args):
        self._obj = SparseRange(*args)

    def __repr__(self):
        return repr(self._obj)

    def __str__(self):
        return repr(self._obj)


def element_formatter(val):
    if val == '':
        return None
    else:
        return str(re.sub(r'\s+', '_', val).upper())


def class_name_formatter(val):
    return str('cgm_' + re.sub(r'\s+', '_', val).lower())


def field_formatter(val):
    if val == '':
        return None
    elif val[-1] == ',':
        return str(val[:-1])
    else:
        return str(val)


def id_formatter(val):
    if val == '':
        return None
    else:
        return str(val)
        #try:
        #    return int(val)
        #except ValueError:
        #    return str(val)

# The coordinates here assume the coordinates used by skim.app:
#   coordinates starting at the lower left of the highlighted box
#   x_start, width, y_start, height
#
# To make them match what tabula expects, subtract the pixel height of 
# 840 from the y coordinate to reverse the y axis
table_config = {
    'cgm_class_codes': {
        'columns': ['class', 'type'],
        'types': [None, None],
        'converters': [id_formatter, class_name_formatter],
        'pages': [
            {
                'page': 23,
                'coords': (0, 595, 495, 135),
            },
        ],
    },
    'cgm_delimiter_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 24,
                'coords': (0, 595, 375, 295),
            },
        ],
    },
    'cgm_metafile_descriptor_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 26,
                'coords': (0, 595, 162, 518),
            },
        ],
    },
    'cgm_picture_descriptor_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 33,
                'coords': (0, 595, 150, 525),
            },
        ],
    },
    'cgm_control_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 38,
                'coords': (0, 595, 65, 350),
            },
        ],
    },
    'cgm_graphical_primitive_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 41,
                'coords': (0, 595, 495, 180),
            },
            {
                'page': 42,
                'coords': (0, 595, 135, 560),
            },
        ],
    },
    'cgm_attribute_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
            {
                'page': 49,
                'coords': (0, 595, 135, 540),
            },
            {
                'page': 50,
                'coords': (0, 595, 330, 370),
            },
        ],
    },
    'cgm_escape_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
                {
                'page': 58,
                'coords': (0, 595, 640, 30),
            },
        ],
    },
    'cgm_external_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
                {
                'page': 59,
                'coords': (0, 595, 635, 40),
            },
        ],
    },
    'cgm_segment_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
                {
                'page': 60,
                'coords': (0, 595, 505, 165),
            },
        ],
    },
    'cgm_application_elements': {
        'columns': ['element', 'id', 'type', 'len', 'range'],
        'types': [None, None, None, None, None],
        'converters': [element_formatter, id_formatter, field_formatter, field_formatter, field_formatter],
        'pages': [
                {
                'page': 64,
                'coords': (0, 595, 640, 30),
            },
        ],
    },
}


def tabulaify_coords(x, width, y, height, page_height=840):
    x_start = x
    x_end = width - x_start
    y_start = page_height - (y + height)
    y_end = y_start + height
    # Return the coordinates using the x/y (0/0) location and, order, and units 
    # expected by tabula.  tabula uses "pdf units" which are 1/72 of an inch.  
    # Thankfully that's the same unit used by skim.
    return y_start, x_start, y_end, x_end


def valid_row(row):
    return all(x is not None for x in row)


def split_list_str(value):
    if value is None:
        return value

    # If the input value is a list, join all lines with a comma
    if isinstance(value, list):
        value = ','.join(value)

    # Now split on all non-enclosed commas
    parts = [
        r'[^-+,\{\(\[]+',
        r'\([^\)]+\)',
        r'\[[^\]]+\]',
        r'\{[^\}]+\}',
        r', ?',
        r'\+ ?',
        r'- ?',
    ]

    pat_str = r'|'.join([f'({p})' for p in parts])
    pat = re.compile(pat_str)

    # Remove all of the empty elements from the list
    val_list = [v for v in pat.split(value) if v]

    # Start with only one element in the results list that is an empty string
    result = [[]]
    for val in val_list:
        if val in [',', '+', '-', ', ', '+ ', '- ']:
            # Only start a new element if the previous is not empty
            if result[-1] != []:
                result.append([])
        else:
            result[-1].append(val)

    # Now go through and re-process any elements that aren't complete
    processed_results = []
    for val_list in result:
        line = []
        for val in val_list:
            if val[0] == '(':
                assert val[-1] == ')'
                val = split_list_str(val[1:-1])
            elif val[0] == '[':
                assert val[-1] == ']'
                val = OffsetWrapper(split_list_str(val[1:-1]))
            elif val[0] == '{':
                assert val[-1] == '}'
                val = SparseRangeWrapper(val[1:-1])

            line.append(val)

        if len(line) == 1:
            processed_results.append(line[0])
        else:
            processed_results.append(tuple(line))

    if len(processed_results) == 1:
        return processed_results[0]
    else:
        return tuple(processed_results)


def parse(pdf_filename):
    out = {}
    for key in table_config:
        out[key] = []

        col_names = table_config[key]['columns']
        col_types = dict((n, t) for n, t in zip(col_names, table_config[key]['types']) if t is not None)
        col_converters = dict((n, t) for n, t in zip(col_names, table_config[key]['converters']) if t is not None)

        for entry in table_config[key]['pages']:
            coords = tabulaify_coords(*entry['coords'])
            options = {
                'area': coords,
                'pages': entry['page'],
                'guess': False,
                'multiple_tables': False,
                'pandas_options': {
                    'header': None,
                    'names': col_names,
                    'dtype': col_types,
                    'converters': col_converters,
                    'keep_default_na': False,
                    'na_values': [],
                },
            }
            df = tabula.read_pdf(pdf_filename, **options)
            assert len(df[0].columns) == len(col_names)

            # Populate the data based for each row
            for i in range(len(df[0])):
                row = list(df[0].loc[i])
                if valid_row(row):
                    merged_data = dict(zip(col_names, row))
                    out[key].append(merged_data)
                else:
                    for col, val in zip(col_names, row):
                        if val is not None:
                            try:
                                out[key][-1][col].append(val)
                            except AttributeError:
                                old = out[key][-1][col]
                                out[key][-1][col] = [old, val]

                latest = out[key][-1]
                if 'id' in latest and isinstance(latest['id'], str):
                    out[key][-1]['id'] = int(latest['id'])
                if 'class' in latest and isinstance(latest['class'], str):
                    try:
                        out[key][-1]['class'] = int(latest['class'])
                    except ValueError:
                        # If the class is invalid then this is the "reserved" 
                        # line, just delete this row
                        out[key] = out[key][:-1]

        # loop through the parsed table rows and make some adjustments
        for row in out[key]:
            if 'element' in row:
                if isinstance(row['element'], list):
                    row['element'] = '_'.join(row['element'])

                # Also join the 'type', 'len', and 'range' fields together 
                # unless there is an 'or' element in the list
                for field in['type', 'len', 'range']:
                    if row[field] == 'see below':
                        row[field] = 'NOOP'
                    elif row[field] == 'n/a':
                        row[field] = None
                    else:
                        # Now split on all non-enclosed commas
                        row[field] = split_list_str(row[field])

    return out


class json_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, OffsetWrapper):
            return str(obj)
        elif isinstance(obj, SparseRangeWrapper):
            return str(obj)

        return super().encode(obj)


def save(output_filename, tables):
    class_table = tables['cgm_class_codes']
    class_name_map = {
        'cgm_delimiter_elements': 'cgm_delimiter_elements',
        'cgm_metafile_descriptor_elements': 'cgm_metafile_descriptor_elements',
        'cgm_picture_descriptor_elements': 'cgm_picture_descriptor_elements',
        'cgm_control_elements': 'cgm_control_elements',
        'cgm_graphical_primitive_elements': 'cgm_graphical_primitive_elements',
        'cgm_attribute_elements': 'cgm_attribute_elements',
        'cgm_escape_element': 'cgm_escape_elements',
        'cgm_external_elements': 'cgm_external_elements',
        'cgm_segment_control_and_segment_attribute_elements': 'cgm_segment_elements',
        'cgm_application_structure_descriptor_elements': 'cgm_application_elements',
    }

    assert len(tables) == len(class_table) + 1

    pyfile = open(output_filename, 'w')

    # import the required types first
    pyfile.write('from cgm.utils import SparseRange, OffsetList, OffsetStr\n\n\n')

    # Write out the non-class tables
    table_list = [r['type'] for r in class_table]
    for table in table_list:
        table_name = class_name_map[table]
        # restructure the table so that instead of a list of elements each one 
        # is a dict indexed by the 'id' of that element
        out_table = dict((v['id'], v) for v in tables[table_name])
        table_str = json.dumps(out_table, indent=2, cls=json_encoder)

        # I do want 'None' instead of 'null' because this is a python file being 
        # created, just using json.dumps() for formatting convenience.
        table_str = re.sub(r'null', r'None', table_str)

        # Similarly, un-jsonify any integer keys
        table_str = re.sub(r'"([0-9]+)":', r'\1:', table_str)

        # Remove the wrapping quotes from around the custom types
        table_str = re.sub(r'"(SparseRange\(.*\))"', r'\1', table_str)
        table_str = re.sub(r'"(OffsetList\(.*\))"', r'\1', table_str)
        table_str = re.sub(r'"(OffsetStr\(.*\))"', r'\1', table_str)

        pyfile.write(f'{table_name} = {table_str}\n\n')

    # Write out this table manually so that it references the other tables in 
    # the file rather than strings. Instead of a list it should be a dict using 
    # the 'class' as the key.
    pyfile.write('cgm_class_codes = {\n')
    for row in class_table:
        pyfile.write(f'  {row["class"]}: {class_name_map[row["type"]]},\n')
    pyfile.write('}\n')


def main(pdf_filename, output_filename):
    tables = parse(pdf_filename)
    #pprint.pprint(tables)
    #print(json.dumps(tables, indent=4))
    save(output_filename, tables)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cgm', help='CGM file to parse')
    parser.add_argument('py', help='output file for the parsed python data')
    args = parser.parse_args()

    main(args.cgm, args.py)
