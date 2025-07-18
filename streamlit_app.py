import streamlit as st

pages = {
    "Pages":
    [ 
        st.Page("pages/home.py", title = "home"),
        st.Page("pages/cura_chatbot.py", title = "Cura ChatBot"),
        st.Page("pages/bias_analysis.py", title = "Bias Analysis"),
        st.Page("pages/statistics.py", title = "Statistics"),
        st.Page("pages/future_aspirations.py", title = "Future Aspirations"),
        st.Page("pages/sources.py", title = "Sources"),
        st.Page("pages/contact_us.py", title = "Contact Us")
    ]
}
pg = st.navigation(pages)
pg.run()


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');

.stApp {
    max-width: 900px;
    margin: 2rem auto;
    padding: 2rem 3rem;
    font-family: 'Merriweather', serif;
    background-color: #FFFFFF;
    color: #042A66;
}

/* Your other CSS styles here, e.g. headers, buttons, sidebar */
h1, h2, h3 {
    color: #0B3D91 !important;
    font-weight: 800;
    margin-bottom: 1.5rem;
}

.stButton>button {
    background-color: #0B3D91 !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 0.7rem 1.8rem !important;
    font-weight: 700 !important;
    border: none !important;
    box-shadow: 0 3px 8px rgba(11, 61, 145, 0.3);
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.stButton>button:hover {
    background-color: #093170 !important;
    box-shadow: 0 6px 16px rgba(9, 49, 112, 0.6);
    cursor: pointer !important;
}

section[data-testid="stSidebar"] {
    background-color: #F5F8FD !important;
    padding: 2rem 1.5rem !important;
    border-radius: 0 15px 15px 0 !important;
    color: #042A66 !important;
    font-weight: 600 !important;
    box-shadow: inset 2px 0 4px rgba(11, 61, 145, 0.1);
}

section[data-testid="stSidebar"] h2 {
    color: #0B3D91 !important;
    font-weight: 800 !important;
}

a {
    color: #0B3D91 !important;
    text-decoration: none !important;
    font-weight: 600 !important;
}

a:hover {
    text-decoration: underline !important;
}

.css-1n76uvr, .css-1r6slb0, .stTextInput>div>div>input {
    border: 1.5px solid #0B3D91 !important;
    border-radius: 10px !important;
    padding: 0.4rem 0.8rem !important;
}

.stButton, .stTextInput, .stSelectbox, .stSlider {
    margin-bottom: 1.5rem !important;
}
</style>
""", unsafe_allow_html=True)