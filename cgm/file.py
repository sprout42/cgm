
class CGMFile(object):
    def __init__(self, filename):
        self.fp = open(filename, 'rb')

    def read(self, size):
        data = self.fp.read(size)
        print(f'@ {self.tell()} read({size}): {data.hex()}')
        return data

    def tell(self):
        return self.fp.tell()

    def next(self):
        # move to the next "word" boundary
        pos = self.tell()
        if pos % 2 == 1:
            _ = self.read(1)
