import json

if __name__ == '__main__':
    # Read selected algorithm from JSON file
    with open("config.json", "r") as f:
        config = json.load(f)
        selected_algorithm = config["selected_algorithm"]

    # Import and run selected algorithm
    algorithm = __import__(selected_algorithm)
    algorithm.run()