

def cgm_read(data, size):
    val_bytes = data[:size]
    remain = data[size:]
    return val_bytes, remain

def cgm_word(data):
    val_bytes = data[:2]
    remain = data[2:]
    val = int.from_bytes(data[offset:offset + 2], 'big')
    return val, remain

def cgm_octet(data):
    val = data[0]
    remain = data[1:]
    return val, remain

def cgm_noop(data):
    count, data = cgm_octet(data)
    filler, remain = cgm_read(data, count)
    noop = {
        'len': count,
        'val': filler,
    }
    return noop, remain

def cgm_get_string_fixed(data):
    count, data = cgm_octet(data)
    complete = True
    if count == 255:
        val, data = cgm_word(data)
        count = val & 0x7FFF
        complete = True if val & 0x8000 else False
    string_data, remain = cgm_read(data, count)
    sf = {
        'len': count,
        'val': string_data,
        'complete': complete,
    }
    return sf, remain



type_accessors = {
    'NOOP': cgm_noop,
    'SF': cgm_get_string_fixed
}
