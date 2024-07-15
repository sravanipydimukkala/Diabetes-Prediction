# Diabetes-Prediction  
A simple machine learning model that predicts whether a patient has diabetic condition or not.  
Collaborated Project with https://github.com/bhavithareddy-05
# DataSet
In this model i have created a synthetic dataset that contains the following attributes:  
# Attributes:  
1.Age  
2.BMI  
3.Glucose  
4.Blood-Pressure  
5.Cholestrol  
6.Family history of diabetes  
7.Physical Activity  
8.Diabetes(Target)  

## Note:  
The values in the dataset are fake.For that i have created a python code that assigns random values to the above attributes.You can use the same code and change the attributes or increase number of attributes to predict more precisely.
# Models:  
I have used four different models for diabetic prediction.  
1.Logistic Regression  
2.Support Vector Machine  
3.Decision Tree  
4.Random Forest
#### ColabNoteBook:https://colab.research.google.com/drive/1JlwmQ88hXFUPZiW77eIZHJF2Jo63feTz?usp=drive_link
# Threshold values:  
The attributes mentioned in the dataset have some threshold values, and when the threshold is reached then the model predicts diabetes.  
### 1.Age:
Age group above 60 yrs are likely to get diabetes.  
### 2.BMI:
Normal Weight: BMI < 25  
Overweight: BMI 25 - 29.9  
Obese: BMI ≥ 30  
Individuals with higher BMI (especially in the overweight and obese range) are at an increased risk of developing diabetes.  
### 3.Glucose:
Normal Fasting Glucose: < 100 mg/dL  
  Prediabetes: 100 - 125 mg/dL  
  Diabetes: ≥ 126 mg/dL  
  Elevated fasting glucose indicates impaired glucose metabolism and inturn leads to diabetes.
### 4.Blood Pressure:
Normal Blood Pressure: < 120/80 mm Hg  
  Prehypertension: 120-139/80-89 mm Hg  
  Hypertension: ≥ 140/90 mm Hg  
  High blood pressure (hypertension) is associated with diabetes risk.Hypertension increases the risk of cardiovascular complications in people with diabetes.     
### 5. Cholesterol:
#### Total Cholesterol:  
  Desirable: < 200 mg/dL  
  Borderline High: 200 - 239 mg/dL  
  High: ≥ 240 mg/dL  
  #### LDL Cholesterol (Bad Cholesterol):  
  Optimal: < 100 mg/dL  
  Near Optimal: 100 - 129 mg/dL  
  High: ≥ 130 mg/dL  
  #### HDL Cholesterol (Good Cholesterol):  
  Low: < 40 mg/dL (men), < 50 mg/dL (women)  
  Desirable: ≥ 60 mg/dL  
  Abnormal cholesterol levels contribute to diabetes complications.  
### 6.Family history:
Having a close family member (parent or sibling) with diabetes increases your risk.
### 7.Physical Activity:
An average of 150 minutes of physical activity can prevent diabetes.And it can be splitted into 30 minutes per day for five days.  

