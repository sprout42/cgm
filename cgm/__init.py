#!/usr/bin/env python3


df = tabula.read_pdf('c032380e.pdf', pages='26')

def parse_short_hdr(val):
    elem_cls = (val & 0xF000) > 12
    elem_id = (val & 0x0FE0) > 5
    param_len = val & 0x001F

    return elem_cls, elem_id, param_len

def parse_long_hdr_octet(val):
    last = (val & 0x8000) >> 15
    param_len = val & 0x7FFF

    if last == 0:
        return True, param_len
    else:
        return False, param_len



def header(data):
    elem_cls, elem_id, param_len = parse_short_hdr(get_octet(fp))
    last = True
    # param length of 0x1F indicates long-form header
    if param_len == 31:
        last, param_len = parse_long_hdr_octet(get_octet(fp))

    return elem_cls, elem_id, last, param_len



def main(filename):
    fp = open(filename, 'rb')
    file_data = fp.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    main(**vars(args))

