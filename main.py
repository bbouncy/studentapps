import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

st.title("Schools Based on Your Preferences")

#Sidebar#
st.sidebar.title("Filters")

Location = st.sidebar.multiselect('Location',
                 options=['1','2','3','4'])

Tuition = st.sidebar.slider('Choose Maximum Tuition',
                            min_value=0, max_value=100)

DegreeType = st.sidebar.multiselect('Choose which type of degree you are interested in',
                                    options=['Certification', 'Associates Degree', "Bachelor's Degree", "Graduate Degree"])

Offerings = st.sidebar.multiselect('Academic Offerings',
                                   options=['1', '2', '3', '4'])

#Accordian#

with st.expander("School Name"): st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)

with st.expander("School Name"): st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
