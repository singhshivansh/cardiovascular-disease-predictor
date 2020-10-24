# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:25:05 2020

@author: Shivansh
"""
import pickle
import streamlit as st

pickle_in = open("cardio_vascular_model.pickle", "rb")
classifier = pickle.load(pickle_in)

def predict_cardio(age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active,
                     bmi):
    prediction = str(classifier.predict([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, bmi]]))
    print(prediction)
    return prediction

def main():
    st.title("CardioVascular Disease Predictor")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit CardioVascular Disease Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    age = st.text_input("Age", "Type Here")
    gender = st.text_input("Gender", "Type Here")
    height = st.text_input("Height", "Type Here")
    weight = st.text_input("Weigth", "Type Here")
    ap_hi = st.text_input("Diastolic Blood Pressure", "Type Here")
    ap_lo = st.text_input("Systolic Blood Pressure", "Type Here")
    cholesterol = st.text_input("Cholestrol", "Type Here")
    gluc = st.text_input("Glucose", "Type Here")
    smoke = st.text_input("Smoking", "Type Here")
    alco = st.text_input("Alcohol", "Type Here")
    active = st.text_input("Active", "Type Here")
    bmi = st.text_input("BMI(Body Mass Index)", "Type Here")
    result = ""
    
    if st.button("Predict"):
        result = predict_cardio(age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active,bmi)
    
    #if result == 1:
     #   st.success("You have CVD")
   # if result == 0:
    #    st.success("You are Disease-free :)")
    st.success("The Output is {}".format(result))
    
    
if __name__ == '__main__':
    main()
    #result = predict_cardio(22469, 1, 155, 69.0, 130, 80, 2, 2, 0, 0, 1, 28.72)
    #print(result)