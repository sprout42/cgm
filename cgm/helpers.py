
import math
from shapely.geometry import Polygon, Point, LineString, GeometryCollection
from shapely.ops import polygonize_full, snap

import matplotlib.pyplot as plt

def is_point(thing):
    # Is a point if thing is only a 2-tuple of numbers
    return isinstance(thing, tuple) \
            and len(thing) == 2 \
            and all(isinstance(t, (int, float, complex)) for t in thing)


def is_area(thing):
    # Is an area if thing is at least a 3-tuple of numbers
    return isinstance(thing, tuple) \
            and len(thing) >= 3 \
            and all(is_point(t) for t in thing)


def is_polygon(thing):
    return isinstance(thing, Polygon)


def make_polygon(things, tolerance=None):
    """
    Constructs a rough-estimate polygon from a list of CGM elements such as
    POLYLINE.

    This is a rough estimate because CIRCULAR_ARC_POINT elements are not
    modeled exactly but instead the start and end points of the arc are used
    to create a straight line.
    """
    if is_area(things):
        return Polygon(things)
    else:
        # Assume this is multiple elements parsed from a CGM file
        lines = []
        for cmd, data in things:
            if cmd == 'POLYLINE':
                lines.append(LineString(data))
            elif cmd == 'CIRCULAR_ARC_POINT':
                lines.append(LineString(data[0], data[2]))

        collection = GeometryCollection(lines)

        # If tolerance is provided create a grid of vertices to snap the lines 
        # into
        if tolerance:
            min_x, min_y, max_x, max_y = collection.bounds

            # round the min values down and max values up
            min_x = int(min_x - (min_x % tolerance))
            min_y = int(min_y - (min_y % tolerance))
            max_x = int(max_x + (tolerance - (max_x % tolerance)))
            max_y = int(max_y + (tolerance - (max_y % tolerance)))

            x_range = range(min_x, max_x + 1, tolerance)
            y_range = range(min_y, max_y + 1, tolerance)
            grid_coords = [(i, j) for j in x_range for i in y_range]
            snap_grid = Polygon(grid_coords)

            snapped_collection = snap(collection, snap_grid, tolerance)
            stuff = polygonize_full(snapped_collection)
        else:
            stuff = polygonize_full(collection)

        polygons = []
        for collection in stuff:
            print(collection)
            if collection and isinstance(collection[0], Polygon):
                for poly in collection:
                    plt.plot(*poly.exterior.xy)
                    polygons.append(poly)
            elif collection and tolerance is not None:
                #new_poly = _normalize_lines(collection, tolerance)
                #plt.plot(*new_poly.exterior.xy)
                #polygons.append(new_poly)
                for line in collection:
                    x_list.extend(line.xy[0])
                    y_list.extend(line.xy[1])

        plt.show()
        return polygons


def find_left(thing):
    """
    Returns the leftmost coordinate value with 0,0 at the lower left of the grid.
    The leftmost coordinate is the smallest X value.
    """
    if is_point(thing):
        return thing[0]
    elif is_area(thing):
        return min(x for x, _ in thing)
    elif is_polygon(thing):
        return min(x for x, _ in thing.coords)
    else:
        raise TypeError('must provide a point or an area')


def find_right(thing):
    """
    Returns the rightmost coordinate value with 0,0 at the lower left of the grid.
    The rightmost coordinate is the largest X value.
    """
    if is_point(thing):
        return thing[0]
    elif is_area(thing):
        return max(x for x, _ in thing)
    elif is_polygon(thing):
        return max(x for x, _ in thing.coords)
    else:
        raise TypeError('must provide a point or an area')


def find_top(thing):
    """
    Returns the upper coordinate value with 0,0 at the lower left of the grid.
    The upper coordinate is the largest Y value.
    """
    if is_point(thing):
        return thing[1]
    elif is_area(thing):
        return max(y for _, y in thing)
    elif is_polygon(thing):
        return max(y for _, y in thing.coords)
    else:
        raise TypeError('must provide a point or an area')


def find_bottom(thing):
    """
    Returns the lowest coordinate value with 0,0 at the lower left of the grid.
    The lowest coordinate is the smallest Y value.
    """
    if is_point(thing):
        return thing[1]
    elif is_area(thing):
        return min(y for _, y in thing)
    elif is_polygon(thing):
        return min(y for _, y in thing.coords)
    else:
        raise TypeError('must provide a point or an area')


def find_center(thing):
    """
    Returns the center of the thing as a point with 0,0 at the lower left of the grid.
    """
    if is_point(thing):
        # The center of a point is easy
        return thing
    elif is_area(thing):
        # 0 is on the left
        left = find_left(thing)
        right = find_right(thing)
        x = left + ((right - left) / 2)

        # 0 is on the bottom
        bottom = find_bottom(thing)
        top = find_top(thing)
        y = bottom + ((top - bottom) / 2)
        return (x, y)
    elif is_polygon(thing):
        return thing.centroid.coords
    else:
        raise TypeError('must provide a point or an area')


def is_inside(area, thing):
    if not is_polygon(area):
        area = make_polygon(area)

    if is_point(thing):
        return area.contains(Point(thing))
    elif is_area(thing):
        return area.contains(Polygon(thing))
    else:
        # Otherwise just try and see what happens
        return area.contains(thing)

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
    if is_point(thing_one):
        thing_one = Point(thing_one)
    elif is_area(thing_one):
        thing_one = make_polygon(thing_one)

    if is_point(thing_two):
        thing_two = Point(thing_two)
    elif is_area(thing_two):
        thing_two = make_polygon(thing_two)

    return thing_one.distance(thing_two)


def find_closest(thing_one, thing_list):
    """
    Identifies which item in the thing_list is closest to the first parameter.
    """
    if is_point(thing_one):
        thing_one = Point(thing_one)
    elif is_area(thing_one):
        thing_one = make_polygon(thing_one)

    min_dist = math.inf
    closest = None
    for item in thing_list:
        dist = distance(thing_one, item)
        if dist < min_dist:
            min_dist = dist
            closest = item

    return closest
