
class CGMFile(object):
    def __init__(self, filename):
        self.fp = open(filename, 'rb')

    def read(self, size):
        ## Round up
        #if size % 1 != 0:
        #    size += 1
        return self.fp.read(size)

    def tell(self):
        return self.fp.tell()
