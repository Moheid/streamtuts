## Project name: Building first streamlit app
## Project date: 2023-08-08 
## Project author: Mohamed Ibrahim

## 1. Load the dependencie library/packages
import streamlit as st

## 2. Create project title 

st.title("Pracital streamlit app resource")

st.header('Course Materials')

if st.button("learn"):
    st.write("Get more information soon, we are making some progress.")
else:
    st.write('We find here our latest updates, keep in touch with us. Thanks for your visiting')