#!/usr/bin/env python3

from .cgm import CGM


def main(filename):
    c = CGM(filename)
    c.parse()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='CGM file to parse')
    args = parser.parse_args()

    main(**vars(args))

