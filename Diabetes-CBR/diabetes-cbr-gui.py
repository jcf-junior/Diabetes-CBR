import tkinter as tk
import json

# root undefined fix
root = tk.Tk()
root.title("Diabetes CBR")

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

k_label = tk.Label(root, text="Enter the value of k: ")
k_label.grid(row=12, column=0)
k_entry = tk.Entry(root)
k_entry.grid(row=12, column=1)
k = int(k_entry.get())

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
    time_of_day_entry = tk.Entry(root)
    time_of_day_entry.grid(row=11, column=1)
    time_of_day = time_of_day_entry.get()
    new_case = {'Preprandial BG': bg, 'IOB': iob, 'BG Target': bg_target, 'CHO': cho, 'Weight': weight, 'ICR': icr, 'ISF': isf, 'Pre-activity duration': pre_activity_duration, 'Pre-activity heart rate': pre_activity_hr, 'Post-activity duration': post_activity_duration, 'Post-activity intensity': post_activity_intensity, 'Time of day': time_of_day}
    return new_case

def cbr(new_case):
    nearest_neighbors = find_nearest_neighbors(new_case, k)
    recommended_insulin_bolus = sum(case['Insulin bolus'] for case in nearest_neighbors) / k
    label = tk.Label(root, text=f'Recommended insulin bolus: {recommended_insulin_bolus}')
    label.grid(row=13, column=1)

submit_button = tk.Button(root, text="Submit", command=lambda: cbr(get_inputs()))

