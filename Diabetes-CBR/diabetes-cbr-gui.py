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

def get_inputs():
    # Blood Glucose
    bg_label = tk.Label(root, text="Enter your current blood glucose level: ")
    bg_label.grid(row=0, column=0)
    bg_entry = tk.Entry(root)
    bg_entry.grid(row=0, column=1)
    bg = float(bg_entry.get())
    
    # Insulin on Board
    iob_label = tk.Label(root, text="Enter your current Insulin on Board: ")
    iob_label.grid(row=1, column=0)
    iob_entry = tk.Entry(root)
    iob_entry.grid(row=1, column=1)
    iob = float(iob_entry.get())
    
    # Blood Glucose Target
    bg_target_label = tk.Label(root, text="Enter your desired blood glucose level: ")
    bg_target_label.grid(row=2, column=0)
    bg_target_entry = tk.Entry(root)
    bg_target_entry.grid(row=2, column=1)
    bg_target = float(bg_target_entry.get())
    
    # Carbohydrates
    cho_label = tk.Label(root, text="Enter the amount of carbohydrates you will consume: ")
    cho_label.grid(row=3, column=0)
    cho_entry = tk.Entry(root)
    cho_entry.grid(row=3, column=1)
    cho = float(cho_entry.get())
    
    # Weight
    weight_label = tk.Label(root, text="Enter your current weight (kg): ")
    weight_label.grid(row=4, column=0)
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=4, column=1)
    weight = float(weight_entry.get())
    
    # Carbohydrate Ratio
    icr_label = tk.Label(root, text="Enter your Carbohydrate Ratio (g/U): ")
    icr_label.grid(row=5, column=0)
    icr_entry = tk.Entry(root)
    icr_entry.grid(row=5, column=1)
    icr = float(icr_entry.get())

    # Insulin Sensitivity Factor
    isf_label = tk.Label(root, text="Enter your Insulin Sensitivity Factor (mg/dL/U): ")
    isf_label.grid(row=6, column=0)
    isf_entry = tk.Entry(root)
    isf_entry.grid(row=6, column=1)
    isf = float(isf_entry.get())

    # Pre-Activity Duration
    pre_activity_duration_label = tk.Label(root, text="Enter the duration of your pre-activity (minutes): ")
    pre_activity_duration_label.grid(row=7, column=0)
    pre_activity_duration_entry = tk.Entry(root)
    pre_activity_duration_entry.grid(row=7, column=1)
    pre_activity_duration = float(pre_activity_duration_entry.get())

    # Pre-Activity Heart Rate
    pre_activity_hr_label = tk.Label(root, text="Enter your pre-activity heart rate (bpm): ")
    pre_activity_hr_label.grid(row=8, column=0)
    pre_activity_hr_entry = tk.Entry(root)
    pre_activity_hr_entry.grid(row=8, column=1)
    pre_activity_hr = float(pre_activity_hr_entry.get())

    #    # Pre-Activity Intensity
    pre_activity_intensity_label = tk.Label(root, text="Enter the intensity of your pre-activity (1-6): ")
    pre_activity_intensity_label.grid(row=9, column=0)
    pre_activity_intensity_entry = tk.Entry(root)
    pre_activity_intensity_entry.grid(row=9, column=1)
    pre_activity_intensity = int(pre_activity_intensity_entry.get())

    # Post-Activity Duration
    post_activity_duration_label = tk.Label(root, text="Enter the duration of your post-activity (minutes): ")
    post_activity_duration_label.grid(row=10, column=0)
    post_activity_duration_entry = tk.Entry(root)
    post_activity_duration_entry.grid(row=10, column=1)
    post_activity_duration = float(post_activity_duration_entry.get())
    
    # Post-Activity Heart Rate
    post_activity_hr_label = tk.Label(root, text="Enter your post-activity heart rate (bpm): ")
    post_activity_hr_label.grid(row=11, column=0)
    post_activity_hr_entry = tk.Entry(root)
    post_activity_hr_entry.grid(row=11, column=1)
    post_activity_hr = float(post_activity_hr_entry.get())
    
    # Post-Activity Intensity
    post_activity_intensity_label = tk.Label(root, text="Enter the intensity of your post-activity (1-6): ")
    post_activity_intensity_label.grid(row=12, column=0)
    post_activity_intensity_entry = tk.Entry(root)
    post_activity_intensity_entry.grid(row=12, column=1)
    post_activity_intensity = int(post_activity_intensity_entry.get())

    # Time of Day
    time_of_day_label = tk.Label(root, text="Enter the time of day (morning, afternoon, evening): ")
    time_of_day_label.grid(row=13, column=0)
    time_of_day_entry = tk.Entry(root)
    time_of_day_entry.grid(row=13, column=1)
    time_of_day = time_of_day_entry.get()

    # K value
    k_label = tk.Label(root, text="Enter your k value: ")
    k_label.grid(row=14, column=0)
    k_entry = tk.Entry(root)
    k_entry.grid(row=14, column=1)
    k = float(k_entry.get())


    submit_button = tk.Button(root, text="Submit", command=lambda: cbr(bg, iob, bg_target, cho, weight, icr, isf, pre_activity_duration, pre_activity_hr, pre_activity_intensity, post_activity_duration, post_activity_hr, post_activity_intensity, time_of_day, k))
    submit_button.grid(row=15, column=0, columnspan=2, pady=10)
    submit_button.config(width=10)
    return [bg, iob, bg_target, cho, weight, icr, isf, pre_activity_duration, pre_activity_hr, post_activity_duration, post_activity_hr, time_of_day, k]


def cbr(new_case):
    nearest_neighbors = find_nearest_neighbors(new_case, k)
    recommended_insulin_bolus = sum(case['Insulin bolus'] for case in nearest_neighbors) / k
    label = tk.Label(root, text=f'Recommended insulin bolus: {recommended_insulin_bolus}')
    label.grid(row=13, column=1)

submit_button = tk.Button(root, text="Submit", command=lambda: cbr(get_inputs()))

root = tk.Tk()
get_inputs()
root.mainloop()
