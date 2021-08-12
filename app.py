#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import pickle
import pandas as pd
import streamlit as st

model=pickle.load(open('impact.pkl','rb'))

def welcome():
    return "Welcome"




def main():
    st.title('Imapct Prediction')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Impact Prediction App</h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
   
    opened_by=st.text_input('opened_by') 
    number=st.text_input('number')
    location=st.text_input('location')
    resolved_by=st.text_input('assignment_group')
    assigned_to=st.text_input('made_sla')
    made_sla=st.text_input('assigned_to')
    u_symptom=st.text_input('u_symptom')
    assignment_group=st.text_input('resolved_by')
    sys_updated_by=st.text_input('sys_updated_by')
    

    

    st.title('Predict The Impact here....!')
    html_temp = """
    <div style="background-color:tomato;padding:5px">
    <h3 style="color:white;text-align:center;"></h3>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    if st.button(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Click Here . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . "):
        features=[[opened_by,number,location,assignment_group,made_sla,assigned_to,u_symptom,resolved_by,sys_updated_by]]
        print(features)
        prediction = model.predict(features)
        print(prediction)
        lc=[str(i) for i in prediction]
        result=int("".join(lc))
        
#         st.success(f'The output is {prediction}')
        
        
        if result == 1:
            st.success('The Impact of this incident will be Low')
        elif result == 2:
            st.success('The Impact of this incident will be Medium')
            st.write(":smile:")
        else:
            st.success('The Impact of this incident will be High')
            
    if st.button("About"):
        st.write("This is Machine Learning Project to predict the Impact of the incident that occured. Thise is a Multiclass classification Project. This project was held by ExcelR institute and Guided by Vinod Sir And Kavi priya Mam.")
    if st.button("Credits"):
        st.write("Shivani Shiralkar | Apurva Pachagade | Shital Jadhav | Kiran Bhongal | Sagar Khande ")

    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Thank You..!</h3>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)        
if __name__=='__main__':
    main()
    


# In[ ]:




