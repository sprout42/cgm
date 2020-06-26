
import re
import functools
import inspect

from cgm.utils import word, assert_word_len

from .base import *
from .noop import *
from .string import *
from .integer import *
from .real import *
from .parsed_types import *
from .color import *
from .vdc import *
from .font import *
from .picture import *
from .app import *
from .sdr import *


# Gather all of the special '_TYPE' type classes into one place
base_types = dict((k, v) for k, v in globals().items()
        if k[0] == '_' and hasattr(v, '__mro__') and issubclass(v, CGMBaseType))


class CGMGenericType(CGMBaseType):
    def __init__(self, fp, config, types):
        self.types = types
        super().__init__(fp=fp, config=config)

    def extract(self):
        values = []
        for typ in self.types:
            values.append(typ(fp=self.fp, config=self.config))
        self.value = tuple(values)

        # This type is a top-level type so make sure the file is word aligned at 
        # the end
        self.fp.next()

    @classmethod
    def _make_type_list(cls, name, len_spec, param_len=None):
        # prefix the "type" with '_' and get the type
        typ_str = f'_{name}'
        typ = base_types[typ_str]

        # Some types ask for the length to be included as a param
        typ_argspec = inspect.getfullargspec(typ)
        send_param_len = 'param_len' in typ_argspec.args

        ## the len_spec may be a string, or may be a list of strings
        #if isinstance(len_spec, list):
        #    send_param_len = any('n' in s for s in len_spec)
        #else:
        #    send_param_len = 'n' in len_spec

        #if typ_str in param_len_override_types or send_param_len:
        if send_param_len:
            args = {'param_len': param_len}
            return [functools.partial(typ, **args)]
        else:
            return [typ]

    @classmethod
    def _fix_param_len(cls, num_mult, n_mult, elem_len):
        # if the same 'n' or '<num>n' prefix is in the type and len fields, 
        # remove it from the len fields because it is taken care of by the 
        # number of types created
        prefix = ''
        if num_mult:
            prefix += num_mult
        if n_mult:
            prefix += n_mult

        if prefix and elem_len.startswith(prefix):
            return elem_len[len(prefix):]
        else:
            return elem_len

    @classmethod
    def make(cls, fp, config, elem, param_len=None):
        print(elem)
        try:
            # If here is a type defined for this element use that instead of 
            # constructing one on the fly from the element table 'type' strings
            special_cls = cls._make_type_list(elem['element'], elem['len'], param_len)
        except KeyError:
            pass
        else:
            return special_cls[0](fp=fp, config=config)

        types = []
        if isinstance(elem['type'], str):
            typ_len_list = [(elem['type'], elem['len'])]
        else:
            typ_len_list = zip(elem['type'], elem['len'])

        for elem_typ, elem_len in typ_len_list:
            match = re.match(r'^(?:([0-9]+)|(n))*([^n].*)', elem_typ)
            print(match.groups())

            elem_len = cls._fix_param_len(match.group(1), match.group(2), elem_len)
            typ_list = cls._make_type_list(match.group(3), elem_len, param_len)

            # If the type is prefixed with a number, duplicate the type the 
            # appropriate number of times
            if match.group(1):
                typ_list = typ_list * int(match.group(1))

            # If it is prefixed with 'n' duplicate it 'param_len' number of 
            # times.
            if match.group(2):
                assert param_len
                typ_list = typ_list * param_len

            # Extend the full type list
            types.extend(typ_list)
        return cls(fp, config, types)

    def __str__(self):
        return str(self.value)


class CGMTopLevelType(CGMBaseType):
    def extract(self):
        # First read a command header to figure out what the next element is
        cmd = COMMAND(fp=self.fp, config=self.config, )

        if cmd.elem['type'] is None:
            self.value = cmd
        else:
            elem = CGMGenericType.make(self.fp, self.config, cmd.elem, cmd.param_len)
            self.value = (cmd, elem)

            # Ensure that the command length matches the size of the element 
            # just created, but only if the command is complete
            if cmd.complete:
                assert_word_len(cmd.param_len, elem.size)

            # Some commands change configuration values so check for those now
            if cmd.elem['element'] in self.config:
                self.config.set(cmd.elem['element'], elem)


class _METAFILE_DEFAULTS_REPLACEMENT(CGMTopLevelType):
    pass


class _METAFILE_ELEMENT_LIST(CGMBaseType):
    _pseudo_elements = {
        0: 'drawing set',
        1: 'drawing-plus-control set',
        2: 'version-2 set',
        3: 'extended-primitives set',
        4: 'version-2-gksm set',
        5: 'version-3 set',
        6: 'version-4 set',
    }

    def __init__(self, fp, config, param_len):
        self.param_len = param_len
        super().__init__(fp=fp, config=config)

    def extract(self):
        self.value = {
            'num': _I(fp=self.fp, config=self.config),
        }

        elements = []
        num = self.value['num'].unwrap()
        for i in range(num):
            elem_cls = _IX(fp=self.fp, config=self.config)
            elem_id = _IX(fp=self.fp, config=self.config)

            _cls = elem_cls.unwrap()
            _id = elem_id.unwrap()

            try:
                elem_str = cgm_class_codes[_cls][_id]['element']
            except KeyError:
                if _cls == -1:
                    elem_str = self._pseudo_elements[_id]
                else:
                    raise

            elem = {
                'class': elem_cls,
                'id': elem_id,
                'elem': elem_str,
            }
            elements.append(elem)

        self.value['elements'] = tuple(elements)


# Gather all of the special '_TYPE' type classes into one place
base_types = dict((k, v) for k, v in globals().items()
        if k[0] == '_' and hasattr(v, '__mro__') and issubclass(v, CGMBaseType))


__all__ = [
    'COMMAND',
    'CGMTopLevelType',
    'CGMGenericType',
    '_METAFILE_DEFAULTS_REPLACEMENT',
    '_METAFILE_ELEMENT_LIST',
]

