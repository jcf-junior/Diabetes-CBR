from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Get the database
db = client["cbr"]

# Check if the cases collection exists
if "cases" not in db.list_collection_names():
    # Create a new collection for cases
    cases_collection = db.create_collection("cases")
    print("Cases collection created successfully.")
else:
    cases_collection = db["cases"]
    print("Cases collection already exists.")

# Check if the config collection exists
if "config" not in db.list_collection_names():
    # Create a new collection for config
    config_collection = db.create_collection("config")
    print("Config collection created successfully.")
else:
    config_collection = db['config']
    print("Config collection already exists.")

# Check if the inputs collection exists
if "inputs" not in db.list_collection_names():
    # Create a new collection for inputs
    inputs_collection = db.create_collection("inputs")
    print("Inputs collection created successfully.")
else:
    inputs_collection = db['inputs']
    print("Inputs collection already exists.")

# Insert the config
config_collection.insert_one({"type" : "config", "data" : {"selected_algorithm": "k_nearest_neighbors","selected_distance_metric": "euclidean_distance","k": 3}, "parametros" : {"Parametros": "", "Parametros2": ""}})
# config_collection.insert_one({"type" : "parameters", "parameters" : {"p1": " ", "p2": " "}})
inputs_collection.insert_one({"type" : "inputs", "data" : {"Preprandial BG": 150,"IOB": 2.5,"BG Target": 110,"CHO": 35,"Patient weight": 75,"ICR": 10,"ISF": 40,"Physical activity preprandial - Duration": 20,"Physical activity preprandial - Heart rate": 80,"Physical activity preprandial - Intensity": 4,"Physical activity postprandial - Duration": 10,"Physical activity postprandial - Intensity": 2,"Time of day": "12:30"}})