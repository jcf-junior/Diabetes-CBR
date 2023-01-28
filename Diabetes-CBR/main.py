import importlib
from db_connection import *

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
