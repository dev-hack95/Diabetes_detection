import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("./models/Random_Forest.pkl", 'rb'))

scalar = pickle.load(open('./models/scalar.pkl', 'rb'))




######################################### Streamlit #########################################

st.title("Diabetes Detrction")

Glucose = st.number_input("Glucose: ")
BloodPressure= st.number_input("BloodPressure: ")
SkinThickness = st.number_input("SkinThickness: ")
Insulin = st.number_input("Insulin: ")
BMI = st.number_input("BMI: ")
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction: ")
Age = st.number_input("Age: ")


data = [Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
data = np.reshape(data, (1, -1))
new_data = scalar.transform(data)

prediction = model.predict(new_data)

submit = st.button('Predict')
if submit:
    if prediction[0] == 0:
        st.write("Healthy")
    else:
        st.write("Diabetic")