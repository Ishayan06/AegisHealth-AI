# import os
# import pickle

# import numpy as np
# import pandas as pd
# import streamlit as st

# # Debug: Print current working directory and file paths
# print("Current working directory:", os.getcwd())
# print("Model file path:", os.path.abspath('diabetes_model.pkl'))
# print("Dataset file path:", os.path.abspath('diabetes.xlsx'))
# print("HTML file path:", os.path.abspath('diabetes.html'))

# # Load the model
# try:
#     model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
#     with open(model_path, 'rb') as file:
#         model = pickle.load(file)
# except FileNotFoundError:
#     st.error(f"Error: 'diabetes_model.pkl' file not found at: {model_path}")
#     st.stop()

# # Function to predict diabetes
# def predict_diabetes(features):
#     features = np.array(features).reshape(1, -1)
#     prediction = model.predict(features)
#     return prediction

# # Streamlit app
# def main():
#     st.title("Diabetes Prediction App")
#     st.write("Please enter the following details to predict diabetes:")

#     # Input fields
#     pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
#     glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
#     blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=150, value=0)
#     skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=0)
#     insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=900, value=0)
#     bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
#     diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.0)
#     age = st.number_input("Age", min_value=0, max_value=120, value=0)

#     # Predict button
#     if st.button("Predict"):
#         features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
#         prediction = predict_diabetes(features)
#         if prediction[0] == 1:
#             st.error("The model predicts that the person has diabetes.")
#         else:
#             st.success("The model predicts that the person does not have diabetes.")

#     # Display the dataset
#     st.write("### Diabetes Dataset")
#     try:
#         dataset_path = os.path.join(os.path.dirname(__file__), 'diabetes.xlsx')
#         df = pd.read_excel(dataset_path)
#         st.write(df)
#     except FileNotFoundError:
#         st.error(f"Error: 'diabetes.xlsx' file not found at: {dataset_path}")

#     # Display the HTML file
#     st.write("### Diabetes Information")
#     try:
#         html_path = os.path.join(os.path.dirname(__file__), 'diabetes.html')
#         with open(html_path, 'r') as file:
#             html_content = file.read()
#         st.components.v1.html(html_content, height=500)
#     except FileNotFoundError:
#         st.error(f"Error: 'diabetes.html' file not found at: {html_path}")

# if __name__ == "__main__":
#     main()
import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Global Styles */
    body {
        font-family: 'Georgia', serif;
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        color: white;
    }

    .css-1egviio {  /* This targets the main content area */
        background: linear-gradient(to right, #3b82f6, #8b5cf6); /* Set the background gradient */
        color: white; /* Ensure text is readable */
    }

    .stApp { /* targets the whole app frame */
        background:  linear-gradient(to right, #3b82f6, #8b5cf6);
        color: white; /* set default text color to white */
    }

    .stButton button {
        background-color: #3b82f6;
        color: white;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #2563eb;
    }
    .stNumberInput input, .stTextInput input {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        color: black; /* Set input text to black for readability */
    }
    .stMarkdown h1 {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        color: white;
    }
    .stMarkdown h2 {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        color: white;
    }
    .stMarkdown h3 {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
        color: white;
    }
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stAlert {
        border-radius: 10px;
    }
    .stSuccess {
        background-color: #10b981;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .stError {
        background-color: #ef4444;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    /* Input Labels */
    .stNumberInput label, .stTextInput label {
        color: white;
    }

    /* Ensure input text is readable */

    </style>
    """,
    unsafe_allow_html=True,
)

# Debug: Print current working directory and file paths
print("Current working directory:", os.getcwd())
print("Model file path:", os.path.abspath('diabetes_model.pkl'))
print("Dataset file path:", os.path.abspath('diabetes.xlsx'))
print("HTML file path:", os.path.abspath('diabetes.html'))

# Load the model
try:
    model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Error: 'diabetes_model.pkl' file not found at: {model_path}")
    st.stop()

# Function to predict diabetes
def predict_diabetes(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction

# Streamlit app
def main():
    st.title("Diabetes Prediction App")
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Know Your Health Risks</h1>
            <p>Get personalized insights into your health risks with our advanced risk prediction tool.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input fields
    st.markdown("### Please enter the following details to predict diabetes:")
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
        blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=150, value=0)
        skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=0)
    with col2:
        insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=900, value=0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0)
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.0)
        age = st.number_input("Age", min_value=0, max_value=120, value=0)

    # Predict button
    if st.button("Predict"):
        features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        prediction = predict_diabetes(features)
        if prediction[0] == 1:
            st.error("The model predicts that the person has diabetes.")
        else:
            st.success("The model predicts that the person does not have diabetes.")

    # Display the dataset
    st.markdown("### Diabetes Dataset")
    try:
        dataset_path = os.path.join(os.path.dirname(__file__), 'diabetes.xlsx')
        df = pd.read_excel(dataset_path)
        st.dataframe(df.style.set_properties(**{'background-color': 'white', 'color': 'black', 'border-radius': '10px'}))
    except FileNotFoundError:
        st.error(f"Error: 'diabetes.xlsx' file not found at: {dataset_path}")

    # Display the HTML file
    st.markdown("### Diabetes Information")
    try:
        html_path = os.path.join(os.path.dirname(__file__), 'diabetes.html')
        with open(html_path, 'r') as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=500)
    except FileNotFoundError:
        st.error(f"Error: 'diabetes.html' file not found at: {html_path}")

if __name__ == "__main__":
    main()
