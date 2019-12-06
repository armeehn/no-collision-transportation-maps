"""
    (H)orizontal(V)ertical cut algorithm for building a k-d tree.
"""

import numpy as np
from useful import build

def hvcut(start, end, n, first_cut = 'v'):
    """Creates an approximate optimal transportation map.

    Creates a complete k-d tree on 2 ** n points for some natural number n.
    Start and end points are then paired together based on their location
    within the tree. This is determined by their path from the root.

    Args:
        start: NumPy array of shape (2 ** n, 2) that represents the starting
            location of the points.
        end: NumPy array of shape (2 ** n, 2) that represents the ending
            location of the points.
        n: Integer that represents the dimensionality of the problem. There are
            2 ** n points.
        first_cut: Choice between `v` and `h`. `v` dictates that we start with
            a vertical cut, and `h` is a horizontal cut.

    Returns:
        NumPy array of shape (2 ** n, 2) which represents the discrete mapping
        as a pairing between start and end points.
    """


    is_vertical = first_cut == 'v'

    # Start
    rs = np.zeros((2**n, 2), dtype = np.int32)
    rs[:, 0] = np.arange(2**n)
    rs = build(2**n, rs, start, is_vertical = is_vertical)

    # End
    re = np.zeros((2**n, 2), dtype = np.int32)
    re[:, 0] = np.arange(2**n)
    re = build(2**n, re, end, is_vertical = is_vertical)

    # Swap the columns so that we can match the identifiers together
    rs[:, [0, 1]] = rs[:, [1, 0]]
    re[:, [0, 1]] = re[:, [1, 0]]

    # Sort based on the identifiers, so that we can fetch them easily
    re = re[re[:, 0].argsort()]

    # Matched identifiers
    rng = np.arange(2**n)
    return np.stack((rs[rng, 1], re[rs[rng, 0], 1]), axis=-1)
