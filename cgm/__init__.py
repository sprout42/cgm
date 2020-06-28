import argparse

from .cgm import *
from .file import *
from .config import *
from . import types

def run(args):
    print(args)
    c = CGM(args.filename)
    if args.exclude_elements:
        # normalize the exclude element list
        exclude_elems = [e.upper() for e in args.exclude_elements]
        c.print(exclude_elems)
    elif args.metadata_only:
        c.print(non_metadata_elements)
    else:
        c.print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
            help='CGM file to parse')
    parser.add_argument('-m', '--metadata-only', action='store_true',
            help='print only extracted metadata elements')
    parser.add_argument('-e', '--exclude-elements', nargs='*',
            help='CGM elements to exclude from printing')
    args = parser.parse_args()
    run(args)
