import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
df = pd.read_csv('insurance.csv')

# Split features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Preprocessing: One-hot encode categorical variables
categorical_features = ['sex', 'smoker', 'region']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'  # Keep numeric columns
)

# Create pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train model
model.fit(X, y)

# ✅ Save the model
with open('insurance_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model training complete. File saved as 'insurance_model.pkl'")
