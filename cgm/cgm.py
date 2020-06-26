
import argparse

from .file import CGMFile
from .config import CGMConfig
from .types import CGMTopLevelType


class CGM(object):
    def __init__(self, filename):
        self.fp = CGMFile(filename)
        self.config = [CGMConfig()]

        self.values = []

    def parse(self):
        try:
            while True:
                obj = CGMTopLevelType(fp=self.fp, config=self.config[-1])
                print(obj)
                self.values.append(obj)
        except EOFError:
            pass

        return self.values


def run(filename):
    c = CGM(filename)
    results = c.parse()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='CGM file to parse')
    args = parser.parse_args()
    run(args.filename)
