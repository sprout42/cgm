
def word(data, offset=0):
    val = int.from_bytes(data[offset:offset + 2], 'big')
    return val


def assert_word_len(one, two):
    # Since file positions need to be rounded up to the nearest 16bits, compare 
    # two sizes rounded up and make sure they match
    assert (one + 1) // 2 == (two + 1) // 2


def sign_bit(bits):
    return 1 << bits - 1


def bit_mask(bits):
    return ~((-1) << bits)


def unsigned(value, size):
    return value & bit_mask(size)


def signed(value, size):
    x = unsigned(value, size)
    if x & sign_bit(size):
        x = x - (1 << size)
    return x


def get_range(val):
    parts = val.split('..')
    if len(parts) == 1:
        return int(parts[0])
    else:
        return range(int(parts[0]), int(parts[1]) + 1)


class OffsetStr(str):
    def __new__(cls, val):
        return super().__new__(cls, val)

    def __repr__(self):
        cls = self.__class__.__name__
        val_str = super().__repr__()
        return f'{cls}({val_str})'


class OffsetList(list):
    def __new__(cls, val):
        return super().__new__(cls, val)

    def __repr__(self):
        cls = self.__class__.__name__
        val_str = super().__repr__()
        return f'{cls}({val_str})'


class SparseRange(tuple):
    def __new__(cls, val):
        if isinstance(val, str):
            return super().__new__(cls, (get_range(v) for v in val.split(',')))
        else:
            return super().__new__(cls, val)

    def __iter__(self):
        for val in super().__iter__():
            try:
                for i in val:
                    yield i
            except TypeError:
                yield val

    def __contains__(self, key):
        for val in super().__iter__():
            try:
                if key in val:
                    return True
            except TypeError:
                if key == val:
                    return True
        return False

    def __repr__(self):
        cls = self.__class__.__name__
        val_str = super().__repr__()
        return f'{cls}({val_str})'
