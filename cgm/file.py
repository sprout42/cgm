
class CGMFile(object):
    def __init__(self, filename):
        self.fp = open(filename, 'rb')

    def read(self, size):
        data = self.fp.read(size)
        if len(data) == 0 and size != 0:
            raise EOFError
        return data

    def tell(self):
        return self.fp.tell()

    def next(self):
        # move to the next "word" boundary
        pos = self.tell()
        if pos % 2 == 1:
            _ = self.read(1)
