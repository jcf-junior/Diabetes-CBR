from new_case import *
from k_nn import *
from db_connection import *

# determine recommended insulin bolus
recommended_insulin_bolus = 0
for neighbor in nearest_neighbors:
    recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
recommended_insulin_bolus /= k

# print recommended insulin bolus
print("Recommended Insulin Bolus: {} U".format(round(recommended_insulin_bolus, 2)))