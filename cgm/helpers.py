
def ispoint(thing):
    # Is a point if thing is only a 2-tuple of numbers
    return isinstance(thing, tuple) \
            and len(thing) == 2 \
            and all(isinstance(t, int) for t in thing)

def isarea(thing):
    # Is a point if thing is at least a 3-tuple of numbers
    # Is a point if thing is only a 2-tuple of points
    return isinstance(thing, tuple) \
            and len(thing) >= 3 \
            and all(ispoint(t) for t in thing)


def findleft(thing):
    """
    Returns the leftmost coordinate value with 0, 0 at the upper left of the grid.
    The leftmost coordinate is the smallest X value.
    """
    if ispoint(thing):
        return thing[0]
    elif isarea(thing):
        return min(t[0] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def findright(thing):
    """
    Returns the rightmost coordinate value with 0, 0 at the upper left of the grid.
    The rightmost coordinate is the largest X value.
    """
    if ispoint(thing):
        return thing[0]
    elif isarea(thing):
        return max(t[0] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def findtop(thing):
    """
    Returns the upper coordinate value with 0, 0 at the upper left of the grid.
    The upper coordinate is the smallest Y value.
    """
    if ispoint(thing):
        return thing[1]
    elif isarea(thing):
        return min(t[1] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def findbottom(thing):
    """
    Returns the lowest coordinate value with 0, 0 at the upper left of the grid.
    The lowest coordinate is the largest Y value.
    """
    if ispoint(thing):
        return thing[1]
    elif isarea(thing):
        return max(t[1] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def findcenter(thing):
    """
    Returns the center of the thing as a point.
    """
    if ispoint(thing):
        # The center of a point is easy
        return thing
    elif isarea(thing):
        left = findleft(thing)
        right = findright(thing)
        x = (right - left) / 2

        top = findtop(thing)
        bottom = findbottom(thing)
        y = (bottom - top) / 2
        return (x, y)
    else:
        raise TypeError('must provide a point or an area')


def isinside(area, thing):
    if not isarea(area):
        raise TypeError('first argument must be an area')
    if not ispoint(thing) and not isarea(thing):
        raise TypeError('second argument must be a point or an area')

    return findleft(area) < findleft(thing) \
            and findright(area) > findright(thing) \
            and findtop(area) < findtop(thing) \
            and findbottom(area) > findbottom(thing)


def isleft(one, two):
    """
    Indicates if one is left of two
    """
    return findleft(one) < findleft(two)


def isright(one, two):
    """
    Indicates if one is right of two
    """
    return findright(one) > findright(two)


def isabove(one, two):
    """
    Indicates if one is above two
    """
    return findtop(one) < findtop(two)


def isbelow(one, two):
    """
    Indicates if one is below two
    """
    return findtop(one) > findtop(two)


def isalignedvert(thing_one, thing_two, margin=1):
    """
    Indicates if the two points are vertically aligned within a margin of error.
    """
    thing_one_center = findcenter(thing_one)
    thing_two_center = findcenter(thing_two)

    # To check for vertical alignment see if the X coordinates are within the 
    # margin of error.
    if isleft(thing_one_center, thing_two_center):
        # thing_one_center[0] is lower than thing_two_center
        return (thing_one_center[0] + 10) >= thing_two_center[0]
    else:
        # thing_one is right, or exactly the same as thing_two
        return (thing_one_center[0] - 10) <= thing_two_center[0]


def isalignedhoriz(thing_one, thing_two, margin=1):
    """
    Indicates if the two points are horizontally aligned within a margin of error.
    """
    thing_one_center = findcenter(thing_one)
    thing_two_center = findcenter(thing_two)

    # To check for horizontal alignment see if the Y coordinates are within the 
    # margin of error.
    if isabove(thing_one_center, thing_two_center):
        # thing_one_center[1] is lower than thing_two_center
        return (thing_one_center[1] + 10) >= thing_two_center[1]
    else:
        # thing_one is below, or exactly the same as thing_two
        return (thing_one_center[1] - 10) <= thing_two_center[1]
