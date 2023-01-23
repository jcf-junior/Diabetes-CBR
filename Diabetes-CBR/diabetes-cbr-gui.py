import tkinter as tk
import json

def find_nearest_neighbors(new_case, k):
    # load cases from json file
    with open('cases.json') as file:
        cases = json.load(file)
    distances = []
    for case in cases:
        distance = euclidean_distance(new_case, case)
        distances.append((distance, case))
    distances.sort()
    nearest_neighbors = [case for _, case in distances[:k]]
    return nearest_neighbors
    
def euclidean_distance(case1, case2):
    distance = 0
    for key in case1:
        if key != 'Insulin bolus':
            distance += (case1[key] - case2[key]) ** 2
    return distance ** 0.5

def get_inputs():
    bg_entry = tk.Entry(root)
    bg_entry.grid(row=0, column=1)
    bg = float(bg_entry.get())
    iob_entry = tk.Entry(root)
    iob_entry.grid(row=1, column=1)
    iob = float(iob_entry.get())
    bg_target_entry = tk.Entry(root)
    bg_target_entry.grid(row=2, column=1)
    bg_target = float(bg_target_entry.get())
    cho_entry = tk.Entry(root)
    cho_entry.grid(row=3, column=1)
    cho = float(cho_entry.get())
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=4, column=1)
    weight = float(weight_entry.get())
    icr_entry = tk.Entry(root)
    icr_entry.grid(row=5, column=1)
    icr = float(icr_entry.get())
    isf_entry = tk.Entry(root)
    isf_entry.grid(row=6, column=1)
    isf = float(isf_entry.get())
    pre_activity_duration_entry = tk.Entry(root)
    pre_activity_duration_entry.grid(row=7, column=1)
    pre_activity_duration = float(pre_activity_duration_entry.get())
    pre_activity_hr_entry = tk.Entry(root)
    pre_activity_hr_entry.grid(row=8, column=1)
    pre_activity_hr = float(pre_activity_hr_entry.get())
    post_activity_duration_entry = tk.Entry(root)
    post_activity_duration_entry.grid(row=9, column=1)
    post_activity_duration = float(post_activity_duration_entry.get())
    post_activity_intensity_entry = tk.Entry(root)
    post_activity_intensity_entry.grid(row=10, column=1)
    post_activity_intensity = float(post_activity_intensity_entry.get())
    # labels
    k_label = tk.Label(root, text="Enter the value of k: ")
    k_label.grid(row=12, column=0)
    k_entry = tk.Entry(root)
    k_entry.grid(row=12, column=1)
    k = int(k_entry.get())


def cbr(new_case):
    nearest_neighbors = find_nearest_neighbors(new_case, k)
    insulin_bolus_list = [case['Insulin bolus'] for case in nearest_neighbors]
    recommended_insulin_bolus = sum(insulin_bolus_list) / len(insulin_bolus_list)
    result_label = tk.Label(root, text="Recommended insulin bolus: {:.2f} U".format(recommended_insulin_bolus))
    result_label.grid(row=13, column=0)


