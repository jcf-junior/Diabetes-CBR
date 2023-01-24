from math import sqrt

# Euclidean distance metric
def euclidean_distance(case1, case2):
    distance = 0
    for key in case1:
        if key != "Recommended Insulin Bolus" and key != "Day time":
            distance += (case1[key] - case2[key]) ** 2
    return sqrt(distance)

# Manhattan distance metric
def manhattan_distance(case1, case2):
    distance = 0
    for key in case1:
        if key != "Recommended Insulin Bolus" and key != "Day time":
            distance += abs(case1[key] - case2[key])
    return distance

# Minkowski distance metric
def minkowski_distance(case1, case2, n):
    distance = 0
    for key in case1:
        if key != "Recommended Insulin Bolus" and key != "Day time":
            distance += abs(case1[key] - case2[key]) ** n
    return distance ** (1/n)

# Cosine similarity metric
def cosine_similarity(case1, case2):
    dot_product = sum(case1[key] * case2[key] for key in case1 if key != "Recommended Insulin Bolus" and key != "Day time")
    norm_case1 = sqrt(sum(case1[key] ** 2 for key in case1 if key != "Recommended Insulin Bolus" and key != "Day time"))
    norm_case2 = sqrt(sum(case2[key] ** 2 for key in case2 if key != "Recommended Insulin Bolus" and key != "Day time"))
    return 1 - (dot_product / (norm_case1 * norm_case2))
