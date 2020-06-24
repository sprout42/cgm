import enum

class COLOR_MODEL(enum.IntEnum):
    RGB = 1
    CIELAB = 2
    CIELUV = 3
    CMYK = 4
    RGB_related = 5

# Because the CGM standard can't spell (yes I know it's a valid alternate 
# spelling depending on what country you are in)
COLOUR_MODEL = COLOR_MODEL


class COLOR_SELECTION_MODE(enum.IntEnum):
    INDEXED = 0
    DIRECT = 1

# Because the CGM standard can't spell (yes I know it's a valid alternate 
# spelling depending on what country you are in)
COLOUR_SELECTION_MODE = COLOR_SELECTION_MODE
