from math import sqrt
from Metrics.distance_metrics import *
import pymongo

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cbr"]
cases_collection = db["cases"]
config_collection = db["config"]
inputs_collection = db["inputs"]

# def run():
################## Cases ##################
# read cases from database
config = config_collection.find_one({"type": "config"})
cases = list(cases_collection.find({"type": "cases"}))

for case in cases:
    case = case["data"].copy()
    case["Time of day"] = 0

################## Metrics ##################
# Read selected distance metric from database
config = config_collection.find_one({"type": "config"})
try:
    selected_distance_metric = config["data"]["selected_distance_metric"]
except TypeError:
    print("The variable config is None and therefore it is not subscriptable. \nThis means that the find_one method from the config_collection is not finding any document that matches the query {""type"": ""config""}.\nExiting...")
    exit()

# Error handler for KeyError
try:
    selected_distance_metric = globals()[selected_distance_metric]
except KeyError:
    print("Invalid distance metric selected.\nExiting...")
    exit()

# get k from config
k =int(config["data"]["k"])

# Find k neighbors
def find_nearest_neighbors(new_case, k, selected_distance_metric):
    distances = []
    for case in cases:
        distance = selected_distance_metric(new_case, case["data"])
        distances.append((case["data"], distance))
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:k]]

# read inputs from database
inputs = inputs_collection.find_one({"type": "inputs"})
if inputs is None:
    print("No inputs found in the database.")
    exit()

# Assign inputs to variables
preprandial_bg = inputs["data"]["Preprandial BG"]
iob = inputs["data"]["IOB"]
bg_target = inputs["data"]["BG Target"]
cho = inputs["data"]["CHO"]
patient_weight = inputs["data"]["Patient weight"]
icr = inputs["data"]["ICR"]
isf = inputs["data"]["ISF"]
physical_activity_preprandial_duration = inputs["data"]["Physical activity preprandial - Duration"]
physical_activity_preprandial_heart_rate = inputs["data"]["Physical activity preprandial - Heart rate"]
physical_activity_preprandial_intensity = inputs["data"]["Physical activity preprandial - Intensity"]
physical_activity_postprandial_duration = inputs["data"]["Physical activity postprandial - Duration"]
physical_activity_postprandial_intensity = inputs["data"]["Physical activity postprandial - Intensity"]
time_of_day = inputs["data"]["Time of day"]

# Set the inputs from file
new_case = {}
new_case["Preprandial BG"] = preprandial_bg
new_case["IOB"] = iob
new_case["BG Target"] = bg_target
new_case["CHO"] = cho
new_case["Patient weight"] = patient_weight
new_case["ICR"] = icr
new_case["ISF"] = isf
new_case["Physical activity preprandial - Duration"] = physical_activity_preprandial_duration
new_case["Physical activity preprandial - Heart rate"] = physical_activity_preprandial_heart_rate
new_case["Physical activity preprandial - Intensity"] = physical_activity_preprandial_intensity
new_case["Physical activity postprandial - Duration"] = physical_activity_postprandial_duration
new_case["Physical activity postprandial - Intensity"] = physical_activity_postprandial_intensity
# Split time of day into hour and minute
hour, minute = time_of_day.split(':')
hour = int(hour)
minute = int(minute)
# Convert time of day to minutes
time_in_minutes = hour * 60 + minute
# Assign time of day to new_case
new_case["Time of day"] = time_in_minutes

# find k nearest neighbors
nearest_neighbors = find_nearest_neighbors(new_case, k, selected_distance_metric)

# determine recommended insulin bolus
recommended_insulin_bolus = 0
for neighbor in nearest_neighbors:
    recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
recommended_insulin_bolus /= k

# print recommended insulin bolus
print("Recommended Insulin Bolus: {} U".format(round(recommended_insulin_bolus, 2)))