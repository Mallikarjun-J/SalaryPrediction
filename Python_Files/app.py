import streamlit as st
from predictor import show_predict_page

with st.sidebar:
    st.markdown('''
        <div style="
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
            border-radius: 14px;
            padding: 1.5rem 1rem 1rem 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(33,147,176,0.07);
            color: #222;
            text-align: left;">
            <h2 style="color: #1a4c7c; margin-bottom: 0.7rem; font-size: 1.3rem; letter-spacing: 0.5px; font-weight: 700;">
                About This App
            </h2>
            <p style="font-size: 1.05rem; margin-bottom: 1.2rem; line-height: 1.5;">
                This application predicts software developer salaries based on your professional background and work details.
            </p>
            <div style="font-size: 1.02rem; margin-bottom: 0.4rem;">
                <span style="font-weight: 600; color: #1a4c7c;">Project:</span> Salary Prediction
            </div>
            <div style="font-size: 1.02rem;">
                <span style="font-weight: 600; color: #1a4c7c;">Author:</span> Malliakrjun
            </div>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('---')

show_predict_page()