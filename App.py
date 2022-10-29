# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import numpy as np
import streamlit as st
from statistics import mode

svm = pickle.load(open('C:/Users/Karth/Project/SVM_Model.sav', 'rb'))
rf = pickle.load(open('C:/Users/Karth/Project/RF_Model.sav', 'rb'))
dt = pickle.load(open('C:/Users/Karth/Project/DT_Model.sav', 'rb'))

def RF_Predict(Input_Data):
    input_data_as_array = np.array(Input_Data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)
    
#    svm_prediction = svm.predict(input_data_reshaped)
    rf_prediction = rf.predict(input_data_reshaped)
#   dt_prediction = dt.predict(input_data_reshaped)
    
#    prediction = mode([svm_prediction, rf_prediction, dt_prediction])[0]
    
    if (rf_prediction == 0):
        output = 'Survival Status: Positive'
        
    elif (rf_prediction == 1):
        output = 'Survival Status: Negative'
        
    else:
        output = 'Invalid Inputs'
    
    return output

def SVM_Predict(Input_Data):
    input_data_as_array = np.array(Input_Data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)
    
    svm_prediction = svm.predict(input_data_reshaped)
 #   rf_prediction = rf.predict(input_data_reshaped)
#   dt_prediction = dt.predict(input_data_reshaped)
    
#    prediction = mode([svm_prediction, rf_prediction, dt_prediction])[0]
    
    if (svm_prediction == 0):
        output = 'Survival Status: Positive'
        
    elif (svm_prediction == 1):
        output = 'Survival Status: Negative'
        
    else:
        output = 'Invalid Inputs'
    
    return output

def DT_Predict(Input_Data):
    input_data_as_array = np.array(Input_Data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)
    
#    svm_prediction = svm.predict(input_data_reshaped)
 #   rf_prediction = rf.predict(input_data_reshaped)
    dt_prediction = dt.predict(input_data_reshaped)
    
#    prediction = mode([svm_prediction, rf_prediction, dt_prediction])[0]
    
    if (dt_prediction == 0):
        output = 'Survival Status: Positive'
        
    elif (dt_prediction == 1):
        output = 'Survival Status: Negative'
        
    else:
        output = 'Invalid Inputs'
    
    return output



def main ():
    st.title('Thoracic Surgery Survival Status')
    
    FVC = st.text_input('FVC')
    FEV1 = st.text_input('FEV1')
    Performance = st.text_input('Perfomance')
    Pain = st.text_input('Pain')
    Haemoptysis = st.text_input('Haemoptysis')
    Dyspnoea = st.text_input('Dyspnoea')
    Cough = st.text_input('Cough')
    Weakness = st.text_input('Weakness')
    Tumor_Size = st.text_input('Tumor Size')
    Diabetes_Mellitus = st.text_input('Diabetes Mellitus')
    MI_6mo = st.text_input('MI 6mo')
    PAD = st.text_input('PAD')
    Smoking = st.text_input('Smoking') 
    Asthma = st.text_input('Asthma')
    Age = st.text_input('Age')
    
    
    Test_Result = ''
    Test_Result_RF = ''
    Test_Result_SVM = ''
    Test_Result_DT = ''
    
    if st.button('Show Result'):
        Test_Result_RF = RF_Predict([FVC, FEV1, Performance, Pain, Haemoptysis, 
                               Dyspnoea, Cough, Weakness, Tumor_Size, 
                               Diabetes_Mellitus, MI_6mo, PAD, Smoking, Asthma, Age])
        
        Test_Result_SVM = SVM_Predict([FVC, FEV1, Performance, Pain, Haemoptysis, 
                               Dyspnoea, Cough, Weakness, Tumor_Size, 
                               Diabetes_Mellitus, MI_6mo, PAD, Smoking, Asthma, Age])
        
        Test_Result_DT = DT_Predict([FVC, FEV1, Performance, Pain, Haemoptysis, 
                               Dyspnoea, Cough, Weakness, Tumor_Size, 
                               Diabetes_Mellitus, MI_6mo, PAD, Smoking, Asthma, Age])
        
        Test_Result = mode([Test_Result_RF, Test_Result_SVM, Test_Result_DT])
        
    st.success(Test_Result)
    


if __name__ == '__main__':
    main()


    
    
