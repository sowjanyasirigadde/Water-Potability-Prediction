import os
import joblib
import pandas as pd

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
MODEL_PATH = os.path.join(BASE_DIR, "model", "water_potability_model.pkl")

# Load model
model = joblib.load(MODEL_PATH)


def predict_water(
    ph,
    hardness,
    solids,
    chloramines,
    sulfate,
    conductivity,
    organic_carbon,
    trihalomethanes,
    turbidity
):

    # Create input dataframe
    data = pd.DataFrame([[
        ph,
        hardness,
        solids,
        chloramines,
        sulfate,
        conductivity,
        organic_carbon,
        trihalomethanes,
        turbidity
    ]], columns=[
        "ph",
        "Hardness",
        "Solids",
        "Chloramines",
        "Sulfate",
        "Conductivity",
        "Organic_carbon",
        "Trihalomethanes",
        "Turbidity"
    ])

    # Predict class
    prediction = model.predict(data)[0]

    # Get probability of both classes
    probability = model.predict_proba(data)[0]

    return prediction, probability