import json
from math import sqrt
from Metrics.distance_metrics import *
import Metrics.distance_metrics as dm


def run():
    ################## Cases ##################
    # read cases from JSON file
    with open("cases.json", "r") as f:
        cases = json.load(f)
        for case in cases:
            # fix for KeyError: Time of day
            case["Time of day"] = 0

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

    # read inputs from JSON file
    with open("inputs.json", "r") as f:
        inputs = json.load(f)

    # get k from config.json
    with open("config.json", "r") as f:
        config = json.load(f)
        k = int(config["k"])

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

    # # ask user for value of k
    # k = int(input("Enter value of k: "))

    # find k nearest neighbors
    nearest_neighbors = find_nearest_neighbors(
        new_case, k, selected_distance_metric)

    # fix for AttributeError

    # determine recommended insulin bolus
    recommended_insulin_bolus = 0
    for neighbor in nearest_neighbors:
        recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
    recommended_insulin_bolus /= k

    # print recommended insulin bolus
    print("Recommended Insulin Bolus: {} U".format(
        round(recommended_insulin_bolus, 2)))
