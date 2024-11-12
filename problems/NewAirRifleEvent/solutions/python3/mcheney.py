"""
Do we have a test where the convex hull doesn't contain the bullseye?
    Or where it does, but the margin of error allows the shot to be outside of the hull?

Does the contestant have to shoot the context hull in order, or can the points be provided randomly?

Add smaller second sample input
"""
import math


# From https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
def point_in_polygon(point, polygon):
    num_vertices = len(polygon)
    x, y = point[0], point[1]
    inside = False

    # Store the first point in the polygon and initialize the second point
    p1 = polygon[0]

    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = polygon[i % num_vertices]

        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p1[1], p2[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p1[1], p2[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p1[0], p2[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside

        # Store the current point as the first point for the next iteration
        p1 = p2

    # Return the value of the inside flag
    return inside


def is_point_on_line_segment(p, a, b):
    """
    Check if point p is on the line segment from a to b.
    """
    # Check if the cross product is zero (collinear)
    # and if p is within the bounding box of a and b
    cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    if cross != 0:
        return False
    # Check if p is within the bounding box of a and b
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def is_point_inside_convex_hull(hull, target):
    """
    Returns True if the target coordinate is inside or on the edge of the convex hull,
    given as a list of points in clockwise order.
    """
    n = len(hull)
    if n < 3:
        return False  # A valid convex hull has at least 3 points

    # Check if the target is on any edge of the hull
    for i in range(n):
        a = hull[i]
        b = hull[(i + 1) % n]
        if is_point_on_line_segment(target, a, b):
            return True

    # Check if the target is inside the hull using the winding number method
    # Since the hull is in clockwise order, all cross products should be non-positive
    for i in range(n):
        a = hull[i]
        b = hull[(i + 1) % n]
        cross = (b[0] - a[0]) * (target[1] - a[1]) - (b[1] - a[1]) * (target[0] - a[0])
        if cross > 0:
            return False  # The point is outside

    return True

def cross_product(o, a, b):
    """
    Return the cross product of vector OA and OB.
    A positive cross product indicates a counter-clockwise turn,
    negative indicates clockwise, and zero indicates collinear points.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """
    Returns the points forming the convex hull in clockwise order,
    starting from the leftmost point, if all points are on the hull.
    Otherwise, returns an empty list.
    """
    # Sort the points lexicographically (by x, then by y)
    points = sorted(points)

    # Build the lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull to get the full hull
    # Remove the last point of each half because it's repeated
    full_hull = lower[:-1] + upper[:-1]

    # Check if all points are on the hull
    if len(full_hull) != len(set(points)):
        return []

    # Return the points in clockwise order
    # Since monotone chain returns counterclockwise, reverse the result
    return full_hull[::-1]

def are_three_points_collinear(a, b, c):
    """
    Check if three points a, b, and c are collinear.
    Returns True if they are collinear, otherwise False.
    """
    # Compute the cross product of vectors AB and BC
    # If the cross product is zero, the points are collinear
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0

def is_polygon_valid(polygon):
    """
    Check if a polygon is valid (no three consecutive points form a line).
    Returns False if any three consecutive points are collinear, otherwise True.
    """
    n = len(polygon)
    if n < 3:
        return False  # A valid polygon must have at least 3 points

    # Check every triplet of consecutive points
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        c = polygon[(i + 2) % n]
        if are_three_points_collinear(a, b, c):
            return False

    return True

A, N, M = [int(ea) for ea in input().split(' ')]

if A > 1000:
    print("A is too big", A)
if N > 1000:
    print("N is too big", N)
if M > 10:
    print("M is too big", M)

for a in range(A):
    line = input().split(' ')
    name = line[0]
    coords = []
    for rawCoord in line[1:-1]:
        split = rawCoord.split(',')
        coord = (int(split[0]), int(split[1]))
        if coord[0] >= 1000000 or coord[1] >= 1000000:
            print('bad value!')
        coords.append(coord)
    if len(coords) != N-1:
        print('wrong number of shots!')
    if len(set(coords)) != len(coords):
        # Shots overlapped
        continue
    hull = convex_hull(coords)
    if len(hull) == 0:
        continue

    # Are any points on the border of the hull?
    if not is_polygon_valid(hull):
        continue
    # Does the hull contain the bullseye?
    # if not point_in_polygon((0,0), hull):
    #     continue

    split = line[-1].split(',')
    bullseyeCoord = (int(split[0]), int(split[1]))

    # Does the hull contain the final shot?
    if not is_point_inside_convex_hull(hull, bullseyeCoord):
        continue

    # Is final shot close enough to bullseye?
    if math.sqrt((bullseyeCoord[0]**2 + bullseyeCoord[1]**2)) > M:
        continue

    print(name)
