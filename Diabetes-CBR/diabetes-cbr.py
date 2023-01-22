import json
from math import sqrt

# read cases from JSON file
with open("cases.json", "r") as f:
    cases = json.load(f)

# function to calculate euclidean distance
def euclidean_distance(case1, case2):
    distance = 0
    for key in case1:
        if key != "Recommended Insulin Bolus":
            distance += (case1[key] - case2[key]) ** 2
    return sqrt(distance)

# function to find k nearest neighbors
def find_nearest_neighbors(new_case, k):
    distances = []
    for case in cases:
        distance = euclidean_distance(new_case, case)
        distances.append((case, distance))
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:k]]

# new case to predict insulin bolus
new_case = {
    "Preprandial BG": 150,
    "IOB": 0.5,
    "BG Target": 110,
    "CHO": 50,
    "Patient weight": 75,
    "ICR": 20,
    "ISF": 40,
    "Physical activity preprandial - Duration": 30,
    "Physical activity preprandial - Heart rate": 70,
    "Physical activity preprandial - Intensity": 3,
    "Physical activity postprandial - Duration": 20,
    "Physical activity postprandial - Intensity": 2,
    "Day time": "14:30"
}

# number of nearest neighbors
k = 3

# find k nearest neighbors
neighbors = find_nearest_neighbors(new_case, k)
print("K nearest neighbors:")
for neighbor in neighbors:
    print(neighbor)

# predict insulin bolus
insulin_bolus = sum([neighbor["Recommended Insulin Bolus"] for neighbor in neighbors]) / k
print("Predicted insulin bolus:", insulin_bolus)
