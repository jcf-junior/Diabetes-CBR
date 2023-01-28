import pymongo
from Metrics.distance_metrics import *

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cbr"]
cases_collection = db["cases"]
config_collection = db["config"]
new_case_collection = db["new_case"]

# read cases from database
config = config_collection.find_one({"type": "config"})
cases = list(cases_collection.find({"type": "cases"}))
for case in cases:
    case = case["data"].copy()
    case["Time of day"] = 0

# read new_case from database
new_case = new_case_collection.find_one({"type": "new_case"})

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