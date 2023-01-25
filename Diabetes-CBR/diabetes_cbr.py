import json
import importlib

# Read the selected algorithm from config.json
with open("config.json", "r") as f:
    config = json.load(f)
    selected_algorithm = config["selected_algorithm"]

# Import the selected algorithm
imported_module = importlib.import_module(selected_algorithm)

if __name__ == '__main__':
# Error handling
    try:
        imported_module.run()
    except AttributeError as e:
        print("Error: {}".format(e))
        print("Ensure that the imported module has a 'run' function.")
    