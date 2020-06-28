
import argparse
import json

from .file import CGMFile
from .config import CGMConfig
from .types import CGMTopLevelType, CGMBaseType


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

    def print(self):
        for val in self.values:
            # val is a top-level type
            unwrapped_data = val.unwrap()
            if isinstance(unwrapped_data, str):
                print(unwrapped_data)
            else:
                cmd = unwrapped_data[0]
                rest = json.dumps(unwrapped_data[1:], indent=4)
                print(f'{cmd}: {rest}')


def run(filename):
    c = CGM(filename)
    c.print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='CGM file to parse')
    args = parser.parse_args()
    run(args.filename)
