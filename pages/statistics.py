import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

st.title("Statistics")

tab1, tab2, tab3 = st.tabs([
    "Food Insecurity vs. Health Care Access",
    "Health Insurance Status",
    "Health Issues in Berkeley"
])

with tab1:
    st.subheader("Food Insecurity vs. Health Care Access by Demographic Group")
    # Add more content here if needed

with tab2:
    st.subheader("Health Insurance Status Among Food Insecure Residents")

    data_berkeley = pd.Series({
        'Medicaid (Medi-Cal)': 40,
        'Uninsured': 33,
        'Employer-sponsored': 10,
        'Covered CA (ACA)': 9,
        'Medicare': 5,
        'Other': 3
    })

    fig, ax = plt.subplots(figsize=(7, 7))
    data_berkeley.plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title('Health Insurance Status Among Food-Insecure Residents (Berkeley, 2023)')
    ax.set_ylabel('')  # removes default y-axis label

    st.pyplot(fig)

with tab3:
    st.subheader("Health Issues Among Food-Insecure 18-29 year olds in Berkeley")

    data = pd.DataFrame({
        'Health Condition': ['Diabetes', 'Hypertension', 'Obesity', 'Depression/Anxiety', 'Heart Disease', 'Poor Dental Health'],
        '18–29': [5, 8, 16, 42, 2, 18]
    })

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(data['Health Condition'], data['18–29'], color='skyblue')
    ax.set_title('Health Issues Among Food-Insecure 18–29 Year Olds in Berkeley (2023)', fontsize=13)
    ax.set_ylabel('Percentage Affected')

    ax.set_xticks(range(len(data['Health Condition'])))
    ax.set_xticklabels(data['Health Condition'], rotation=30, ha='right')

    st.pyplot(fig)