import functools

from .base import CGMVariableType
from .integer import _N, _E, _I, _IF8, _IF16, _IF32, _IX, _UI8, _UI16, _UI32
from .real import _R
from .color import _CI, _CD, _CCO
from .string import _SF, _S
from .vdc import _VDC


class _SDR(CGMVariableType):
    _data_types = {
        #1: _SDR,
        2: _CI,
        3: _CD,
        4: _N,
        5: _E,
        6: _I,
        #7: reserved,
        8: _IF8,
        9: _IF16,
        10: _IF32,
        11: _IX,
        12: _R,
        13: _S,
        14: _SF,
        #15: _VC,
        16: _VDC,
        17: _CCO,
        18: _UI8,
        19: _UI32,
        #20: BS,
        #21: CL,
        22: _UI16,
    }

    def __init__(self, fp, config):
        # Make sure to align file pointer to a word boundary before extracting 
        # an SDR, do this before the constructor so the starting offset is 
        # accurate.
        fp.next()
        super().__init__(fp=fp, config=config, param_len=None)

    def extract(self):
        # Get the SDR size from the first element
        self.sdr_len = _I(fp=self.fp, config=self.config)
        self.param_len = self.sdr_len.unwrap()
        super().extract()

    def extract_items(self):
        item = {
            'type': _IX(fp=self.fp, config=self.config),
            'len': _I(fp=self.fp, config=self.config),
        }

        item_type_index = item['type'].unwrap()
        item_len = item['len'].unwrap()
        print(item_type_index, item_len)
        if item_type_index in self._data_types:
            args = {
                'config': self.config,
                'fp': self.fp,
            }
            item_type = self._data_types[item_type_index]
            elems = []
            elem_len_sum = 0
            while elem_len_sum < item_len:
                elems.append(item_type(**args))
                elem_len_sum += elems[-1].size
            item['elements'] = tuple(elems)
        else:
            raise ValueError(f'Bad SDR type index: {item_type_index}')
        return item


__all__ = [
    '_SDR',
]
