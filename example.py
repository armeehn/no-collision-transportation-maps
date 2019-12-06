"""
    Example of how to use the code.
"""

from hvcut import hvcut
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# For comparison purposes
import ot

# Exponential dimension of the problem
n = 6

# Start (source) Initialization
start = np.zeros((2 ** n, 3))

# Identifiers for the points
start[:, 0] = np.arange(2 ** n)
start[:, 1:] = np.random.randn(2 ** n, 2)

# End (target) Initialization
end = np.zeros((2 ** n, 3))

# Identifiers for the points
end[:, 0] = np.arange(2 ** n)
end[:, 1:] = np.random.randn(2 ** n, 2)

# Perform the pairing of points
pairing = hvcut(start, end, n = n)

# Comparison of results

C = cdist(start[:,1:], end[:,1:], metric='sqeuclidean')

# OT using linear programming
a, b = np.ones((2 ** n,)) / 2 ** n, np.ones((2 ** n,)) / 2 ** n
plan = ot.lp.emd(a, b, C)

r = np.arange(2 ** n)

hv_cost = C[pairing[:, 0], pairing[:, 1]].sum()

# Element-wise multiplication against cost matrix as EMD might not be a map
otlp_cost = ((2 ** n) * plan * C).sum()

rel_err = 100 * abs(hv_cost - otlp_cost) / otlp_cost
ratio = hv_cost / otlp_cost

print(  'OTLP: %.4f\n'
        'HV: %.4f\n\n'
        'Relative Error: %.4f%%\n'
        'Ratio: %.4f' % (otlp_cost, hv_cost, rel_err, ratio))
