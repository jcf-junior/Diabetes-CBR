from math import sqrt
import pymongo

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cbr"]
inputs_collection = db["inputs"]
new_case_collection = db["new_case"]

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

# Insert the new case into the database
new_case_collection.insert_one({"type" : "new_case", "data" : {"Preprandial BG": preprandial_bg,"IOB": iob,"BG Target": bg_target,"CHO": cho,"Patient weight": patient_weight,"ICR": icr,"ISF": isf,"Physical activity preprandial - Duration": physical_activity_preprandial_duration,"Physical activity preprandial - Heart rate": physical_activity_preprandial_heart_rate,"Physical activity preprandial - Intensity": physical_activity_preprandial_intensity,"Physical activity postprandial - Duration": physical_activity_postprandial_duration,"Physical activity postprandial - Intensity": physical_activity_postprandial_intensity,"Time of day": time_in_minutes}})
