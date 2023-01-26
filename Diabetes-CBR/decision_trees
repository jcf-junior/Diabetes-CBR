import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# read cases from JSON file
with open("cases.json", "r") as f:
    cases = json.load(f)
    for case in cases:
        # fix for KeyError: Time of day
        case["Time of day"] = 0

# convert cases to a pandas dataframe
df = pd.DataFrame(cases)

# split data into features (X) and target (y)
X = df[['Preprandial BG', 'IOB', 'BG Target', 'CHO', 'Patient weight', 'ICR', 'ISF', 
       'Physical activity preprandial - Duration', 'Physical activity preprandial - Heart rate', 
       'Physical activity preprandial - Intensity', 'Physical activity postprandial - Duration', 
       'Physical activity postprandial - Intensity', 'Time of day']]

X.fillna(X.mean(), inplace=True)


#Convert 'Recommended Insulin Bolus' into categorical
y = pd.cut(df['Recommended Insulin Bolus'], bins=[0,1,3,5], labels=['Low','Medium', 'High'])

# read inputs from JSON file
with open("inputs.json", "r") as f:
    inputs = json.load(f)

# convert inputs to a pandas dataframe
new_case = pd.DataFrame(inputs, index=[0])

print(new_case.isnull().sum())


# train decision tree model
clf = DecisionTreeClassifier()
clf.fit(X, y)

# make prediction using the new case
prediction = clf.predict(new_case)[0]

# print the recommended insulin bolus
print("Recommended Insulin Bolus:", prediction)

# train random forest model
rf = RandomForestClassifier()
rf.fit(X, y)

# make prediction using the new case
prediction = rf.predict(new_case)[0]

# print the recommended insulin bolus
print("Recommended Insulin Bolus:", prediction)