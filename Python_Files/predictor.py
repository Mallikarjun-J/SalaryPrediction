# Project: Salary Prediction
# Author: Malliakrjun
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from model_final import prepare_dataframe
import os

def load_model():
    # Get the absolute path to the model file relative to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(project_root, 'Model', 'model_3.pkl')
    with open(model_path, 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
model = data["MODEL"]
label_encoders = data["LABEL_ENCODERS"]
scaler = data["SCALER"]

def show_predict_page():
    # Professional Banner and Title
    st.markdown("""
        <div style='background: linear-gradient(90deg, #e0eafc 0%, #cfdef3 100%); padding: 2rem 1rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 2px 8px rgba(33,147,176,0.07);'>
            <h1 style='color: #1a4c7c; text-align: left; margin-bottom: 0; font-size: 2.2rem; font-weight: 700;'>Salary Prediction</h1>
            <p style='color: #3a3a3a; text-align: left; font-size: 1.15rem; margin-top: 0.5rem;'>Predict your software developer salary with AI-powered insights.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='font-size: 1.7rem; font-weight: 700; color: #1a4c7c; margin-bottom: 1.2rem; margin-top: 1.2rem; border-bottom: 2px solid #e0eafc; padding-bottom: 0.3rem;'>
            Personal Information
        </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        education_level = (
            'Bachelor’s degree (B.A., B.S., B.Eng., etc.)',
            'Some college/university study without earning a degree',
            'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
            'Primary/elementary school',
            'Professional degree (JD, MD, Ph.D, Ed.D, etc.)',
            'Associate degree (A.A., A.S., etc.)',
            'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
            'Something else'
        )
        education_input = st.selectbox("Education Level", education_level, key="education_level")

        age = (
            "18-24 years old",
            "25-34 years old",
            "35-44 years old",
            "45-54 years old",
            "55-64 years old",
            "65 years or older",
            "Prefer not to say"
        )
        age_input = st.selectbox("Age", age, key="age")

    with col2:
        dev_type = (
            'Senior Executive (C-Suite, VP, etc.)', 
            'Developer, back-end', 
            'Developer, front-end', 
            'Developer, full-stack', 
            'System administrator', 
            'Developer, QA or test', 
            'Designer', 
            'Data scientist or machine learning specialist', 
            'Data or business analyst', 
            'Security professional', 
            'Research & Development role', 
            'Developer, mobile', 
            'Database administrator', 
            'Developer, embedded applications or devices', 
            'Developer, desktop or enterprise applications', 
            'Engineer, data', 
            'Product manager', 
            'Academic researcher', 
            'Cloud infrastructure engineer', 
            'Other (please specify):', 
            'Developer Experience', 
            'Engineering manager', 
            'DevOps specialist', 
            'Engineer, site reliability', 
            'Project manager', 
            'Blockchain', 
            'nan', 
            'Developer, game or graphics', 
            'Developer Advocate', 
            'Hardware Engineer', 
            'Educator', 
            'Scientist', 
            'Marketing or sales professional', 
            'Student'
        )
        dev_type_input = st.selectbox("Developer Type", dev_type, key="dev_type")

        orgsize = (
            '2 to 9 employees', 
            '5,000 to 9,999 employees', 
            '100 to 499 employees', 
            '20 to 99 employees', 
            '1,000 to 4,999 employees', 
            '10 to 19 employees', 
            '10,000 or more employees', 
            '500 to 999 employees', 
            'Just me - I am a freelancer, sole proprietor, etc.', 
            'I don’t know',
            "NAN"
        )
        orgsize_input = st.selectbox("Organisation Size", orgsize, key="orgsize")

    st.markdown("""
        <div style='font-size: 1.7rem; font-weight: 700; color: #1a4c7c; margin-top: 2.2rem; margin-bottom: 1.2rem; border-bottom: 2px solid #e0eafc; padding-bottom: 0.3rem;'>
            Work Preferences
        </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        aiselect = ('Yes', "No, and I don't plan to", 'No, but I plan to soon')
        aiselect_input = st.selectbox("Do you currently use AI tools in your development process?", aiselect, key="aiselect")
        remoteworkselect = ('Remote', 'Hybrid (some remote, some in-person)', 'In-person',"Other")
        remotework_input = st.selectbox("Work Mode", remoteworkselect, key="remotework")
    with col2:
        experience_input = st.slider("Years of Experience", 0, 50, 3, key="experience")
        yearscode_input = st.slider("Years of Coding Experience", 0, 50, 3, key="yearscode")
        yearscodepro_input = st.slider("Years of Pro Coding Experience", 0, 50, 3, key="yearscodepro")
    with col3:
        languages_input = st.text_input("Programming Languages you have worked with (separate with ;)", "")
        databases_input = st.text_input("Databases you have worked with (separate with ;)", "")
        learning_sources_input = st.text_input("Learning Sources you have used (separate with ;)", "")

    with col1:
        currency = ('USD\tUnited States dollar', 'INR\tIndian rupee')
        currency_input = st.selectbox("Currency", currency, key="currency")

    st.markdown("""
        <div style='font-size: 1.45rem; font-weight: 700; color: #1a4c7c; margin-top: 2.2rem; margin-bottom: 1.2rem; border-bottom: 2px solid #e0eafc; padding-bottom: 0.3rem;'>
            Get Your Salary Prediction
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .stButton > button {
            background: linear-gradient(90deg, #e0eafc 0%, #cfdef3 100%);
            color: #1a4c7c;
            font-size: 1.15rem;
            font-weight: 700;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 2.5rem;
            margin: 1.2rem 0 1.5rem 0;
            box-shadow: 0 2px 8px rgba(33,147,176,0.10);
            transition: background 0.3s, box-shadow 0.3s;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #cfdef3 0%, #e0eafc 100%);
            box-shadow: 0 4px 16px rgba(33,147,176,0.18);
            color: #1a4c7c;
        }
        </style>
    """, unsafe_allow_html=True)
    if st.button("Predict Salary", use_container_width=True):
        # Prepare input for prediction
        user_input = pd.DataFrame({
            'EdLevel': [education_input],
            'Age': [age_input],
            'DevType': [dev_type_input],
            'OrgSize': [orgsize_input],
            'AISelect': [aiselect_input],
            'RemoteWork': [remotework_input],
            'Currency': [currency_input],
            'WorkExp': [experience_input],
            'YearsCode': [yearscode_input],
            'YearsCodePro': [yearscodepro_input],
            'LanguageHaveWorkedWith': [languages_input],
            'DatabaseHaveWorkedWith': [databases_input],
            'LearnCode': [learning_sources_input]
        })
        X = prepare_dataframe(user_input, model, label_encoders, scaler)
        salary = model.predict(X)[0]
        currency_symbol = "$"
        if "INR" in currency_input:
            salary = salary * 83  # USD to INR conversion
            currency_symbol = "₹"
        st.markdown(
            f"""
            <div style='background: linear-gradient(90deg, #e0eafc 0%, #cfdef3 100%); padding: 2rem 1rem; border-radius: 16px; margin: 2rem 0; text-align: center; color: #1a4c7c; font-size: 2rem; font-weight: bold; box-shadow: 0 4px 16px rgba(33,147,176,0.10);'>
                🎉 Your Estimated Salary:<br>
                <span style='font-size:2.5rem;'>{currency_symbol}{salary:,.2f}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<footer style='text-align: center; color: grey; margin-top: 2rem;'>© Malliakrjun</footer>", unsafe_allow_html=True)