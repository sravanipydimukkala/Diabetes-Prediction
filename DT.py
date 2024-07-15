from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
df = pd.read_csv('diabetes_training_data.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
tree_model = DecisionTreeClassifier(random_state=42)

tree_model.fit(X_train, y_train)
y_pred = tree_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Tree Model Accuracy on Test Set: {accuracy * 100:.2f}%")

def get_user_input():
    print("Please enter the following details to predict diabetes risk:")
    age = float(input("Age: "))
    bmi = float(input("Body Mass Index (BMI): "))
    glucose = float(input("Fasting Blood Sugar Level: "))
    blood_pressure = float(input("Blood Pressure: "))
    cholesterol = float(input("Cholesterol Level: "))
    family_history = int(input("Family History of Diabetes (1 for Yes, 0 for No): "))
    physical_activity = float(input("Physical Activity Level (in minutes): "))
    
    user_data = np.array([[age, bmi, glucose, blood_pressure, cholesterol, family_history, physical_activity]])
    return user_data

user_data = get_user_input()

user_prediction = tree_model.predict(user_data)

if user_prediction == 1:
    print("The model predicts that you may have diabetes.")
else:
    print("The model predicts that you may not have diabetes.")
