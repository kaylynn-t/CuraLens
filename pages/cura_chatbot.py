import streamlit as st
import pandas as pd

# Load the disease data
@st.cache_data
def load_data():
    df = pd.read_csv("diseases.csv")
    return df

df = load_data()

# Title and intro
st.title("Cura Chatbot")
st.write("Enter your symptoms below to get possible conditions and treatment suggestions.")

# Input field
prompt = st.text_input("Describe your symptoms:")

# Simple diagnosis function
def get_diagnosis(symptom_input, df):
    if not symptom_input.strip():
        return ""
    
    matches = df[df['Symptoms'].str.contains(symptom_input, case=False, na=False)]
    
    if not matches.empty:
        result = ""
        for index, row in matches.iterrows():
            result += f"**Possible Condition:** {row['Disease']}\n\n"
            result += f"**Suggested Treatment:** {row['Treatment']}\n\n---\n\n"
        return result
    else:
        return "❗Sorry, we couldn't find a match for those symptoms. Please consider reaching out to a medical professional."

# Display results
if prompt:
    response = get_diagnosis(prompt, df)
    st.markdown(response)

# Disclaimer
st.write("**This tool is not a substitute for professional medical advice, diagnosis, or treatment.**")

