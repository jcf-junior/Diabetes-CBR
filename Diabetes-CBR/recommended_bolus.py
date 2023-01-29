from new_case import *
from db_connection import *
from find_neighbors import *
from k_nn import *

# determine recommended insulin bolus
recommended_insulin_bolus = 0
for neighbor in nearest_neighbors:
    recommended_insulin_bolus += neighbor["Recommended Insulin Bolus"]
recommended_insulin_bolus /= k

def getInsulin():
    # print recommended insulin bolus
    print("Recommended Insulin Bolus: {} U".format(round(recommended_insulin_bolus, 2)))