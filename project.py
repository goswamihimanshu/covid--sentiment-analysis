import streamlit as st


import data_app as da

import ml_app as ma

def main():

    #EDA
    da.main()

    st.header("LogisticRegression Prediction")

    #Predictor
    ma.main()

if(__name__=='__main__'):
    main()
