from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Get the database
db = client['cbr']

# Check if the cases collection exists
if "cases" not in db.list_collection_names():
    # Create a new collection for cases
    cases_collection = db.create_collection("cases")
    print("Cases collection created successfully.")
else:
    print("Cases collection already exists.")

# Check if the config collection exists
if "config" not in db.list_collection_names():
    # Create a new collection for config
    config_collection = db.create_collection("config")
    print("Config collection created successfully.")
else:
    print("Config collection already exists.")

# Check if the inputs collection exists
if "inputs" not in db.list_collection_names():
    # Create a new collection for inputs
    inputs_collection = db.create_collection("inputs")
    print("Inputs collection created successfully.")
else:
    print("Inputs collection already exists.")
