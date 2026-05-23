# Diabetes Prediction ML Project
# Overview
This Machine Learning project predicts whether a person is diabetic or not using medical attributes such as glucose level, BMI, blood pressure, age, etc.
The project uses Support Vector Machine (SVM) algorithm for classification.
---
## Dataset Information
Dataset Used:
PIMA Indians Diabetes Dataset
Features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
Target:
- 0 = Non-Diabetic
- 1 = Diabetic
---
## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab
- Matplotlib
- Seaborn
---
## Machine Learning Workflow
1. Data Collection
2. Data Analysis
3. Data Preprocessing
4. Data Standardization
5. Train-Test Split
6. Model Training using SVM
7. Model Evaluation
8. Prediction System
---
## Model Accuracy
Training Accuracy: 78%

Testing Accuracy: 77%
---

## Installation Steps
1. Clone the repository
```bash
git clone https://github.com/yourusername/diabetes-prediction-ml-project.git
```
2. Install libraries
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
3. Run the project
```bash
python diabetes_prediction.py
```
---
## Project Output
Example Prediction:
```python
Input:
(4,110,92,0,0,37.6,0.191,30)
Output:
The person is NOT diabetic
```
---
## Future Improvements
- Add Streamlit Web App
- Deploy model online
- Add multiple ML models
- Improve accuracy
- Add real-time prediction UI
---
## Author
Sajal Srivastava
