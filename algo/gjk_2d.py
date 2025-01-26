import numpy as np

def support(shape1, shape2, direction):
    """
    Finds the support point of the Minkowski Difference of two shapes in the given direction.
    """
    # Ensure direction is a numpy array
    direction = np.array([direction[0], direction[1]])

    # Find the farthest point in the given direction for shape1
    farthest_point_shape1 = max(shape1, key=lambda point: np.dot(point, direction))

    # Find the farthest point in the opposite direction for shape2
    farthest_point_shape2 = max(shape2, key=lambda point: np.dot(point, -direction))

    # Compute the support point in the Minkowski Difference
    support_point = farthest_point_shape1 - farthest_point_shape2

    # Return a 3d vector because numpy doesn't support cross product between 2d vectors.
    return np.array([support_point[0], support_point[1], 0])

def gjk(shape1, shape2):
    """
    Implements the GJK algorithm to determine if two convex shapes intersect.
    """
    # Initial direction can be any vector.
    direction = np.array([1, 0])

    # Get the initial support point
    simplex = [support(shape1, shape2, direction)]

    # Reverse the direction towards the origin, origin in this case is (0, 0)
    direction = -simplex[0]

    while True:
        # Add a new point to the simplex in the current direction
        new_point = support(shape1, shape2, direction)

        # If the new point is not past the origin in the direction, no collision
        if np.dot(new_point, direction) < 0:
            return False

        # Add the new point to the simplex
        simplex.append(new_point)

        # Check if the simplex contains the origin
        if handle_simplex(simplex, direction):
            return True

def handle_simplex(simplex, direction):
    """
    Updates the simplex and direction for the GJK algorithm.
    """
    if len(simplex) == 2:
        # Line case
        return handle_line(simplex, direction)
    elif len(simplex) == 3:
        # Triangle case
        return handle_triangle(simplex, direction)
    return False

def handle_line(simplex, direction):
    """
    Handles the line case for the simplex.
    """
    B, A = simplex
    AB = B - A
    AO = -A

    # Must convert the 2d vector into 3d
    AB = np.array([AB[0], AB[1], 0])
    AO = np.array([AO[0], AO[1], 0])

    # New direction is perpendicular to AO towards the origin
    direction[:] = np.cross(np.cross(AB, AO), AB)

    # Line cannot contains the origin point. It can touch it.
    return False

def handle_triangle(simplex, direction):
    """
    Handles the triangle case for the simplex.
    """
    C, B, A = simplex
    AB = B - A
    AC = C - A

    # Must convert 2d vector into 3d
    AO = np.array([-A[0], -A[1], 0])
    AB = np.array([AB[0], AB[1], 0])
    AC = np.array([AC[0], AC[1], 0])

    # Perpendicular to AB and AC
    AB_perp = np.cross(np.cross(AC, AB), AB)
    AC_perp = np.cross(np.cross(AB, AC), AC)

    if np.dot(AB_perp, AO) > 0:
        simplex.pop(0)  # Remove C
        direction[:] = AB_perp[:]
        return False
    elif np.dot(AC_perp, AO) > 0:
        simplex.pop(1)  # Remove B
        direction[:] = AC_perp[:]
        return False
    
    return True