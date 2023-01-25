import json
from math import sqrt
from Metrics.distance_metrics import *
import k_nearest_neighbors
import Metrics.distance_metrics as dm
import importlib

################## Cases ##################
# read cases from JSON file
with open("cases.json", "r") as f:
    cases = json.load(f)
    for case in cases:
        # fix for KeyError: Time of day
        case["Time of day"] = 0
############################################

################## Metrics ##################
# Read selected distance metric from JSON file
with open("config.json", "r") as f:
    config = json.load(f)
    selected_distance_metric = config["selected_distance_metric"]
# Error handler for KeyError
try:
    selected_distance_metric = globals()[selected_distance_metric]
except KeyError:
    print("Invalid distance metric selected.\nExiting...")
    exit()
############################################

################## Inputs ##################
# read inputs from JSON file
with open("inputs.json", "r") as f:
    inputs = json.load(f)
############################################

################## Algorithms ##################
    # read the config.json file
with open("config.json", "r") as f:
    config = json.load(f)
    selected_algorithm = config["selected_algorithm"]

algorithm_module = importlib.import_module(selected_algorithm)
algorithm_module.run_algorithm()

# call the function for the selected algorithm
output = algo.run_algorithm(input_data)

# process and print the output
print(output)
############################################

# Find k neighbors
def find_nearest_neighbors(new_case, k, selected_distance_metric):
    distances = []
    for case in cases:
        distance = selected_distance_metric(new_case, case)
        distances.append((case, distance))
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:k]]

# Assign inputs to variables
preprandial_bg = inputs["Preprandial BG"]
iob = inputs["IOB"]
bg_target = inputs["BG Target"]
cho = inputs["CHO"]
patient_weight = inputs["Patient weight"]
icr = inputs["ICR"]
isf = inputs["ISF"]
physical_activity_preprandial_duration = inputs["Physical activity preprandial - Duration"]
physical_activity_preprandial_heart_rate = inputs["Physical activity preprandial - Heart rate"]
physical_activity_preprandial_intensity = inputs["Physical activity preprandial - Intensity"]
physical_activity_postprandial_duration = inputs["Physical activity postprandial - Duration"]
physical_activity_postprandial_intensity = inputs["Physical activity postprandial - Intensity"]
time_of_day = inputs["Time of day"]

# Set the inputs from file
new_case = {}
new_case["Preprandial BG"] = inputs["Preprandial BG"]
new_case["IOB"] = inputs["IOB"]
new_case["BG Target"] = inputs["BG Target"]
new_case["CHO"] = inputs["CHO"]
new_case["Patient weight"] = inputs["Patient weight"]
new_case["ICR"] = inputs["ICR"]
new_case["ISF"] = inputs["ISF"]
new_case["Physical activity preprandial - Duration"] = inputs["Physical activity preprandial - Duration"]
new_case["Physical activity preprandial - Heart rate"] = inputs["Physical activity preprandial - Heart rate"]
# Split time of day into hour and minute
hour, minute = time_of_day.split(':')
hour = int(hour)
minute = int(minute)
# Convert time of day to minutes
time_in_minutes = hour * 60 + minute
# Assign time of day to new_case
new_case["Time of day"] = time_in_minutes

