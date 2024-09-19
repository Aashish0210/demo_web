import streamlit as st
import pandas as pd


st.set_page_config(page_title='hello',page_icon='tada')
# to import csv file
# df=pd.read_csv('student_scores6.csv')

# st.write(df)

name=st.text_input('Enter your name')
father=st.text_input('Enter Father name')
add=st.text_area('Enter your address')
css=st.selectbox('Enter class',[1,2,3,4,5,6])
if st.button('Done'):
    st.markdown(f"""
    name: {name}
    father: {father}
    addresss: {add}
    css: {css}
                """)

