from datetime import datetime
import streamlit as st
import sys
import os
from datetime import datetime

# -------------------------------------------------------
# Add project root to Python path
# -------------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.predict import predict_water

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="wide"
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------
st.sidebar.title("💧 Water Potability")

st.sidebar.markdown("""
## About

This application predicts whether water is safe for drinking using a **Random Forest Machine Learning model**.

### Model Details
- **Algorithm:** Random Forest Classifier
- **Accuracy:** 66.92%
- **Features:** 9
- **Output:** Potable / Not Potable

**Dataset:** Kaggle Water Potability Dataset
""")

# -------------------------------------------------------
# Title
# -------------------------------------------------------
st.title("💧 Water Potability Prediction System")

st.markdown("""
Predict whether water is **safe for drinking**
using a trained **Random Forest Machine Learning model**.
""")

st.markdown("---")

# -------------------------------------------------------
# Input Fields
# -------------------------------------------------------
st.subheader("Enter Water Quality Parameters")

col1, col2, col3 = st.columns(3)

with col1:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        help="Recommended drinking water pH: 6.5 - 8.5"
    )

    hardness = st.number_input(
        "Hardness",
        value=200.0,
        help="Typical range: 60 - 180 mg/L"
    )

     chloramines = st.number_input(
        "Chloramines",
        value=7.0,
        help="Disinfectant used in water treatment"
    )
  

with col2:

   

    sulfate = st.number_input(
        "Sulfate",
        value=330.0,
        help="Recommended level: below 250 mg/L"
    )

     turbidity = st.number_input(
        "Turbidity",
        value=4.0,
        help="Recommended value: below 5 NTU"
    )


st.markdown("---")

# -------------------------------------------------------
# Prediction Button
# -------------------------------------------------------
if st.button("🔍 Predict Water Quality", use_container_width=True):

    # Input Validation
    if (
        hardness <= 0 or
        solids <= 0 or
        chloramines <= 0 or
        sulfate <= 0 or
        conductivity <= 0 or
        organic_carbon <= 0 or
        trihalomethanes <= 0 or
        turbidity <= 0
    ):
        st.error("Please enter valid positive values for all water quality parameters.")
        st.stop()

    prediction, probability = predict_water(
        ph,
        hardness,
        chloramines,
        sulfate,
        turbidity
    )

    # -------------------------------------------------------
    # Prediction Result
    # -------------------------------------------------------
    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Water is Safe for Drinking")
    else:
        st.error("❌ Water is NOT Safe for Drinking")

    st.caption(
        f"Prediction generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    # -------------------------------------------------------
    # Prediction Probability
    # -------------------------------------------------------
    st.markdown("### Prediction Probability")

    st.write(f"❌ Not Potable : {probability[0]*100:.2f}%")
    st.progress(float(probability[0]))

    st.write(f"✅ Potable : {probability[1]*100:.2f}%")
    st.progress(float(probability[1]))

    # -------------------------------------------------------
    # Entered Parameters
    # -------------------------------------------------------
    st.markdown("---")

    st.subheader("Entered Water Parameters")

    st.table({
        "Parameter": [
            "pH",
            "Hardness",
            "Chloramines",
            "Sulfate",
            "Turbidity"
        ],
        "Value": [
            ph,
            hardness,
            chloramines,
            sulfate,
            turbidity
        ]
    })

# -------------------------------------------------------
# Input Parameters
# -------------------------------------------------------
st.markdown("---")

st.subheader("Input Parameters")

st.write("""
- pH
- Hardness
- Chloramines
- Sulfate
- Turbidity
""")

# -------------------------------------------------------
# Reference Water Quality Values
# -------------------------------------------------------
st.markdown("---")

st.subheader("Reference Water Quality Values")

st.table({
    "Parameter": [
        "pH",
        "Hardness",
        "Chloramines",
        "Sulfate",
        "Turbidity"
    ],
    "Recommended Range": [
        "6.5 - 8.5",
        "60 - 180 mg/L",
        "< 4 mg/L",
        "< 250 mg/L",
        "< 5 NTU"
    ]
})

# -------------------------------------------------------
# Model Information
# -------------------------------------------------------
st.markdown("---")

st.subheader("Model Information")

st.write("**Algorithm:** Random Forest Classifier")
st.write("**Accuracy:** 66.92%")
st.write("**Dataset:** Kaggle Water Potability Dataset")
st.write("**Number of Features:** 9")
st.write("**Target Variable:** Potability")

# -------------------------------------------------------
# Water Quality Guidelines
# -------------------------------------------------------
st.markdown("---")

st.subheader("💡 Drinking Water Guidelines")

st.info("""
✔ The ideal **pH** for drinking water is between **6.5 and 8.5**.

✔ Lower **Turbidity** usually indicates cleaner water.

✔ Excess **Chloramines** and **Sulfate** may reduce water quality.

✔ This prediction is generated by a Machine Learning model and should **not replace laboratory water testing**.
""")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.markdown("---")
st.caption("Developed by Sirigadde Sowjanya | B.Tech (Artificial Intelligence & Data Science)")
