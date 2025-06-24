# task3
# 💼 Insurance Cost Predictor Web App

## ✅ Internship Project – Full Data Science Pipeline

- **Company**: CodTech IT Solutions  
- **Name**: Jami Venkata Dhanush  
- **Intern ID**: CT06DL1263  
- **Domain**: Data Science  
- **Duration**: 6 Weeks  
- **Mentor**: Neela Santhosh  

---

## 🎯 Project Objective

Develop and deploy a full end-to-end Data Science project using Flask. The application predicts a person’s insurance cost based on demographic and health-related inputs using a trained machine learning model.

---

## 🧠 Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **Machine Learning**: Scikit-learn, Pandas  
- **Model Storage**: Pickle  
- **Deployment Ready**: Flask-based local API  

---

## 📊 Dataset

- **File**: `insurance.csv`  
- **Source**: Kaggle  
- **Features**:
  - `age`: Age of the person
  - `sex`: Gender
  - `bmi`: Body Mass Index
  - `children`: Number of children
  - `smoker`: Smoking status
  - `region`: Residential area
- **Target**: `charges` – Medical insurance cost

---

## 🏗️ Project Structure

task3/
├── app.py                 # Flask app to handle requests and render the frontend
├── train_model.py         # Script to train the regression model and save it as a .pkl file
├── insurance.csv          # Dataset used for training the model
├── insurance_model.pkl    # Saved model pipeline (includes encoder and regressor)
├── templates/
│   └── index.html         # HTML frontend interface for collecting user input
├── static/                # (Optional) Folder for static files like CSS or JavaScript
├── screenshots/           # (Optional) Folder for storing screenshots of UI and outputs
└── README.md              # Project documentation (this file)
### output
![Image](https://github.com/user-attachments/assets/8b71e1dc-8e7f-4736-a4a5-67da808b0900)

