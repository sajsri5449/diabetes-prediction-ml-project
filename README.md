# 🩺 Diabetes Prediction ML Project

# 📌 Project Overview
This project is a Machine Learning based Diabetes Prediction System developed using Python and Scikit-learn.
The system predicts whether a person is diabetic or non-diabetic based on important medical parameters such as glucose level, BMI, insulin, age, blood pressure, etc.

The project also includes a Streamlit web application for real-time prediction.
---
# 🎯 Objectives
- Predict diabetes using Machine Learning
- Perform data preprocessing and analysis
- Train ML classification model
- Evaluate model accuracy
- Build a real-time prediction system
- Deploy model using Streamlit
---
# 📂 Dataset Information
Dataset Used:
PIMA Indians Diabetes Dataset
Total Records:
768
Total Features:
8
Target Variable:
- 0 → Non-Diabetic
- 1 → Diabetic
Features Used:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
---
# 🛠 Technologies Used
## Programming Language
- Python
## Libraries
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
## Platform
- Google Colab
- GitHub
---
# ⚙ Machine Learning Workflow
## 1️⃣ Data Collection
Loaded diabetes dataset using Pandas.

## 2️⃣ Data Analysis
Performed statistical analysis using:
- head()
- describe()
- value_counts()

## 3️⃣ Data Preprocessing
Separated:
- Features (X)
- Labels (Y)

## 4️⃣ Data Standardization
Used StandardScaler to normalize data.

## 5️⃣ Train-Test Split
Dataset divided into:
- 80% Training Data
- 20% Testing Data

## 6️⃣ Model Training
Used Support Vector Machine (SVM) classifier.

## 7️⃣ Model Evaluation
Calculated training and testing accuracy.

## 8️⃣ Prediction System
Created predictive system using user input values.
--
# 🤖 Machine Learning Model Used
## Support Vector Machine (SVM)
SVM is a supervised machine learning algorithm used for classification problems.
Reason for choosing SVM:
- Good accuracy
- Works well on classification datasets
- Efficient for smaller datasets
---
# 📈 Model Accuracy
| Type | Accuracy |
|------|-----------|
| Training Accuracy | 78% |
| Testing Accuracy | 77% |
---
# 🖥 Streamlit Web Application
This project also includes a Streamlit web app where users can:
✅ Enter medical data  
✅ Predict diabetes instantly  
✅ Use model through browser interface
Run locally using:
```bash
streamlit run app.py
```
---
# 📊 Workflow Diagram
Dataset
↓
Data Analysis
↓
Data Preprocessing
↓
Feature Scaling
↓
Train-Test Split
↓
SVM Model Training
↓
Prediction System
↓
Accuracy Evaluation

---

# 🚀 Future Improvements

- Add Multiple ML Models
- Improve Accuracy
- Deploy Online
- Add User Authentication
- Create Mobile-Friendly UI
- Add Real-Time Health Recommendations

---

# 📦 Installation Steps

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sajsri5449/diabetes-prediction-ml-project.git
```

## 2️⃣ Install Required Libraries

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

## 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 💡 Example Prediction

Input:

```python
(4,110,92,0,0,37.6,0.191,30)
```

Output:

```python
The person is NOT diabetic
```

---

# 📁 Project Structure

```bash
diabetes-prediction-ml-project/
│
├── app.py
├── diabetes.csv
├── Diabetes_Prediction_.ipynb
├── diabetes_prediction_.py
├── requirements.txt
├── README.md
```

---

# 👨‍💻 Author

## Sajal Srivastava

Machine Learning & Data Science Enthusiast

---

# ⭐ Conclusion

This project demonstrates the complete Machine Learning workflow from data preprocessing to deployment using Streamlit.

The project helped in understanding:
- Data preprocessing
- Feature scaling
- Classification algorithms
- Model evaluation
- Web app deployment using Streamlit
