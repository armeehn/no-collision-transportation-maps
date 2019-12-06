"""
    Some useful functions for k-d tree building.
"""

import numpy as np

def pns(n, points, is_vertical):
    """(p)roject a(n)d (s)plit.

    Projects the points onto a lower dimensional space in order to create the
    half spaces. Creates the partitioning of the set into two subsets of equal
    size with respect to which half space elements of the set are in and
    returns the two subsets.

    Args:
        n: Number of points. Assumed to be a power of 2.
        points: NumPy array of points with shape (n, 2) that are being
            projected onto a lower dimensional space and split according to the
            median.
        is_vertical: Boolean to decide if the points are to be split
            vertically if True and horizontally otherwise.

    Returns:
        Two NumPy arrays that represent the lower and greater half spaces of
            the set of points that was supplied as an argument.
    """

    # Note: Zeroth column is reserved for the IDs of the points

    if is_vertical:
        # Project to y axis
        projected = points[:, 1]
    else:
        # Project to x axis
        projected = points[:, 2]

    k = np.median(projected)

    # Get the initial half spaces
    lower = points[projected < k]
    greater = points[projected > k]
    equal = points[projected == k]

    # Check if the splitting is not perfect
    if len(equal) > 0:

        half = n >> 1
        to_fill = half - len(lower)

        if to_fill > 0:
            lower = lower.append(equal[:to_fill])

        if half - len(greater) > 0:
            # Fill with the remainder, if necessary
            greater = greater.append(equal[to_fill:])

    return lower, greater

def build(n, registry, points, is_vertical):
    """Builds the registry.

    Recursively builds the registry on subsets of points.

    Args:
        n: Number of points. Assumed to be a power of 2.
            registry: NumPy array that holds the mapping identifiers of each
            point.
        points: NumPy array of points with shape (n, 2) that are to be
            projected onto a lower dimensional space and split according to the
            median.
        is_vertical: Boolean to decides if the points are to be split
            vertically if True and horizontally otherwise.

    Returns:
        Updated registry.

    Raises:
        ValueError: Points should not have zero length.

        We must stop the recursion at the base case: a singleton.
    """

    # Error case
    if n == 0:
        raise ValueError('Points should not have zero length.')

    # Base case
    if n == 1:
        return registry

    # Find the half spaces
    l, g = pns(n, points, is_vertical)

    # Update registry
    registry = update(update(registry, l, 0), g, 1)

    # Recursive step
    registry = build(n >> 1, registry, l, not is_vertical)
    return build(n >> 1, registry, g, not is_vertical)

def update(registry, points, side):
    """Updates the registry using the points provided.

    Args:
        registry: NumPy array that holds the mapping identifiers of each point.
        points: NumPy array of points with shape (k, 2) that will have their
            registry value updated depending on where they land in the half
            space. This is determined by the argument `side`.
        side: Boolean Integer that determines if the point was on the lower
            half or greater half of the space, based on the median. Lower and
            greater are given a side of 0 and 1 respectively.

    Returns:
        Updated registry on supplied sets of points. Registry values of points
        in original set that are not in `points` argument remain unchanged.
    """

    id = points[:, 0].astype(np.int32)
    registry[id, 1] = 2 * registry[id, 1] + side

    return registry
