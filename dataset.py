import csv
import random

headers = ["Age", "BMI", "Glucose", "BloodPressure", "Cholesterol", "FamilyHistory", "PhysicalActivity", "Diabetes"]
synthetic_data = [headers]

for _ in range(100):
    age = random.randint(20, 60)
    bmi = round(random.uniform(18, 32), 1)
    glucose = random.randint(90, 140)
    blood_pressure = random.randint(100, 150)
    cholesterol = random.randint(170, 240)
    family_history = random.choice([0, 1])
    physical_activity = random.randint(15, 60)
    diabetes = random.choice([0, 1])

    row = [age, bmi, glucose, blood_pressure, cholesterol, family_history, physical_activity, diabetes]
    synthetic_data.append(row)

csv_file_path = "synthetic_diabetes_data.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(synthetic_data)

print(f"Synthetic data has been saved to {csv_file_path}")
