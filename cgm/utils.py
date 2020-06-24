def word(data):
    val_bytes = data[:2]
    remain = data[2:]
    val = int.from_bytes(data[offset:offset + 2], 'big')
    return val, remain


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
