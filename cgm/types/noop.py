from .base import CGMBaseType


class _NOOP(CGMBaseType):
    def __init__(self, fp, config, param_len):
        self.param_len = param_len
        super().__init__(fp, config)

    def extract(self):
        # Consume the required number of bytes
        self.raw = self.fp.read(self.param_len)
        self.value = None

    def __str__(self):
        return f'{self.__class__.__name__}({self.raw.hex()})'

__all__ = [
    '_NOOP',
]
