
import sys
import os
import os.path
import argparse

from .cgm import *
from .file import *
from .config import *
from . import types

def parse(filenames):
    parsed = {}
    for filename in args.filename:
        print(f'PARSING {filename}')
        c = CGM(filename)
        parsed[filename] = c

    return parsed


def run(args):
    if args.output is None:
        # Print to sdtout
        outfile = sys.stdout
    else:
        if args.output[0] is not None:
            if os.path.isdir(args.output[0]):
                # Use this directory as the base for the automatically created 
                # output files
                outputdir = args.output[0]
                outfile = None
            else:
                outfile = open(args.output[0], 'w')
        else:
            outputdir = os.getcwd()
            outfile = None

    parsed = parse(args.filename)
    for filename in parsed:
        c = parsed[filename]

        if outfile is None:
            auto_out_filename = os.path.split(filename)[1] + '-parsed.txt'
            outputfilename = os.path.join(outputdir, auto_out_filename)
            _outfile = open(outputfilename , 'w')
        else:
            _outfile = outfile

        if args.exclude_elements:
            # normalize the exclude element list
            exclude_elems = [e.upper() for e in args.exclude_elements]
            c.print(exclude_elems, file=_outfile)
        elif args.metadata_only:
            c.print(non_metadata_elements, file=_outfile)
        else:
            c.print(file=_outfile)

        if outfile is None:
            _outfile.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='+',
            help='CGM file(s) to parse')
    parser.add_argument('-m', '--metadata-only', action='store_true',
            help='print only extracted metadata elements')
    parser.add_argument('-e', '--exclude-elements', nargs='*',
            help='CGM elements to exclude from printing')
    parser.add_argument('-o', '--output', nargs='?', action='append',
            help='save the output to a file instead of stdout')
    args = parser.parse_args()
    run(args)
