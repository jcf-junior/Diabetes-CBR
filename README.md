[![CodeFactor](https://www.codefactor.io/repository/github/jcf-junior/diabetes-cbr/badge)](https://www.codefactor.io/repository/github/jcf-junior/diabetes-cbr)
# Dataset Generator

This script generates a dataset of random values within a specific range for each input. This dataset may not be accurate for real-world applications and should only be used for testing purposes.

# Diabetes-CBR

This program is a simulation of a case-based reasoning (CBR) system for diabetes management. It uses a specified algorithm to determine the recommended insulin bolus for a new case based on the similarity to existing cases in a database.

1. Clone or download the repository
2. Import the necessary requirements
```bash
pip install -r requirements.txt
```
3. Start the backend server using Python 3
```bash
sudo python3 db.py 
```
4. Generate a testing dataset (optional)
```bash
sudo python3 generator.py 
```
5. Run the program using Python 3
```bash
sudo python3 diabetes_cbr.py 
```
6. Choose what algorithm and metric should be used in the db.py file
7. The program will then retrieve the keys and use the selected algorithm and metric to determine the recommended insulin bolus for the new case based on the similarity to existing cases in the database
8. The recommended insulin bolus will be displayed on the screen

## Inputs

- Preprandial Blood Glucose (BG) – [50-250] mg/dL
- IOB – [0-1] U
- BG Target – 100 or 110 mg/dL
- Carbohydrates Amount (CHO) – [25-80] g
- Patient weight – [50-140] kg
- ICR – [8-23]
- ISF – [25-55]
- Physical activity preprandial:
  - Duration- [0 - 100] min
  - Heart rate- [40-110] bpm or intensity [0-6]
- Physical activity postprandial:
  - Duration- [0 - 100] min
  - Intensity- [0-6]
- Day time - (hh:mm)

## Output

- Recommended Insulin Bolus- [0-12] U


## Disclaimer: 
### This program is a simulation and should not be used for medical diagnosis or treatment. It should be used for educational and research purposes only. It's important to consult with a licensed professional before making any medical decisions.
