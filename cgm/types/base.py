
from cgm.utils import word
from . import parsed_types

class CGMBaseType(object):
    def __init__(self, fp, config):
        self.fp = fp
        self.config = config

        self.offset = fp.tell()
        self.extract()

        # Save how many byte were captured for this type
        self.size = fp.tell() - self.offset

    def extract(self):
        raise NotImplementedError

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.__class__.__name__}({self.value})'

    @classmethod
    def _unwrap(cls, value):
        if issubclass(value.__class__, CGMBaseType):
            return value.value
        else:
            return value

    def unwrap(self):
        # The value of the parsed types is often a tuple, with other primitive 
        # types under it.  return the bare values but maintain the list/tuple 
        # structure.
        if isinstance(self.value, list):
            unwrapped_list = list(CGMBaseType._unwrap(v) for v in self.value)
            if len(unwrapped_list) == 1:
                return unwrapped_list[0]
            else:
                return unwrapped_list
        elif isinstance(self.value, tuple):
            unwrapped_tuple = tuple(CGMBaseType._unwrap(v) for v in self.value)
            if len(unwrapped_tuple) == 1:
                return unwrapped_tuple[0]
            else:
                return unwrapped_tuple
        elif isinstance(self.value, dict):
            return dict((k, CGMBaseType._unwrap(v)) for k, v in self.value.items())
        else:
            return CGMBaseType._unwrap(self.value)


class CGMVariableType(CGMBaseType):
    def __init__(self, fp, config, param_len):
        self.param_len = param_len
        super().__init__(fp=fp, config=config)

    def _sum_item_size(self, item):
        if isinstance(item, dict):
            return sum(self._sum_item_size(v) for v in item.values())
        elif isinstance(item, list) or isinstance(item, tuple):
            return sum(self._sum_item_size(i) for i in item)
        else:
            return item.size

    def extract(self):
        # Only extract strings until the length matches the font list size
        max_len = self.param_len

        items_list = []
        items_len = 0
        while items_len < max_len:
            items = self.extract_items()
            items_len += self._sum_item_size(items)
            items_list.append(items)

        self.value = tuple(items_list)

    def extract_items(self):
        raise NotImplementedError


class COMMAND(CGMBaseType):
    def extract(self):
        self.raw = self.fp.read(2)
        val = word(self.raw)
        self.elem_cls = (val & 0xF000) >> 12
        self.elem_id = (val & 0x0FE0) >> 5
        self.param_len = val & 0x001F

        if self.param_len == 31:
            self.raw += self.fp.read(2)
            val = word(self.raw, 2)
            self.param_len = val & 0x7FFF
            # 0 means "last", 1 means "not last"
            self.complete = not bool(val & 0x8000)
        else:
            self.complete = True

        # Get the name of this element for debugging purposes
        print(self.elem_cls, self.elem_id, self.complete)
        elem_list = parsed_types.cgm_class_codes[self.elem_cls]
        self.elem = elem_list[self.elem_id]

    def __str__(self):
        if self.complete:
            return f'{self.__class__.__name__}({self.elem["element"]}: {self.elem_cls}, {self.elem_id}, {self.param_len})'
        else:
            return f'{self.__class__.__name__}({self.elem["element"]} INCOMPLETE : {self.elem_cls}, {self.elem_id}, {self.param_len})'

__all__ = [
    'CGMBaseType',
    'CGMVariableType',
    'COMMAND',
]
