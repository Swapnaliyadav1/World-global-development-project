# -*- coding: utf-8 -*-
"""

#"""
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide',page_title='Global Development Clustering Analysis')
#st.title('Global Development Clustering Analysis')
df=pd.read_csv(r"C:\Users\Admin\Desktop\Clustered_ World_Development_Data.csv",index_col=0)
data=df.copy()
df=df.drop(columns='cluster')

def load_country_analysis(country):
 # load the information of contry
    country_data = df[df['country']==country]
    st.subheader('Country data')
    st.write(f"Analysis for {country}")
    st.dataframe(country_data)
    
def similar_country_data(similar_country):
    similar_country_data = data[data['cluster']==similar_country]
    st.subheader('Similar_country_data')
    st.dataframe(similar_country_data)
    
st.sidebar.title('Analysis')

option = st.sidebar.selectbox('Select One',['country Analysis','Similarity'])

if option=='country Analysis':
    country=st.sidebar.selectbox('Select country',df['country'])
    btn1 = st.sidebar.button('Find country Details')
    st.title('country Analysis')
    if btn1:
        load_country_analysis(country)

else:
    
    st.title('similar country Analysis')
    similar_country=st.sidebar.selectbox('Select country options',data['cluster'].drop_duplicates())
    btn2=st.sidebar.button('Find similar country development')
    if btn2:
        similar_country_data(similar_country)
        