from db_connection import *
from recommended_bolus import *
from find_neighbors import *
from recommended_bolus import *

# set input parameters
nearest_neighbors = find_nearest_neighbors(new_case["data"], k, selected_distance_metric)