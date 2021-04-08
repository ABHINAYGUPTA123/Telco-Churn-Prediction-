# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:54:28 2021

@author: onward
"""
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_telco_churn(SeniorCitizen, tenure, MonthlyCharges,TotalCharges,
       Partner_Yes, Dependents_Yes, InternetService_Fiber_optic,
       InternetService_No, OnlineSecurity_No_internet_service,
       OnlineSecurity_Yes, OnlineBackup_No_internet_service,
       OnlineBackup_Yes, DeviceProtection_No_internet_service,
       DeviceProtection_Yes, TechSupport_No_internet_service,
       TechSupport_Yes, StreamingMovies_No_internet_service,
       StreamingMovies_Yes, Contract_One_year, Contract_Two_year,
       PaperlessBilling_Yes, PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electroni_check, PaymentMethod_Mailed_check,
       tenure_group_13_24, tenure_group_25_36, tenure_group_37_48,
       tenure_group_49_60, tenure_group_61_72):
    
    
    prediction=classifier.predict([[SeniorCitizen, tenure, MonthlyCharges,TotalCharges,
       Partner_Yes, Dependents_Yes, InternetService_Fiber_optic,
       InternetService_No, OnlineSecurity_No_internet_service,
       OnlineSecurity_Yes, OnlineBackup_No_internet_service,
       OnlineBackup_Yes, DeviceProtection_No_internet_service,
       DeviceProtection_Yes, TechSupport_No_internet_service,
       TechSupport_Yes, StreamingMovies_No_internet_service,
       StreamingMovies_Yes, Contract_One_year, Contract_Two_year,
       PaperlessBilling_Yes, PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electroni_check, PaymentMethod_Mailed_check,
       tenure_group_13_24, tenure_group_25_36, tenure_group_37_48,
       tenure_group_49_60, tenure_group_61_72]])
    print(prediction)
    return prediction

   
   


def main():
    st.title("Telco Churn")
    html_temp = """
    <div style="background-color:purple;padding:10px">
    <h2 style="color:black;text-align:center;">Customer Churn ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    SeniorCitizen = st.text_input("SeniorCitizen","Type Here")
    tenure = st.text_input("tenure","Type Here")
    MonthlyCharges = st.text_input("MonthlyCharges","Type Here")
    TotalCharges = st.text_input("TotalCharges","Type Here")
    Partner_Yes = st.text_input("Partner_Yes","Type Here")
    Dependents_Yes = st.text_input("Dependents_Yes","Type Here")
    InternetService_Fiber_optic = st.text_input("InternetService_Fiber optic","Type Here")
    InternetService_No = st.text_input("InternetService_No","Type Here")
    OnlineSecurity_No_internet_service = st.text_input("OnlineSecurity_No internet service","Type Here")
    OnlineSecurity_Yes = st.text_input("OnlineSecurity_Yes","Type Here")
    OnlineBackup_No_internet_service = st.text_input("OnlineBackup_No internet service","Type Here")
    OnlineBackup_Yes = st.text_input("OnlineBackup_Yes","Type Here")
    DeviceProtection_No_internet_service = st.text_input("DeviceProtection_No internet service","Type Here")
    DeviceProtection_Yes = st.text_input("DeviceProtection_Yes","Type Here")
    TechSupport_No_internet_service = st.text_input("TechSupport_No internet service","Type Here")
    TechSupport_Yes = st.text_input("TechSupport_Yes","Type Here")
    StreamingMovies_No_internet_service = st.text_input("StreamingMovies_No internet service","Type Here")
    StreamingMovies_Yes = st.text_input("StreamingMovies_Yes","Type Here")
    Contract_One_year = st.text_input("Contract_One year","Type Here")
    Contract_Two_year = st.text_input("Contract_Two year","Type Here")
    PaperlessBilling_Yes = st.text_input("PaperlessBilling_Yes","Type Here")
    PaymentMethod_Credit_card_automatic = st.text_input("PaymentMethod_Credit card (automatic)","Type Here")
    PaymentMethod_Electronic_check = st.text_input("PaymentMethod_Electronic","Type Here")
    PaymentMethod_Mailed_check = st.text_input("check PaymentMethod_Mailed check","Type Here")
    tenure_group_13_24 = st.text_input("tenure_group_13 - 24","Type Here")
    tenure_group_25_36 = st.text_input("tenure_group_25 - 36","Type Here")
    tenure_group_37_48 = st.text_input("tenure_group_37 - 48","Type Here")
    tenure_group_49_60 = st.text_input("tenure_group_49 - 60","Type Here")
    tenure_group_61_72 = st.text_input("tenure_group_61 - 72","Type Here")
    
    
    
    result=""
    if st.button("Predict"):
        result=predict_telco_churn(SeniorCitizen, tenure, MonthlyCharges,TotalCharges,
       Partner_Yes, Dependents_Yes, InternetService_Fiber_optic,
       InternetService_No, OnlineSecurity_No_internet_service,
       OnlineSecurity_Yes, OnlineBackup_No_internet_service,
       OnlineBackup_Yes, DeviceProtection_No_internet_service,
       DeviceProtection_Yes, TechSupport_No_internet_service,
       TechSupport_Yes, StreamingMovies_No_internet_service,
       StreamingMovies_Yes, Contract_One_year, Contract_Two_year,
       PaperlessBilling_Yes, PaymentMethod_Credit_card_automatic,
       PaymentMethod_Electronic_check, PaymentMethod_Mailed_check,
       tenure_group_13_24, tenure_group_25_36, tenure_group_37_48,
       tenure_group_49_60, tenure_group_61_72)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()