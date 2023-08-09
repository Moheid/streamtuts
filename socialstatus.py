## Project name: Building first streamlit app
## Project date: 2023-08-08 
## Project author: Mohamed Ibrahim

## 1. Load the dependencie library/packages
import streamlit as st
import numpy as np


## 2. Create project title 

st.title("Pracital Streamlit App Resource")

st.header('Course Materials')

if st.button("learn"):
    st.write("Get more information soon, we are making some progress.")
else:
    st.write('We find here our latest updates, keep in touch with us. Thanks for your visiting')

## 3. Create 4 Columns 

col1, col2, col3, col4 = st.columns(4)
data = np.random.rand(1, 500000)

with col1:
    st.header("Facebook")
    st.write("450K")

with col2:
    st.header("Twitter")
    st.write("50K")

with col3:
    st.header("Instagram")
    st.write("35K")
with col4:
    st.header("Youtube")
    st.write("250K")

tab1, tab2, tab3, tab4 = st.tabs(["Facebook", "Twitter", "Intagram", "Youtube"])
data = np.random.randn(10, 1)

with tab1:
    st.subheader("Facebook Followers")
    st.line_chart(data)
with tab2:
    st.subheader("Twitter Followers")
    st.bar_chart(data)
with tab3:
    st.subheader("Instagram Followers")
    st.bar_chart(data)
with tab4:
    st.subheader("Youtube Subscribers")
    st.area_chart(data)
