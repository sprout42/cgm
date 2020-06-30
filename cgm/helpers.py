
import math

def is_point(thing):
    # Is a point if thing is only a 2-tuple of numbers
    return isinstance(thing, tuple) \
            and len(thing) == 2 \
            and all(isinstance(t, int) for t in thing)

def is_area(thing):
    # Is a point if thing is at least a 3-tuple of numbers
    # Is a point if thing is only a 2-tuple of points
    return isinstance(thing, tuple) \
            and len(thing) >= 3 \
            and all(is_point(t) for t in thing)


def find_left(thing):
    """
    Returns the leftmost coordinate value with 0, 0 at the upper left of the grid.
    The leftmost coordinate is the smallest X value.
    """
    if is_point(thing):
        return thing[0]
    elif is_area(thing):
        return min(t[0] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def find_right(thing):
    """
    Returns the rightmost coordinate value with 0, 0 at the upper left of the grid.
    The rightmost coordinate is the largest X value.
    """
    if is_point(thing):
        return thing[0]
    elif is_area(thing):
        return max(t[0] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def find_top(thing):
    """
    Returns the upper coordinate value with 0, 0 at the upper left of the grid.
    The upper coordinate is the smallest Y value.
    """
    if is_point(thing):
        return thing[1]
    elif is_area(thing):
        return min(t[1] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def find_bottom(thing):
    """
    Returns the lowest coordinate value with 0, 0 at the upper left of the grid.
    The lowest coordinate is the largest Y value.
    """
    if is_point(thing):
        return thing[1]
    elif is_area(thing):
        return max(t[1] for t in thing)
    else:
        raise TypeError('must provide a point or an area')


def find_center(thing):
    """
    Returns the center of the thing as a point.
    """
    if is_point(thing):
        # The center of a point is easy
        return thing
    elif is_area(thing):
        left = find_left(thing)
        right = find_right(thing)
        x = (right - left) / 2

        top = find_top(thing)
        bottom = find_bottom(thing)
        y = (bottom - top) / 2
        return (x, y)
    else:
        raise TypeError('must provide a point or an area')


def is_inside(area, thing):
    if not is_area(area):
        raise TypeError('first argument must be an area')
    if not is_point(thing) and not is_area(thing):
        raise TypeError('second argument must be a point or an area')

    return find_left(area) < find_left(thing) \
            and find_right(area) > find_right(thing) \
            and find_top(area) < find_top(thing) \
            and find_bottom(area) > find_bottom(thing)


def is_left(one, two):
    """
    Indicates if one is left of two
    """
    return find_left(one) < find_left(two)


def is_right(one, two):
    """
    Indicates if one is right of two
    """
    return find_right(one) > find_right(two)


def is_above(one, two):
    """
    Indicates if one is above two
    """
    return find_top(one) < find_top(two)


def is_below(one, two):
    """
    Indicates if one is below two
    """
    return find_top(one) > find_top(two)


def is_aligned_vert(thing_one, thing_two, margin=1):
    """
    Indicates if the two points are vertically aligned within a margin of error.
    """
    thing_one_center = find_center(thing_one)
    thing_two_center = find_center(thing_two)

    # To check for vertical alignment see if the X coordinates are within the 
    # margin of error.
    if is_left(thing_one_center, thing_two_center):
        # thing_one_center[0] is lower than thing_two_center
        return (thing_one_center[0] + 10) >= thing_two_center[0]
    else:
        # thing_one is right, or exactly the same as thing_two
        return (thing_one_center[0] - 10) <= thing_two_center[0]


def is_aligned_horiz(thing_one, thing_two, margin=1):
    """
    Indicates if the two points are horizontally aligned within a margin of error.
    """
    thing_one_center = find_center(thing_one)
    thing_two_center = find_center(thing_two)

    # To check for horizontal alignment see if the Y coordinates are within the 
    # margin of error.
    if is_above(thing_one_center, thing_two_center):
        # thing_one_center[1] is lower than thing_two_center
        return (thing_one_center[1] + 10) >= thing_two_center[1]
    else:
        # thing_one is below, or exactly the same as thing_two
        return (thing_one_center[1] - 10) <= thing_two_center[1]


def distance(thing_one, thing_two):
    """
    Returns the distance between the centers of two things.
    """
    thing_one_center = find_center(thing_one)
    thing_two_center = find_center(thing_two)

    # We could do this calculation ourselves but why bother when python does it 
    # for us
    return math.dist(thing_one_center, thing_two_center)


def find_closest_center(thing_one, thing_list):
    """
    Identifies which item in the thing_list is closest to the first parameter.

    This uses the center of an item to represent the nearness to the first
    thing, which means that strange shapes can easily confuse this function.
    It's just a helper not an advanced algorithm.
    """
    thing_center = find_center(thing_one)

    min_dist = math.inf
    for item in thing_list:
        dist = distance(thing_center, item)
        if dist < min_dist:
            min_dist = dist

    return min_dist
