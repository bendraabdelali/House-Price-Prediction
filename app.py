import streamlit as st 
import numpy as np
import pandas as pd
import joblib

# from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from function import MS_Zoning , Sale_Type
model = joblib.load('model.joblib')

st.title('House Price Prediction ? :ship:')
# LotFrontage ,  LotArea , YearBuilt , GarageCars  , MSZoning , Bedroom  , Kitchen ,  SaleType ,  YrSold  , _2ndFlrSF 
LotFrontage = st.number_input("Input Linear feet of street connected to property ", 21) 
LotArea  =  st.number_input("Lot size in square feet")
YearBuilt = st.slider("old of the  house",10)
YearBuilt =  2023- YearBuilt 
GarageCars = st.slider("Size of garage in car capacity",0,9)

MSZoning1 =  st.selectbox("Identifies the general zoning classification of the sale. ", [
       "C	Commercial",
       "FV	Floating Village Residential",
       "RH	Residential High Density",
       "RL	Residential Low Density",
       "RP	Residential Low Density Park", 
       "RM	Residential Medium Density",
])
        
MSZoning =  MS_Zoning(MSZoning1)        

Bedroom = st.number_input("Number of Bedrooms ")
Kitchen = st.number_input("Number of Kitchen ")
SaleType1 = st.selectbox("Type of sale", [
       "WD 	Warranty Deed - Conventional",
       "CWD	Warranty Deed - Cash",
       "New	Home just constructed and sold",
       "COD	Court Officer Deed/Estate",
       "Con	Contract 15% Down payment regular terms",
       "ConLw	Contract Low Down payment and low interest",
       "ConLI	Contract Low Interest",
       "ConLD	Contract Low Down",
       "Oth	Other"
       ])


SaleType = Sale_Type(SaleType1)

YrSold =  st.slider("Year Sold",10)

_2ndFlrSF =  st.slider("Second floor square feet if you don't went enter 0",0,4 ) 






def predict(): 
    row =[190,MSZoning,LotFrontage,LotArea,1,3,3,0,4,0,3,2,2,0,0,7,7,YearBuilt,YearBuilt,1,1,13,14,2,0.0,2,2,0,5,0.0,5,
        0.0,0.0,_2ndFlrSF,2,2,0,4,596,0,LotArea,0.0,0.0,2,1,Bedroom,Kitchen,0,6,0,5,GarageCars,1,0,0,0,0,90,100,0,
        10,YrSold,SaleType,4,9]
    X = pd.DataFrame([row])
    prediction = model.predict(X) 
    back = np.expm1(prediction)
    back =  round(back[0], 2)
    
    st.success("a house with this feature it will be {}$".format(back))

trigger = st.button('Predict', on_click=predict)