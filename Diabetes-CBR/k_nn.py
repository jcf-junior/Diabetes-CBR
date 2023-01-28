import pymongo
from math import sqrt
# from Metrics.distance_metrics import *
from db_connection import *

# get k from config
p1=config["parameters"]["p1"]
k=p1

# Find k neighbors
def find_nearest_neighbors(new_case, k, selected_distance_metric):
    distances = []
    for case in cases:
        distance = selected_distance_metric(new_case, case["data"])
        distances.append((case["data"], distance))
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:k]]

nearest_neighbors = find_nearest_neighbors(new_case["data"], k, selected_distance_metric)