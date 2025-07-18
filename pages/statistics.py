import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import warnings
import os

st.title("Statistics")

tab1, tab2, tab3, tab4, tab5, = st.tabs([
    "PreMature Death Based on County and State", 
    "Disease and Symptoms", 
    "Precautions to Dieases",
    "Disease + Other Symptoms of Patient",
    "Life Expectancy"
])

with tab1:
    st.write("")
with tab2:
    st.write("Hello!")
with tab3:
    st.write("Welcome")

# Clean up Streamlit output
warnings.filterwarnings('ignore')