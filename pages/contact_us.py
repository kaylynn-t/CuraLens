import streamlit as st

st.title("Contact Us")

st.markdown("### Connect with Our Team on LinkedIn")

team = {
    "Emily Hu": "https://www.linkedin.com/in/emily-hu-199763373/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
    "Kaylynn Tan": "https://www.linkedin.com/in/kaylynn-t-9b286126a/",
    "Swarnika Narayanan": "https://www.linkedin.com/in/swarnika-narayanan-036a072a7/",
    "Prisha Banushali": "https://www.linkedin.com/in/prisha-bhanushali-37b374227/",
    "Malaz Ahmed": "https://www.linkedin.com/in/emmapatel"
}

for person, link in team.items():
    st.markdown(f"""
    <a href="{link}" target="_blank" style="
        text-decoration:none;
        color:#0B3D91;
        font-weight:700;
        font-size:18px;
        display:flex;
        align-items:center;
        margin-bottom:0.8rem;
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="24" height="24" style="margin-right:8px;">
        {person}
    </a>
    """, unsafe_allow_html=True)

st.image("images/team_photo.JPG", caption = "(Left to right) Kaylynn, Prisha, *Non-Project Member*, Emily, Swarnika")
st.image("images/team_photo2.JPG", caption = "(Left to right) Prisha, Malaz, Swarnika")
st.image("images/team_photo3.JPG", caption = "(Left to right) Swarnika, Kaylynn, Emily, *Non-Project Member*, Prisha")
