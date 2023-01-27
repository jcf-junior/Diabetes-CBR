from math import sqrt
from Metrics.distance_metrics import *
from variable_assignment import *

# find k nearest neighbors
nearest_neighbors = find_nearest_neighbors(new_case, k, selected_distance_metric)

print(nearest_neighbors)