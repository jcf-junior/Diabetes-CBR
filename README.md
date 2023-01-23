# Diabetes-CBR

This program is a simulation of a case-based reasoning (CBR) system for diabetes management. It uses the k-NN algorithm to determine the recommended insulin bolus for a new case based on the similarity to existing cases in a JSON file.

## Usage
1. Clone or download the repository
2. Run the program using Python 3
3. The program will prompt the user to enter the inputs for a new case
4. The program will then use the k-NN algorithm to determine the recommended insulin bolus for the new case based on the similarity to existing cases in the JSON file
5. The recommended insulin bolus will be displayed on the screen

## Inputs

- Preprandial Blood Glucose (BG) – [50-250] mg/dL
- IOB – [0-1] U
- BG Target – 100 or 110 mg/dL
- Carbohydrates Amount (CHO) – [25-80] g
- Patient weight – [50-140] kg
- ICR – [8-23]
- ISF – [25-55]
- Physical activity preprandial:
..* Duration- [0 - 100] min
..* Heart rate- [40-110] bpm or intensity [0-6]
- Physical activity postprandial:
..* Duration- [0 - 100] min
..* Intensity- [0-6]
- Day time - (hh:mm)

## Output

- Recommended Insulin Bolus- [0-12] U

## Requirements
- Python 3
- json library


## Disclaimer: 
