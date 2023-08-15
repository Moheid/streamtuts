# Project Name: App naviation 
# Date created: 15 Aug, 2023

import streamlit as st
from streamlit_option_menu import option_menu  #pip install streamlit-option-menu

# 1. Create Sidebar menu 
with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu", #required
        options=["Facebook", "Twitter", "Youtube", "Instagram", "Linkedin"] # required
    )

if selected == "Home":
    st.title(f"Facebook Insights {selected}")
if selected == "Twitter":
    st.title(f"Twitter Equity {selected}")
if selected == "Youtube":
    st.title(f"Youtube Insights {selected}")
if selected == "Instagram":
    st.title(f"Instagram Insights Performance {selected}")
if selected == "Linkedin":
    st.title(f"Linkedin Insights {selected}")
