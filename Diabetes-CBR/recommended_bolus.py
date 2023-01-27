import pymongo
from new_case import *
from k_nn import *
from db_connection import *

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

# determine recommended insulin bolus
recommended_insulin_bolus = 0
for neighbor in nearest_neighbors:
    recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
recommended_insulin_bolus /= k

# print recommended insulin bolus
print("Recommended Insulin Bolus: {} U".format(round(recommended_insulin_bolus, 2)))