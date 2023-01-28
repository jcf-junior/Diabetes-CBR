from recommended_bolus import *

def run():
    # find k nearest neighbors
    nearest_neighbors = find_nearest_neighbors(new_case["data"], k, selected_distance_metric)