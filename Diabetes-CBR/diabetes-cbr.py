import json
from math import sqrt
from Metrics.distance_metrics import *

# read cases from JSON file
with open("cases.json", "r") as f:
    cases = json.load(f)
    for case in cases:
        # fix for KeyError: Time of day
        case["Time of day"] = 0

# Read selected distance metric from JSON file
with open("config.json", "r") as f:
    config = json.load(f)
    selected_distance_metric = config["selected_distance_metric"]
# Dictionary dependency fix    
    selected_distance_metric = globals()[selected_distance_metric]

def find_nearest_neighbors(new_case, k, distance_metric):
    distances = []
    for case in cases:
        distance = distance_metric(new_case, case)
        distances.append((case, distance))
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:k]]

# prompt user to enter inputs for new case
new_case = {}
new_case["Preprandial BG"] = int(input("Enter preprandial blood glucose level (mg/dL): "))
new_case["IOB"] = float(input("Enter current insulin on board (U): "))
new_case["BG Target"] = int(input("Enter target blood glucose level (100 or 110 mg/dL): "))
new_case["CHO"] = int(input("Enter carbohydrates amount (g): "))
new_case["Patient weight"] = int(input("Enter patient weight (kg): "))
new_case["ICR"] = int(input("Enter insulin to carb ratio: "))
new_case["ISF"] = int(input("Enter insulin sensitivity factor: "))
new_case["Physical activity preprandial - Duration"] = int(input("Enter duration of physical activity before meal (min): "))
new_case["Physical activity preprandial - Heart rate"] = int(input("Enter heart rate during physical activity before meal (bpm): "))
new_case["Physical activity preprandial - Intensity"] = int(input("Enter intensity of physical activity before meal (0-6): "))
new_case["Physical activity postprandial - Duration"] = int(input("Enter duration of physical activity after meal (min): "))
new_case["Physical activity postprandial - Intensity"] = int(input("Enter intensity of physical activity after meal (0-6): "))

# prompt user to enter time of day
time_of_day = input("Enter time of day (hh:mm): ")
hour, minute = time_of_day.split(':')
hour = int(hour)
minute = int(minute)
time_in_minutes = hour * 60 + minute
new_case["Time of day"] = time_in_minutes

# ask user for value of k
k = int(input("Enter value of k: "))

# find k nearest neighbors
nearest_neighbors = find_nearest_neighbors(new_case, k)

# determine recommended insulin bolus
recommended_insulin_bolus = 0
for neighbor in nearest_neighbors:
    recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
recommended_insulin_bolus /= k

# print recommended insulin bolus
print("Recommended Insulin Bolus: {} U".format(round(recommended_insulin_bolus, 2)))

