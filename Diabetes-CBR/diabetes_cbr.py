import importlib
import json

# read selected algorithm from JSON file
with open("config.json", "r") as f:
    config = json.load(f)
    selected_algorithm = config["selected_algorithm"]
    imported_module = importlib.import_module(selected_algorithm)

# run selected algorithm
try:
    if __name__ == '__main__':
        imported_module.run()
except AttributeError as e:
        print("The selected algorithm does not have a 'run' function.\nExiting...")
        exit()
