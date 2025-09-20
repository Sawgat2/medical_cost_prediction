import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/medical_cost_model.pkl")  # Load model

st.title("Medical Cost Prediction App")

# User inputs
age = st.number_input("Age",18,100,30)
bmi = st.number_input("BMI",10.0,50.0,25.0)
children = st.number_input("Number of Children",0,10,0)
sex = st.selectbox("sex",["male","female"])
smoker = st.selectbox("Smoker",["yes","no"]),
region = st.selectbox("Region",["northwest","northeast","southeast","southwest"])


input_data = pd.DataFrame({
    "age":[age],
    "bmi":[bmi],
    "children":[children],
    "sex":[sex],
    "smoker":[smoker],
    "region":[region]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Medical Cost: ${prediction[0]:,.2f}")