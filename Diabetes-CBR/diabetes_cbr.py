import importlib
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Get the config collection
config_collection = client['cbr']['config']

# Find the config document
config = config_collection.find_one()

# Get the selected algorithm from the config document
selected_algorithm = config["data"]["selected_algorithm"]

# Import the selected algorithm's module
imported_module = importlib.import_module(selected_algorithm)

# Run the selected algorithm's run() function
try:
    if __name__ == '__main__':
        imported_module.run()
except AttributeError as e:
    print("The selected algorithm does not have a 'run' function.\nExiting...")
    exit()
