import streamlit as st

pages = {
    "Pages":
    [ 
        st.Page("pages/home.py", title = "home"),
        st.Page("pages/symptom_checker.py", title = "Symptom Checker"),
        st.Page("pages/bias_analysis.py", title = "Bias Analysis"),
        st.Page("pages/statistics.py", title = "Statistics"),
        st.Page("pages/doctor_resources.py", title = "Doctor's Resources"),
        st.Page("pages/sources.py", title = "Sources"),
        st.Page("pages/contact_us.py", title = "Contact Us")
    ]
}
pg = st.navigation(pages)
pg.run()