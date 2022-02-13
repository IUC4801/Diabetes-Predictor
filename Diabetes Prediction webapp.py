# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:02:21 2022

@author: Ayushi Chaudhuri
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/Ayushi Chaudhuri/Desktop/Diabetes/trained_model.sav','rb'))

#creating function to prediction

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    #Title for webpage
    st.title("Diabetes Prediction System")
    
    #getting input data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies=st.text_input("Number of Pregnencies")
    Glucose=st.text_input("Glucose level")
    BloodPressure=st.text_input("Blood Pressure value")
    SkinThickness=st.text_input("Skin Thickness value")
    Insulin=st.text_input("Insulin level")
    BMI =st.text_input("BMI value")
    DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
    Age=st.text_input("Age of the person")
    
    #code for prediction
    
    diagnosis=''
    
    #creating a button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)    
    
if __name__=='__main__':
    main()    
 