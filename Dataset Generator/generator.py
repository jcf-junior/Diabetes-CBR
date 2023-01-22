import random
import json

# generate random cases
cases = []
for i in range(10):
    case = {}
    case["Preprandial BG"] = random.randint(50, 250)
    case["IOB"] = round(random.uniform(0, 1), 2)
    case["BG Target"] = random.choice([100, 110])
    case["CHO"] = random.randint(25, 80)
    case["Patient weight"] = random.randint(50, 140)
    case["ICR"] = random.randint(8, 23)
    case["ISF"] = random.randint(25, 55)
    case["Physical activity preprandial - Duration"] = random.randint(0, 100)
    case["Physical activity preprandial - Heart rate"] = random.randint(40, 110)
    case["Physical activity preprandial - Intensity"] = random.randint(0, 6)
    case["Physical activity postprandial - Duration"] = random.randint(0, 100)
    case["Physical activity postprandial - Intensity"] = random.randint(0, 6)
    case["Day time"] = f"{random.randint(0,23)}:{random.randint(0,59)}"
    case["Recommended Insulin Bolus"] = round(random.uniform(0, 12), 2)
    cases.append(case)

# write cases to JSON file
with open("cases.json", "w") as f:
    json.dump(cases, f)
