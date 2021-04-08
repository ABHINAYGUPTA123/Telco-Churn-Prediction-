# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 01:33:48 2021

@author: onward
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_telco_churn():
    
    
    SeniorCitizen=request.args.get("SeniorCitizen")
    Partner=request.args.get("Partner")
    Dependents=request.args.get("Dependents")
    tenure=request.args.get("tenure")
    InternetService =request.args.get("InternetService")   
    OnlineSecurity=request.args.get("OnlineSecurity")
    OnlineBackup=request.args.get("OnlineBackup")
    DeviceProtection=request.args.get("DeviceProtection")
    TechSupport=request.args.get("TechSupport")
    StreamingMovies=request.args.get("StreamingMovies")
    Contract=request.args.get("Contract")
    PaperlessBilling=request.args.get("PaperlessBilling")
    PaymentMethod=request.args.get("PaymentMethod")
    MonthlyCharges =request.args.get("MonthlyCharges")
    TotalCharges=request.args.get("TotalCharges")
    prediction=classifier.predict([[SeniorCitizen, Partner, Dependents, tenure, InternetService,
       OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport,
       StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
       MonthlyCharges, TotalCharges]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(port=8000)