#!/usr/bin/env python
#
# pip install tabula-py

import re
#import pprint
import json
import tabula
import numpy as np


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
                'coords': (0, 595, 160, 510),
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
                elif 'element' in latest and isinstance(latest['element'], list):
                    out[key][-1]['element'] = '_'.join(latest['element'])

    return out


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

    # Write out the non-class tables
    table_list = [r['type'] for r in class_table]
    for table in table_list:
        table_name = class_name_map[table]
        table_str = json.dumps(tables[table_name], indent=2)
        pyfile.write(f'{table_name} = {table_str}\n\n')


    # Write out this table manually so that it references the other tables in 
    # the file rather than strings
    pyfile.write('cgm_class_codes = [\n')
    for row in class_table:
        out_fmt = '  { "class": %s, "type": %s },\n'
        pyfile.write(out_fmt % (row['class'], class_name_map[row['type']]))
    pyfile.write(']\n')


def main(pdf_filename, output_filename):
    tables = parse(pdf_filename)
    #pprint.pprint(tables)
    #print(json.dumps(tables, indent=4))
    save(output_filename, tables)


if __name__ == '__main__':
    pdf_filename = 'docs/c032380e.pdf'
    output_filename = 'cgm_types.py'
    main(pdf_filename, output_filename)
