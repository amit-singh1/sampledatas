# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:44:38 2020

@author: amit
"""

import streamlit as st
import pandas as pd
import xlrd

st.title("Enter Your GRE SCORE")

user_input = st.text_input("250+ scores will provide a decent university")


DATA_URL = r'C:\Users\amit\Project\New folders\sampledatas\grees.xlsx'

df = pd.read_excel(DATA_URL)

##df = xlrd.open_workbook("greee.xlsx")

if user_input!="":
    val = int(user_input)
    st.dataframe(df[df['Scores']<val])

else :
    st.write("Results will show up here")